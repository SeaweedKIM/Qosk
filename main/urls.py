from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'kiosk'

urlpatterns = [
    path('', views.Main, name='main'),
    path('place/', views.Place, name='place'),
    path('face/', views.Face, name='face'),
    path('face/load/', views.Load, name='load'),
    # path('menu/', views.Menu, name='menu'),

    path('menu1/', views.Menu1, name='menu1'),
    path('menu2/', views.Menu2, name='menu2'),
    path('menu3/', views.Menu3, name='menu3'),
    path('menu4/', views.Menu4, name='menu4'),
    path('menu/order/', views.Order, name='order'),
    path('kitchen/', views.Kitchen, name='kitchen'),
    path('favor/', views.Favorlist, name='favor'),

    path('menu1/<int:food_id>/', views.add_cart1, name = 'add_cart1'),
    path('menu2/<int:food_id>/', views.add_cart2, name = 'add_cart2'),
    path('menu3/<int:food_id>/', views.add_cart3, name = 'add_cart3'),
    path('menu4/<int:food_id>/', views.add_cart4, name = 'add_cart4'),

    path('menulist/', views.MenuList, name='menulist'),
    path('menulist/<int:food_id>/', views.food_detail, name='food_detail'),
    path('menulist/add_menulist/', views.add_menulist, name='add_menulist'),
    path('menulist/modify/<int:food_id>/', views.food_modify, name='food_modify'),
    path('menulist/delete/<int:food_id>/', views.food_delete, name='food_delete'),

    path('test/', views.test, name='test'),
    
    # path('add/<int:food_id>/', views.add_cart, name='add_cart'),
    # path('cart/', views.cart_detail, name = 'cart_detail'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)