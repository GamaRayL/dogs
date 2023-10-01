from django.contrib import admin

from mainapp.models import Dog, Breed, Food


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'breed',)
    list_filter = ('breed',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'dog',)
    list_filter = ('dog',)
