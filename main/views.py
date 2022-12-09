# from django.views.generic.base import TemplateView
#
# class Main(TemplateView):
#     template_name = 'main.html'

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import List
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import Menuform
from django.http import HttpResponse

from django.http import HttpResponseRedirect

def Main(request):
    return render(request, 'main.html')


def Place(request):
    return render(request, 'place.html')


def Face(request):
    return render(request, 'face.html')


def Load(request):
    return render(request, 'load.html')


# Menu 관련 View--------------------------------------------------------

def Menu1(request, total=0, counter=0, cart_items = None):
    q = List.objects.values_list('category', flat=True).distinct()
    # coffee_category = List.objects.filter(category='커피')

    # below is coded by Young Kim
    page= request.GET.get('page', '1')  # 페이지
    age_and_gender = request.GET.get('age_and_gender', '1')

    if age_and_gender == '1':
        # male 20
        preference= List.objects.filter(category='커피').order_by( '-M20', 'food_name')
        print = '20대 남성'
    elif age_and_gender == '2':
        preference= List.objects.filter(category='커피').order_by( '-M30', 'food_name')
        print= "30대 남성"
    elif age_and_gender == '3':
        # male 40
        preference= List.objects.filter(category='커피').order_by( '-M40', 'food_name')
        print= "40대 남성"
    elif age_and_gender == '4':
        # male 50
        preference= List.objects.filter(category='커피').order_by( '-M50', 'food_name')
        print= "50대 남성"
    elif age_and_gender == '5':
        # male 60
        preference= List.objects.filter(category='커피').order_by( '-M60', 'food_name')
        print= "60대 남성"
    elif age_and_gender == '6':
        # male 70
        preference= List.objects.filter(category='커피').order_by( '-M70', 'food_name')
        print= "70대 남성"
    elif age_and_gender == '8':
        # female 20
        preference= List.objects.filter(category='커피').order_by( '-W20', 'food_name')
        print= "20대 여성"
    elif age_and_gender == '9':
        # female 30
        preference= List.objects.filter(category='커피').order_by( '-W30', 'food_name')
        print= "30대 여성"
    elif age_and_gender == '10':
        # female 40
        preference= List.objects.filter(category='커피').order_by( '-W40', 'food_name')
        print= "40대 여성"
    elif age_and_gender == '11':
        # female 50
        preference= List.objects.filter(category='커피').order_by( '-W50', 'food_name')
        print= "50대 여성"
    elif age_and_gender == '12':
        # female 60
        preference= List.objects.filter(category='커피').order_by( '-W60', 'food_name')
        print= "60대 여성"
    elif age_and_gender == '13':
        # female 70
        preference= List.objects.filter(category='커피').order_by( '-W70', 'food_name')
        print= "70대 여성"


    coffee_category = preference


    # above is coded by Young Kim

    coffee_paginator = Paginator(coffee_category, 6)  # 페이지당 n개씩 보여주기
    coffee_page_obj = coffee_paginator.get_page(page)
    cart_items = CartItem.objects.filter(active=True)
    for cart_item in cart_items:
        total += (cart_item.food.price * cart_item.quantity)
        counter += cart_item.quantity
    context = {
        'coffee_category':coffee_page_obj,
        'q':q,
        'cart_items': cart_items,
        'total':total,
        'counter':counter,
        'page':page,
        'print':print
        }
    return render(request, 'menu1.html', context)


