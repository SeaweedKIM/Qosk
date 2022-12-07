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
    #coffee_category = List.objects.filter(category='커피')
    coffee_category = (list(List.objects.filter(category='커피')))


    # below is coded by Young Kim
    page= request.GET.get('page', '1')  # 페이지
    age_and_gender = request.GET.get('age_and_gender', '1')
    preference = []
    if age_and_gender == '1':
        # male 20
        preference=[9,0,1,8,6,7,4,5,2,3]
    elif age_and_gender == '2':
        # male 30
        preference=[9,0,1,8,5,6,3,8,2,5]
    elif age_and_gender == '3':
        # male 40
        preference=[9,0,1,2,8,4,7,5,4,6]
    elif age_and_gender == '4':
        # male 50
        preference=[x - 1 for x in [10,1,2,3,8,7,5,4,9,6]]
    elif age_and_gender == '5':
        # male 60
        preference=[x - 1 for x in [10,1,2,3,8,6,5,4,9,7]]
    elif age_and_gender == '6':
        # male 70
        preference=[x - 1 for x in [10,1,2,4,9,5,7,3,8,6]] 
    elif age_and_gender == '8':
        # female 20
        preference=[x - 1 for x in [10,1,2,4,9,5,7,3,8,6]]
    elif age_and_gender == '9':
        # female 30
        preference=[9,0,1,6,2,3,7,8,4,5]
    elif age_and_gender == '10':
        # female 40
        preference=[9,0,1,5,6,3,4,2,7,8]
    elif age_and_gender == '11':
        # female 50
        preference=[9,0,1,2,6,3,7,4,8,5]
    elif age_and_gender == '12':
        # female 60
        preference=[9,0,1,3,5,4,7,2,8,6]
    elif age_and_gender == '13':
        # female 70
        preference=[9,0,1,2,5,4,6,3,8,7]
    coffee_category = [coffee_category[i] for i in preference]


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
        'page':page
        }
    return render(request, 'menu1.html', context)


def Menu2(request, total=0, counter=0, cart_items = None):
    q = List.objects.values_list('category', flat=True).distinct()

    tea_category = List.objects.filter(category='차')

        # below is coded by Young Kim
    page= request.GET.get('page', '1')  # 페이지
    age_and_gender = request.GET.get('age_and_gender', '1')
    preference = []
    if age_and_gender == '1':
        # male 20
        preference=[2,3,7,4,0,5,1,6,8]
    elif age_and_gender == '2':
        # male 30
        preference=[1,4,5,7,0,3,2,8,6]
    elif age_and_gender == '3':
        # male 40
        preference=[0,1,5,6,8,4,2,7,3]
    elif age_and_gender == '4':
        # male 50
        preference=[3,2,1,6,8,5,4,7,0]
    elif age_and_gender == '5':
        # male 60
        preference=[3,4,5,7,8,2,1,6,0]
    elif age_and_gender == '6':
        # male 70
        preference=[1,2,3,7,8,5,4,6,0] 
    elif age_and_gender == '8':
        # female 20
        preference=[5,4,8,3,2,0,1,7,6]
    elif age_and_gender == '9':
        # female 30
        preference=[2,4,8,3,5,0,1,7,6]
    elif age_and_gender == '10':
        # female 40
        preference=[0,1,6,5,8,4,2,7,3]
    elif age_and_gender == '11':
        # female 50
        preference=[2,4,6,5,8,3,1,7,0]
    elif age_and_gender == '12':
        # female 60
        preference=[1,3,6,2,8,5,4,7,0]
    elif age_and_gender == '13':
        # female 70
        preference=[2,4,6,5,8,3,1,7,0]

    tea_category = [tea_category[i] for i in preference]


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
        'page':page
        }
    return render(request, 'menu2.html', context)


