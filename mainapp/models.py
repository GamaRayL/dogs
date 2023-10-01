from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Breed(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(max_length=255, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'
        ordering = ('name',)


class Dog(models.Model):
    nickname = models.CharField(max_length=50, verbose_name='кличка')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, **NULLABLE)
    photo = models.ImageField(upload_to='photos/', verbose_name='фотография', **NULLABLE)
    birth_date = models.DateField(verbose_name='дата рождения', **NULLABLE)
    email = models.CharField(max_length=150, unique=True, verbose_name='почта', **NULLABLE)

    def __str__(self):
        return f'{self.nickname} {self.breed} {self.birth_date}'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
        ordering = ('nickname',)


class Food(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, verbose_name='собака')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'корм'
        verbose_name_plural = 'корма'


class Parent(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, verbose_name='собака')
    nickname = models.CharField(max_length=150, verbose_name='кличка')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='порода')
    birth_date = models.DateField(verbose_name='дата рождения', **NULLABLE)