def Menu2(request, total=0, counter=0, cart_items = None):
    q = List.objects.values_list('category', flat=True).distinct()

        # below is coded by Young Kim
    page= request.GET.get('page', '1')  # 페이지
    age_and_gender = request.GET.get('age_and_gender', '1')

    if age_and_gender == '1':
        # male 20
        preference= List.objects.filter(category='차').order_by( '-M20', 'food_name')
        print= "20대 남성"
    elif age_and_gender == '2':
        # male 30
        preference= List.objects.filter(category='차').order_by( '-M30', 'food_name')
        print= "30대 남성"
    elif age_and_gender == '3':
        # male 40
        preference= List.objects.filter(category='차').order_by( '-M40', 'food_name')
        print= "40대 남성"
    elif age_and_gender == '4':
        # male 50
        preference= List.objects.filter(category='차').order_by( '-M50', 'food_name')
        print= "50대 남성"
    elif age_and_gender == '5':
        # male 60
        preference= List.objects.filter(category='차').order_by( '-M60', 'food_name')
        print= "60대 남성"
    elif age_and_gender == '6':
        # male 70
        preference= List.objects.filter(category='차').order_by( '-M70', 'food_name')
        print= "70대 남성"
    elif age_and_gender == '8':
        # female 20
        preference= List.objects.filter(category='차').order_by( '-W20', 'food_name')
        print= "20대 여성"
    elif age_and_gender == '9':
        # female 30
        preference= List.objects.filter(category='차').order_by( '-W30', 'food_name')
        print= "30대 여성"
    elif age_and_gender == '10':
        # female 40
        preference= List.objects.filter(category='차').order_by( '-W40', 'food_name')
        print= "40대 여성"
    elif age_and_gender == '11':
        # female 50
        preference= List.objects.filter(category='차').order_by( '-W50', 'food_name')
        print= "50대 여성"
    elif age_and_gender == '12':
        # female 60
        preference= List.objects.filter(category='차').order_by( '-W60', 'food_name')
        print= "60대 여성"
    elif age_and_gender == '13':
        # female 70
        preference= List.objects.filter(category='차').order_by( '-W70', 'food_name')
        print= "70대 여성"

    tea_category = preference


    # above is coded by Young Kim
    

    tea_paginator = Paginator(tea_category, 6)  # 페이지당 n개씩 보여주기
    tea_page_obj = tea_paginator.get_page(page)

    cart_items = CartItem.objects.filter(active=True)
    for cart_item in cart_items:
        total += (cart_item.food.price * cart_item.quantity)
        counter += cart_item.quantity

    context = {
        'tea_category':tea_page_obj,
        'q':q,
        'cart_items': cart_items,
        'total':total,
        'counter':counter,
        'page':page,
        'print':print
        }
    return render(request, 'menu2.html', context)


def Menu3(request, total=0, counter=0, cart_items = None):
    q = List.objects.values_list('category', flat=True).distinct()

        # below is coded by Young Kim
    page= request.GET.get('page', '1')  # 페이지
    age_and_gender = request.GET.get('age_and_gender', '1')
    
    if age_and_gender == '1':
        # male 20
        preference= List.objects.filter(category='음료').order_by( '-M20', 'food_name')
        print= "20대 남성"
    elif age_and_gender == '2':
        # male 30
        preference= List.objects.filter(category='음료').order_by( '-M30', 'food_name')
        print= "30대 남성"
    elif age_and_gender == '3':
        # male 40
        preference= List.objects.filter(category='음료').order_by( '-M40', 'food_name')
        print= "40대 남성"
    elif age_and_gender == '4':
        # male 50
        preference= List.objects.filter(category='음료').order_by( '-M50', 'food_name')
        print= "50대 남성"
    elif age_and_gender == '5':
        # male 60
        preference= List.objects.filter(category='음료').order_by( '-M60', 'food_name')
        print= "60대 남성"
    elif age_and_gender == '6':
        # male 70
        preference= List.objects.filter(category='음료').order_by( '-M70', 'food_name') 
        print= "70대 남성"
    elif age_and_gender == '8':
        # female 20
        preference= List.objects.filter(category='음료').order_by( '-W20', 'food_name')
        print= "20대 여성"
    elif age_and_gender == '9':
        # female 30
        preference= List.objects.filter(category='음료').order_by( '-W30', 'food_name')
        print= "30대 여성"
    elif age_and_gender == '10':
        # female 40
        preference= List.objects.filter(category='음료').order_by( '-W40', 'food_name')
        print= "40대 여성"
    elif age_and_gender == '11':
        # female 50
        preference= List.objects.filter(category='음료').order_by( '-W50', 'food_name')
        print= "50대 여성"
    elif age_and_gender == '12':
        # female 60
        preference= List.objects.filter(category='음료').order_by( '-W60', 'food_name')
        print= "60대 여성"
    elif age_and_gender == '13':
        # female 70
        preference= List.objects.filter(category='음료').order_by( '-W70', 'food_name')
        print= "70대 여성"

    beverage_category = preference


    # above is coded by Young Kim

    beverage_paginator = Paginator(beverage_category, 6)  # 페이지당 n개씩 보여주기
    beverage_page_obj = beverage_paginator.get_page(page)

    cart_items = CartItem.objects.filter(active=True)
    for cart_item in cart_items:
        total += (cart_item.food.price * cart_item.quantity)
        counter += cart_item.quantity

    context = {
        'beverage_category':beverage_page_obj,
        'q':q,
        'cart_items': cart_items,
        'total':total,
        'counter':counter,
        'page':page,
        'print':print
        }
    return render(request, 'menu3.html', context)


