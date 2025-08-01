"""todolist URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from calendars import views

urlpatterns = [
    url(r'^$',auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/', views.home , name='home'),
    url(r'^todos/', include('todos.urls')),
    url(r'^calendars/',include('calendars.urls')),
    url(r'^admin/', admin.site.urls),
]
