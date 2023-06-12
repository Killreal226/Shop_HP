from django.db import models
from django.urls import reverse

class Product (models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, db_index=True,verbose_name='URL')
    description = models.TextField (verbose_name='Описание')
    photo = models.ImageField (upload_to='photos/', verbose_name='Фото')
    time_create = models.DateTimeField (auto_now_add=True)
    time_update = models.DateTimeField (auto_now=True)
    price = models.DecimalField (max_digits=7, decimal_places=2, verbose_name='Цена')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug}) 

    class Meta:
        verbose_name='Товары'
        verbose_name_plural = 'Товары'
        ordering = ['time_create']

class Category (models.Model):
    name = models.CharField (max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, db_index=True,verbose_name='URL')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug })
            
    class Meta:
        verbose_name='Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id'] 
 
class Data_message (models.Model):
    email = models.CharField (max_length=255, db_index=True, verbose_name='Ваш E-mail')
    message = models.TextField(verbose_name='Ваше сообщение:')

    class Meta:
        verbose_name='Обратная связь'
        ordering = ['email'] 
 