def Menu4(request, total=0, counter=0, cart_items = None):
    q = List.objects.values_list('category', flat=True).distinct()

    # below is coded by Young Kim
    page= request.GET.get('page', '1')  # 페이지
    age_and_gender = request.GET.get('age_and_gender', '1')

    if age_and_gender == '1':
        # male 20
        preference= List.objects.filter(category='디저트').order_by( '-M20', 'food_name')
        print= "20대 남성"
    elif age_and_gender == '2':
        # male 30
        preference= List.objects.filter(category='디저트').order_by( '-M30', 'food_name')
        print= "30대 남성"
    elif age_and_gender == '3':
        # male 40
        preference= List.objects.filter(category='디저트').order_by( '-M40', 'food_name')
        print= "40대 남성"
    elif age_and_gender == '4':
        # male 50
        preference= List.objects.filter(category='디저트').order_by( '-M50', 'food_name')
        print= "50대 남성"
    elif age_and_gender == '5':
        # male 60
        preference= List.objects.filter(category='디저트').order_by( '-M60', 'food_name')
        print= "60대 남성"
    elif age_and_gender == '6':
        # male 70
        preference= List.objects.filter(category='디저트').order_by( '-M70', 'food_name')
        print= "70대 남성"
    elif age_and_gender == '8':
        # female 20
        preference= List.objects.filter(category='디저트').order_by( '-W20', 'food_name')
        print= "20대 여성"
    elif age_and_gender == '9':
        # female 30
        preference= List.objects.filter(category='디저트').order_by( '-W30', 'food_name')
        print= "30대 여성"
    elif age_and_gender == '10':
        # female 40
        preference= List.objects.filter(category='디저트').order_by( '-W40', 'food_name')
        print= "40대 여성"
    elif age_and_gender == '11':
        # female 50
        preference= List.objects.filter(category='디저트').order_by( '-W50', 'food_name')
        print= "50대 여성"
    elif age_and_gender == '12':
        # female 60
        preference= List.objects.filter(category='디저트').order_by( '-W60', 'food_name')
        print= "60대 여성"
    elif age_and_gender == '13':
        # female 70
        preference= List.objects.filter(category='디저트').order_by( '-W70', 'food_name')
        print= "70대 여성"

    dessert_category = preference


    # above is coded by Young Kim

    dessert_paginator = Paginator(dessert_category, 6)  # 페이지당 n개씩 보여주기
    dessert_page_obj = dessert_paginator.get_page(page)

    cart_items = CartItem.objects.filter(active=True)
    for cart_item in cart_items:
        total += (cart_item.food.price * cart_item.quantity)
        counter += cart_item.quantity

    context = {
        'dessert_category':dessert_page_obj,
        'q':q,
        'cart_items': cart_items,
        'total':total,
        'counter':counter,
        'page':page,
        'print':print
        }
    return render(request, 'menu4.html', context)