def Menu3(request, total=0, counter=0, cart_items = None):
    q = List.objects.values_list('category', flat=True).distinct()

    beverage_category = List.objects.filter(category='음료')

        # below is coded by Young Kim
    page= request.GET.get('page', '1')  # 페이지
    age_and_gender = request.GET.get('age_and_gender', '1')
    preference = []
    if age_and_gender == '1':
        # male 20
        preference=[8,12,9,15,5,3,0,2,1,6,4,14,10,16,13,11,7]
    elif age_and_gender == '2':
        # male 30
        preference=[6,11,8,16,7,3,0,1,2,5,4,13,9,15,14,12,10]
    elif age_and_gender == '3':
        # male 40
        preference=[1,12,7,11,8,5,4,2,3,0,6,15,10,9,13,14,16]
    elif age_and_gender == '4':
        # male 50
        preference=[1,11,10,14,8,6,2,7,5,0,3,9,4,12,13,15,16]
    elif age_and_gender == '5':
        # male 60
        preference=[0,8,7,11,13,12,9,10,14,1,2,3,5,4,6,16,15]
    elif age_and_gender == '6':
        # male 70
        preference=[0,8,7,12,13,11,10,9,14,1,3,2,5,6,4,15,16] 
    elif age_and_gender == '8':
        # female 20
        preference=[4,8,9,16,7,3,1,2,0,6,5,14,13,10,11,15,12]
    elif age_and_gender == '9':
        # female 30
        preference=[2,12,11,13,7,4,0,3,1,6,5,14,9,8,10,16,15]
    elif age_and_gender == '10':
        # female 40
        preference=[0,13,12,15,10,9,5,1,4,3,2,11,8,6,7,16,14]
    elif age_and_gender == '11':
        # female 50
        preference=[0,14,12,13,11,9,7,4,10,8,1,5,3,2,6,16,15]
    elif age_and_gender == '12':
        # female 60
        preference=[0,8,7,14,11,9,10,12,13,3,2,4,5,1,6,15,16]
    elif age_and_gender == '13':
        # female 70
        preference=[0,8,7,10,14,13,9,15,12,2,3,1,5,4,6,16,11]

    beverage_category = [beverage_category[i] for i in preference]


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
        'page':page
        }
    return render(request, 'menu3.html', context)


def Menu4(request, total=0, counter=0, cart_items = None):
    q = List.objects.values_list('category', flat=True).distinct()
    dessert_category = List.objects.filter(category='디저트')

    # below is coded by Young Kim
    page= request.GET.get('page', '1')  # 페이지
    age_and_gender = request.GET.get('age_and_gender', '1')
    preference = []
    if age_and_gender == '1':
        # male 20
        preference=[9,7,6,5,8,3,0,2,1,4]
    elif age_and_gender == '2':
        # male 30
        preference=[9,8,7,6,4,2,0,3,1,5]
    elif age_and_gender == '3':
        # male 40
        preference=[8,6,5,7,4,0,2,1,3,9]
    elif age_and_gender == '4':
        # male 50
        preference=[7,8,5,6,3,0,2,1,4,9]
    elif age_and_gender == '5':
        # male 60
        preference=[6,7,3,8,5,0,4,1,2,9]
    elif age_and_gender == '6':
        # male 70
        preference=[3,8,6,2,0,7,1,4,5,9] 
    elif age_and_gender == '8':
        # female 20
        preference=[9,7,8,5,4,0,2,1,3,6]
    elif age_and_gender == '9':
        # female 30
        preference=[7,8,0,6,2,3,1,4,5,9]
    elif age_and_gender == '10':
        # female 40
        preference=[8,7,6,4,0,2,1,3,5,9]
    elif age_and_gender == '11':
        # female 50
        preference=[6,9,7,4,0,3,1,2,5,8]
    elif age_and_gender == '12':
        # female 60
        preference=[3,5,4,8,0,2,1,7,6,9]
    elif age_and_gender == '13':
        # female 70
        preference=[6,7,4,8,0,2,1,5,3,9,]

    dessert_category = [dessert_category[i] for i in preference]


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
        'page':page
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


def Order(request):
    return render(request, 'order.html')


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

def Category_test(request, word):
    food_category = List.objects.filter(category=word).values()
    # context = {'food_category':food_category}
    # return render(request, 'menu.html', context)
    return HttpResponse(food_category)
    # return HttpResponse(context)

def test(request):
    q = List.objects.values_list('category', flat=True).distinct()
    q_dict = {
        'q':q,
    }

    # q_category = List.objects.filter(category=)
    # context = q_dict
    # filter = List.objects.filter(category=q)
    # return render(request, 'test.html', q_dict)
    return HttpResponse(q_dict)


# def food_detail(request, food_id):
#     food = get_object_or_404(List, pk=food_id)
#     context = {'food': food}
#     return render(request, 'food_detail.html', context)




# Cart View ---------------------------------

from .models import CartItem
from django.core.exceptions import ObjectDoesNotExist




def add_cart1(request, food_id):
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
    
    return redirect('kiosk:menu1')
    # return render(request, 'menu1.html', {'cart_items':cart_items})


def add_cart2(request, food_id):
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
    
    return redirect('kiosk:menu2')

def add_cart3(request, food_id):
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
    
    return redirect('kiosk:menu3')

def add_cart4(request, food_id):
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
    
    return redirect('kiosk:menu4')


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
