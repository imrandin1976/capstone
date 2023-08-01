from django.contrib import admin
from django.urls import path
from . import views
from .views import index, menuView, bookingView, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token


# Url Routes
urlpatterns = [
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>/', SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
    

]