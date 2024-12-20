from django.contrib import admin
from django.urls import path
from items import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items',views.items),
    path('nike',views.nike),
    path('glasses',views.glasses),
    path('denim',views.denim),
    path('fastrack',views.fastrack),
    path('iphone',views.iphone),
    path('trouser',views.trouser),
    path('poco',views.poco),
    path('kvs',views.kvs),
    path('screw',views.screw),
    path('formal',views.formal),
    path('denver',views.denver),
    path('submit',views.submit),
    path('login',views.login),
]
