from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .models import *
from .forms import *
from .utils import *


class All_Product (DataMixin,ListView):
    model = Product
    template_name = 'shop/all_product.html'
    context_object_name ='list_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context (title ='Все товары')
        return dict(list(context.items())+list(c_def.items()))

class Page_Home (DataMixin,TemplateView):
    template_name = 'shop/home.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context (title ='Главная страница')
        return dict(list(context.items())+list(c_def.items()))


# def page_home (request):
#     cats = Category.objects.all ()
#     context ={
#         'title':'Главная страница',
#         'cats':cats,
#         'dop_menu': dop_menu
#     }
#     return render(request, 'shop/home.html', context=context)

# def all_product (request):
#     product = Product.objects.all ()
#     cats = Category.objects.all ()
#     context ={
#         'title':'Все товары',
#         'cats':cats,
#         'dop_menu': dop_menu,
#         'list_product':product
#     }
#     return render(request, 'shop/all_product.html', context=context)

def pageNotFound (request, exception):
    return HttpResponseNotFound ('Страница не найдена!')

class About (DataMixin,TemplateView):
    template_name = 'shop/about.html'
    context_object_name = 'home'            #Тут

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context (title ='О сайте')
        return dict(list(context.items())+list(c_def.items()))

def create_rev (request):
    return HttpResponse ('<h1>Оставить отзыв о сайте</h1>')

class FeedBack (LoginRequiredMixin,DataMixin,CreateView):
    form_class = FeedBack_form
    template_name = 'shop/FeedBack.html'
    success_url = reverse_lazy ('home')
    #login_url = reverse_lazy ('home')
    login_url =  'Login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context (title ='Обратная связь')
        return dict(list(context.items())+list(c_def.items()))

# def FeedBack (request):
#     if request.method == 'POST':
#         form = FeedBack_form(request.POST)
#         if form.is_valid():
#             #print (form.cleaned_data)
#             form.save()
#             return redirect ('home')
#     else:
#         form = FeedBack_form ()

#     cats = Category.objects.all ()
#     context ={
#         'title':'Обратная связь',
#         'cats':cats,
#         'dop_menu': dop_menu,
#         'form':form
#     }
#     return render (request, 'shop/FeedBack.html', context=context)

class LoginUser (DataMixin, LoginView):
    form_class =  LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context (title = 'Вход')
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self) -> str:
        return reverse_lazy('home')

class Register_User(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy ('entrance')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context (title = 'Регистрация')
        return dict(list(context.items())+list(c_def.items()))


class Show_Post (DataMixin,DetailView):
    model = Product
    template_name = 'shop/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context (title = context['post'].name)
        return dict(list(context.items())+list(c_def.items()))


# def show_post (request, post_slug):
#     post = get_object_or_404 (Product, slug = post_slug)
#     cats = Category.objects.all ()

#     context = {
#         'title': post.name,
#         'dop_menu':dop_menu,
#         'cats': cats,
#         'post':post,
#     }
#     return render(request, 'shop/post.html', context=context)

class Show_Category(DataMixin,ListView):
    model = Product
    template_name = 'shop/all_product.html'
    context_object_name = 'list_product'
    allow_empty =False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context (title = str(context['list_product'][0].cat))
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter (cat__slug=self.kwargs['cat_slug'])


# def show_category (request, cat_slug):
#     cat = Category.objects.get (slug=cat_slug)
#     product = Product.objects.filter (cat_id=cat.id)
#     cats = Category.objects.all ()  
#     context ={
#         'title': cat.name,
#         'cats':cats,
#         'dop_menu': dop_menu,
#         'list_product':product
#     }
#     return render(request, 'shop/all_product.html', context=context)

def logout_User(request):
    logout(request)
    return redirect('Login')