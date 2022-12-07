from django import forms
from .models import List

# class Menuform(forms.Form):
#     title = forms.CharField()
#     body = forms.CharField(widget=forms.Textarea)

# class Menuform(forms.Form):
#     food_name = forms.CharField(max_length=200)
#     price = forms.IntegerField()
#     food_explain = forms.CharField(max_length=1000, required=False)
#     category = forms.CharField(max_length=250)
#     image = forms.ImageField(required=False)

from django.views import View

# class Menuform(View):
#    def post(self, request):
#         food_name = request.POST['food_name']
#         price = request.POST['price']
#         food_explain = request.POST['food_explain']
#         category = request.POST['category']
#         image = request.FILES.__getitem__('image')


class Menuform(forms.ModelForm):
    class Meta:
        model = List  # 사용할 모델
        fields = ['food_name', 'price', 'food_explain', 'category', 'image']

#------------------------------------------
