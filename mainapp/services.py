from django.conf import settings
from django.core.cache import cache

from mainapp.models import Food


def get_cached_foods_for_dogs(dog_pk):
    if settings.CACHE_ENABLED:
        key = f'food_list_{dog_pk}'
        food_list = cache.get(key)
        if food_list is None:
            food_list = Food.objects.filter(dog_id=dog_pk)
            cache.set(key, food_list)
    else:
        food_list = Food.objects.filter(dog_pk=dog_pk)

    return food_list