# def Menu(request):
#     page = request.GET.get('page', '1')  # 페이지
#     food_list = List.objects.order_by('food_num')
#     # products = List.objects.filter(category='커피')
#     paginator = Paginator(food_list, 6)  # 페이지당 n개씩 보여주기
#     page_obj = paginator.get_page(page)
#     context = {'food_list':page_obj}
#     return render(request, 'menu.html', context)

# def Menu(request):
#     q = List.objects.values_list('category', flat=True).distinct()

#     page = request.GET.get('page', '1')  # 페이지

#     coffee_category = List.objects.filter(category='커피')
#     coffee_paginator = Paginator(coffee_category, 6)  # 페이지당 n개씩 보여주기
#     coffee_page_obj = coffee_paginator.get_page(page)

#     tea_category = List.objects.filter(category='차')
#     tea_paginator = Paginator(tea_category, 6)  # 페이지당 n개씩 보여주기
#     tea_page_obj = tea_paginator.get_page(page)

#     beverage_category = List.objects.filter(category='음료')
#     beverage_paginator = Paginator(beverage_category, 6)  # 페이지당 n개씩 보여주기
#     beverage_page_obj = beverage_paginator.get_page(page)

#     dessert_category = List.objects.filter(category='디저트')
#     dessert_paginator = Paginator(dessert_category, 6)  # 페이지당 n개씩 보여주기
#     dessert_page_obj = dessert_paginator.get_page(page)

#     # food_list = List.objects.order_by('food_num')
#     # paginator = Paginator(food_list, 6)  # 페이지당 n개씩 보여주기
#     # page_obj = paginator.get_page(page)

#     context = {
#         'coffee_category':coffee_page_obj,
#         'tea_category':tea_page_obj,
#         'beverage_category':beverage_page_obj,
#         'dessert_category':dessert_page_obj,
#         'q':q,
#         # 'food_list':page_obj
#         }
#     return render(request, 'menu.html', context)


# ----------------------------------------------------------


def Order(request, total=0, counter=0):
    cart_items = CartItem.objects.filter(active=True)
    for cart_item in cart_items:
        total += (cart_item.food.price * cart_item.quantity)
        counter += cart_item.quantity

    context = {
        'cart_items': cart_items,
        'total':total,
        'counter':counter,
        }
    return render(request, 'order.html', context)


def Kitchen(request):
    return render(request, 'kitchen.html')


def Favorlist(request):
    return render(request, 'favor.html')




# MenuList 관련 View ------------------------------




def MenuList(request):
    page = request.GET.get('page', '1')  # 페이지
    food_list = List.objects.order_by('food_num')
    paginator = Paginator(food_list, 13)  # 페이지당 n개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'food_list':page_obj}
    return render(request, 'menulist.html', context)


def food_detail(request, food_id):
    food = get_object_or_404(List, pk=food_id)
    context = {'food': food}
    return render(request, 'food_detail.html', context)


def food_modify(request, food_id):
    food = get_object_or_404(List, pk=food_id)
    if request.method == "POST":
        form = Menuform(request.POST, request.FILES, instance=food)
        if form.is_valid():
            # food.food_name = form.cleaned_data['food_name']
            # food.price = form.cleaned_data['price']
            # food.food_explain = form.cleaned_data['food_explain']
            # food.category = form.cleaned_data['category']
            # food.image = form.cleaned_data['image']
            food = form.save(commit=False)
            # food.modify_date = timezone.now()  # 수정일시 저장
            food.save()
            return redirect('kiosk:food_detail', food_id=food.food_num)
    else:
        form = Menuform(instance=food)
    context = {'form': form}
    return render(request, 'menu_form.html', context)


def food_delete(request, food_id):
    food = get_object_or_404(List, pk=food_id)
    food.delete()
    return redirect('kiosk:menulist')

