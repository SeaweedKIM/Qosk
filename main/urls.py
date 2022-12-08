from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'kiosk'

urlpatterns = [

    # 존재하지만 안 쓰는 페이지들 ~~
    # path('', views.Main, name='main'),
    path('place/', views.Place, name='place'),
    path('face/', views.Face, name='face'),
    path('face/load/', views.Load, name='load'),

    # path('menu/', views.Menu, name='menu'),

    path('', views.Menu1, name='menu1'),
    path('menu2/', views.Menu2, name='menu2'),
    path('menu3/', views.Menu3, name='menu3'),
    path('menu4/', views.Menu4, name='menu4'),
    path('order/', views.Order, name='order'),
    path('kitchen/', views.Kitchen, name='kitchen'),
    path('favor/', views.Favorlist, name='favor'),

    path('menu/add/<int:food_id>/', views.add_cart, name = 'add_cart'),
    path('menu/rm/<int:food_id>/', views.remove_cart, name = 'remove_cart'),
    path('menu/clear/', views.clear, name = 'clear_cart'),
    path('menu/home/', views.home, name = 'home'),

    path('menulist/', views.MenuList, name='menulist'),
    path('menulist/<int:food_id>/', views.food_detail, name='food_detail'),
    path('menulist/add_menulist/', views.add_menulist, name='add_menulist'),
    path('menulist/modify/<int:food_id>/', views.food_modify, name='food_modify'),
    path('menulist/delete/<int:food_id>/', views.food_delete, name='food_delete'),

    path('test/', views.test, name='test'),
    
    # path('add/<int:food_id>/', views.add_cart, name='add_cart'),
    # path('cart/', views.cart_detail, name = 'cart_detail'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)