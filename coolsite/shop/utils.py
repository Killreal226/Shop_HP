from .models import *

dop_menu =[{'title':'О сайте','url_name':'about'},
           {'title':'Оставить отзыв', 'url_name':'create_rev'}, 
           {'title':'Обратная связь', 'url_name':'FeedBack'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all ()

        #user_menu = dop_menu.copy()
        #if not self.request.user.is_authenticated:     #Если нужно, чтобы ссылка для не авторизованного пользователя просто пропадала
            #user_menu.pop(2)

        #context['dop_menu'] = user_menu

        context['dop_menu'] = dop_menu 
        context['cats'] = cats
        return context

