"""
URL configuration for stackoverflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stackoverflow import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.questionList),
    path('ask/', views.ask),
    path('question123/', views.question123),
    path('tag/', views.tag),
    path('settings/', views.settings), # во 2 не нужно
    path('login/', views.login),
    path('signup/', views.register)
     #нужна страница hot/
]

# cписок новых вопросов (главная страница) (URL = /)
# cписок “лучших” вопросов (URL = /hot/)
# cписок вопросов по тэгу (URL = /tag/blablabla/)
# cтраница одного вопроса со списком ответов (URL = /question/35/)
# форма логина (URL = /login/)
# форма регистрации (URL = /signup/)
# форма создания вопроса (URL = /ask/)