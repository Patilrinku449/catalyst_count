"""catalyst_count URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from catalyst import views
# from .views import UserCreateView, UserUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    # path('/', include('catalyst.urls')),
    path('admin_users/', views.admin_users, name='admin_users'),
    path('fileUploader/', views.index, name='fileUploader'),
    path('datatable/', views.datatable, name='datatable'),
    # path('user/new/', UserCreateView.as_view(), name='user-new'),
    # path('user/<int:pk>/edit/', UserUpdateView.as_view(), name='user-edit'),
    # path('dataTable/<str:file>', views.datatable, name='datatable'),
    # path('', views.index , name='login'),
    # path('register', views.register, name='register' ),
    # path('custom',views.custom , name= 'custom'),
    # path('home',views.home , name= 'home'),
]
