"""culling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home import views as home_views
from lists import views as list_views
#from lists.views import ListDetailView
from django.contrib.auth import views as auth_views
from auth_user import views as create_user_views
from quiz.views import QuizListView, QuestionListView, QuizCreateView, QuestionCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',  auth_views.LoginView.as_view(template_name='auth_users/login.html'), name='login'),
    url(r'^logout',  auth_views.LogoutView.as_view(template_name='auth_users/logout.html'), name='logout'),
    url(r'^home', home_views.dashboard, name='home'),
    url(r'^user-list', list_views.user_lists, name='lists'),
    url(r'^list/(?P<pk>\d+)/', list_views.list_items, name='list_details'),
    url(r'^create-user', create_user_views.create_user, name='create-user'),
    url(r'^view-quiz', QuizListView.as_view(), name='view-quiz'),
    url(r'^create-quiz', QuizCreateView.as_view(), name='create-quiz'),
    url(r'^create-question/(?P<pk>\d+)/', QuestionCreateView.as_view(), name='create-question'),
]
