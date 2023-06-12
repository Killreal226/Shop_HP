from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo','price', 'cat')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_filter = ('name', 'cat')
    prepopulated_fields ={'slug':('name',)}

class CategoryAdmin (admin.ModelAdmin): 
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields ={'slug':('name',)}

class Data_messageAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'message')
    list_display_links = ('id', 'email')



admin.site.register(Product, ProductAdmin) 
admin.site.register(Category,CategoryAdmin)
admin.site.register(Data_message, Data_messageAdmin)