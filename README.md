# Shop_HP

Данный проект представляет собой сайт (в перспективе магазин) 
товаров по вселенной Гарри Поттера. Данный проект реализован на фреймворке Django и в своей работе использует базу данных SQLite. Доступна рабочая админка сайта, а также регистрация и авторизация пользователей.

## Установка 

1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение 
3. Установите зависимости 
`pip install -r requirements.txt`

## Настрока сайта

1. Чтобы запустить сайт перейдите в каталог __coolsite__
`cd coolsite`
2. Пропешите команду:
`python manage.py runserver`
3. В браузере перейдите по ссылке:
[http://127.0.0.1:8000/home](http://127.0.0.1:8000/home)
4. Для перехода на главную страницу можно нажать значок в левом верхнем углу

На сайте доступны Категории товаров, Данные о товарах. Регистрация пользователей, авторизация, обратная связь, а также главная страница и страница о сайте

## Админ-панель
Для регистрации админки проделайте следующие действия
1. перейдите в каталог __coolsite__ если не находитесь в нем
`cd coolsite`
2. Пропешите следующую команду:
`python manage.py createsuperuser`
3. Напишите имя пользователя, логин и паролью. Если все сделано правильно админ зарегистрирован. 
4. Для того, чтобы перейти в админку перейдите по ссылке:
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) и авторизуйтесь 

Через админ панель вам можно добавлять новые товары в базу данных, удалять старые, редактировать их, просматривать обратную связь.


