from .views import *
from django.urls import path 

urlpatterns = [
    path('home/', Page_Home.as_view(), name='home'),
    path('all/', All_Product.as_view(), name='all'),
    path('about/', About.as_view(), name='about'),
    path('create rev/', create_rev, name='create_rev'),
    path('FeedBack/', FeedBack.as_view(), name='FeedBack'),
    path('Login/', LoginUser.as_view(), name='Login'),
    path('Logout/', logout_User, name='Logout'),
    path('registration/', Register_User.as_view(), name='registration'),
    path('post/<slug:post_slug>/', Show_Post.as_view(), name='post'),
    path('category/<slug:cat_slug>/', Show_Category.as_view(), name='category')
]