from django.db import models


# Create your models here.
# class Customer(models.Model):
#     order_num = models.BigAutoField(primary_key=True)
#     date = models.DateTimeField(auto_now_add=True, null=False)
#     gender = models.CharField(max_length=50, blank=True)
#     age_group = models.CharField(max_length=255, blank=True)
#     total_num = models.IntegerField(default=0, null=False)
#     total_price = models.IntegerField(default=0, null=False)


class List(models.Model):
    food_num = models.BigAutoField(primary_key=True)
    food_name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(default=0, null=False)
    food_explain = models.TextField(max_length=2000, blank=True)
    category = models.CharField(max_length=250, null=False)
    image = models.ImageField(upload_to='static/menuimg/', blank=True)

    # modify_date = models.DateTimeField(null=True, blank=True)

    M20 = models.IntegerField(default=0, null=True)
    M30 = models.IntegerField(default=0, null=True)
    M40 = models.IntegerField(default=0, null=True)
    M50 = models.IntegerField(default=0, null=True)
    M60 = models.IntegerField(default=0, null=True)
    M70 = models.IntegerField(default=0, null=True)
    W20 = models.IntegerField(default=0, null=True)
    W30 = models.IntegerField(default=0, null=True)
    W40 = models.IntegerField(default=0, null=True)
    W50 = models.IntegerField(default=0, null=True)
    W60 = models.IntegerField(default=0, null=True)
    W70 = models.IntegerField(default=0, null=True)

    def __str__(self):
        return '{}'.format(self.food_name)

    # def get_photo_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url


# class Bill(models.Model):
#     order_num = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     menu_num = models.ForeignKey(List, on_delete=models.CASCADE)


# class Order(models.Model):
#     food_name = models.ForeignKey(List, on_delete=models.CASCADE)


#     def __str__(self):
#         return '{}'.format(self.food_name)


# Create your models here.



# class Food(models.Model):
#     food_name = models.CharField(max_length=200)
#     price = models.IntegerField(default=0)
#     category = models.CharField(max_length=250)


# class Customer(models.Model):
#     date = models.DateTimeField(auto_now_add=True)
#     gender_and_age = models.CharField(max_length=2, blank=True)
#     order = models.ForeignKey(Food, on_delete=models.CASCADE)

# YOLOv5
import os

from django.db import models
from django.utils.translation import gettext_lazy as _


# class ImageModel(models.Model):
#     image = models.ImageField(_("image"), upload_to='images')

#     class Meta:
#         verbose_name = "Image"
#         verbose_name_plural = "Images"

#     def __str__(self):
#         return str(os.path.split(self.image.path)[-1])





# 장바구니 ------------------
# class Cart(models.Model):   # 필요없는 듯
#     cart_id = models.CharField(max_length=250, blank=True)
#     date_added = models.DateField(auto_now_add=True)
#     class Meta:
#         db_table = 'Cart'   # db에서 보이는 테이블 이름
#         ordering = ['date_added']

#     def __str__(self):
#         return self.cart_id

class CartItem(models.Model):
    food = models.ForeignKey(List, on_delete=models.CASCADE)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()    # 상품 객체의 수량
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'CartItem'   # 테이블 이름

    def sub_total(self):
        return self.food.price * self.quantity  # 상품 객체의 총 가격

    def __str__(self):
        return self.food.food_name