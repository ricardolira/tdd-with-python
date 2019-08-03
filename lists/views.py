from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return_dict = {'new_item_text': request.POST.get('item_text',''),}
    return render(request, 'home.html', return_dict)
