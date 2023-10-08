from django.conf import settings
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from mainapp.forms import DogForm, FoodForm, ParentForm
from mainapp.models import Breed, Dog, Food, Parent


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'
    extra_context = {
        'title': 'Популярные породы'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Breed.objects.all()[:3]
        return context_data


class BreedListView(ListView):
    model = Breed
    extra_context = {
        'title': 'Все породы'
    }


class BreedDetailView(DetailView):
    model = Breed


class DogListView(ListView):
    model = Dog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(breed_id=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        breed_item = Breed.objects.get(pk=self.kwargs.get('pk'))
        context_data['object_list'] = (
            Dog.objects.filter(breed_id=breed_item, owner=self.request.user)
        )
        context_data['breed_pk'] = breed_item.pk
        context_data['title'] = f'Собаки породы - {breed_item.name}'

        return context_data


class DogCreateView(CreateView):
    model = Dog
    form_class = DogForm
    success_url = reverse_lazy('mainapp:breeds')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class DogUpdateView(UpdateView):
    model = Dog
    form_class = DogForm

    def get_success_url(self):
        return reverse('mainapp:breed_dogs', args=[self.object.breed.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        food_formset = inlineformset_factory(Dog, Food, form=FoodForm, extra=1)
        parent_formset = inlineformset_factory(Dog, Parent, form=ParentForm, extra=1)

        if self.request.method == 'POST':
            context_data['food_formset'] = food_formset(self.request.POST, instance=self.object)
            context_data['parent_formset'] = parent_formset(self.request.POST, instance=self.object)
        else:
            context_data['food_formset'] = food_formset(instance=self.object)
            context_data['parent_formset'] = parent_formset(instance=self.object)

        return context_data

    def form_valid(self, form):
        food_formset = self.get_context_data()['food_formset']
        parent_formset = self.get_context_data()['parent_formset']
        self.object = form.save()

        if food_formset.is_valid() and parent_formset.is_valid():
            food_formset.instance = self.object
            parent_formset.instance = self.object

            food_formset.save()
            parent_formset.save()

        return super().form_valid(form)


class DogDetailView(DetailView):
    model = Dog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        if settings.CACHE_ENABLED:
            key = f'food_list_{self.object.pk}'
            food_list = cache.get(key)
            if food_list is None:
                food_list = self.object.food_set.all()
                cache.set(key, food_list)
        else:
            food_list = self.object.food_set.all()

        context_data['foods'] = food_list
        return context_data


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('mainapp:breeds')
