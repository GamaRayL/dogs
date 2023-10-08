from django.urls import path
from django.views.decorators.cache import cache_page

from mainapp.views import IndexView, BreedListView, DogListView, DogCreateView, DogUpdateView, DogDeleteView, \
    DogDetailView
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', cache_page(60)(IndexView.as_view()), name='popular_list'),
    path('breeds/', BreedListView.as_view(), name='breeds'),
    path('<int:pk>/dogs/', DogListView.as_view(), name='breed_dogs'),
    path('view/<int:pk>/', DogDetailView.as_view(), name='view_dog'),
    path('dogs/create', DogCreateView.as_view(), name='dog_create'),
    path('dogs/update/<int:pk>/', DogUpdateView.as_view(), name='dog_update'),
    path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
]