def add_menulist(request):
    if request.method == 'POST':
        form = Menuform(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            return redirect('kiosk:menulist')
    else:
        form = Menuform()
    context = {'form': form}
    return render(request, 'menu_form.html', context)






# 테스트용 ----------------------------

def test(request, total=0, counter=0, cart_items = None):
    q = List.objects.values_list('category', flat=True).distinct()
    # coffee_category = List.objects.filter(category='커피')


    # below is coded by Young Kim
    page= request.GET.get('page', '1')  # 페이지
    age_and_gender = request.GET.get('age_and_gender', '1')

    if age_and_gender == '1':
        # male 20
        preference= List.objects.filter(category='커피').order_by( '-M20', 'food_name')
    elif age_and_gender == '2':
        preference= List.objects.filter(category='커피').order_by( '-M30', 'food_name')

    coffee_category = preference

    coffee_paginator = Paginator(coffee_category, 6)  # 페이지당 n개씩 보여주기
    coffee_page_obj = coffee_paginator.get_page(page)
    cart_items = CartItem.objects.filter(active=True)
    for cart_item in cart_items:
        total += (cart_item.food.price * cart_item.quantity)
        counter += cart_item.quantity
    context = {
        'coffee_category':coffee_page_obj,
        'q':q,
        'cart_items': cart_items,
        'total':total,
        'counter':counter,
        'page':page
        }
    return render(request, 'test.html', context)

    # q_category = List.objects.filter(category=)
    # context = q_dict
    # filter = List.objects.filter(category=q)
    # return render(request, 'test.html', q_dict)
    # return HttpResponse(q_dict)


# def food_detail(request, food_id):
#     food = get_object_or_404(List, pk=food_id)
#     context = {'food': food}
#     return render(request, 'food_detail.html', context)




# Cart View ---------------------------------


from .models import CartItem
from django.core.exceptions import ObjectDoesNotExist


# 추가, 수량, 가격 조회 기능 ---------------


def add_cart(request, food_id):
    food = get_object_or_404(List, pk=food_id)
    try:
        cart_item = CartItem.objects.get(food = food)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:   # 기본 값
        cart_item = CartItem.objects.create(
            food = food,
            quantity = 1,
        )
        cart_item.save()

    # cart_items = CartItem.objects.filter(active=True)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def Cart(request, total=0, counter=0, cart_items = None):
#     cart_items = CartItem.objects.filter(active=True)
#     for cart_item in cart_items:
#         total += (cart_item.food.price * cart_item.quantity)
#         counter += cart_item.quantity

#     content = {
#         'cart_items': cart_items,
#         'total':total,
#         'counter':counter
#     }

#     return render(request, 'menu1.html', content)




# def _cart_id(request):    # 주문 기능을 이용하는 고객에게 부여할 식별코드 생성 함수
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart

# def add_cart (request, food_id):
#     food = List.objects.get(id = food_id)
#     try:  # 특정 고객을 인식하는 용도(필요없음)
#         cart = Cart.objects.get(cart_id = _cart_id(request))
#     except Cart.DoesNotExist:
#         cart = Cart.objects.create(
#             cart_id = _cart_id(request)
#         )
#         cart.save()

#     try:
#         cart_item = CartItem.objects.get(food = food, cart = cart)
#         cart_item.quantity += 1
#         cart_item.save()
#     except CartItem.DoesNotExist:
#         cart_item = CartItem.objects.create(
#             food = food,
#             quantity = 1,
#             cart = cart
#         )
#         cart_item.save()
#     return redirect('kiosk:cart_detail')


# def cart_detail(request, total=0, counter=0, cart_items=None):
#     try:
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_items = CartItem.objects.filter(cart=cart, active=True)
#         for cart_item in cart_items:
#             total += (cart_item.food.price * cart_item.quantity)
#             counter += cart_item.quantity
#     except ObjectDoesNotExist:
#         pass

#     return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))



# 제거 기능 -------------------


def remove_cart(request, food_id):
    food = get_object_or_404(List, pk=food_id)
    cart_item = CartItem.objects.get(food = food)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# 전체 삭제 기능 -----------------



def clear(request):
    cart_item = CartItem.objects.all()
    cart_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def home(request):
    cart_item = CartItem.objects.all()
    cart_item.delete()
    return redirect('kiosk:menu1')