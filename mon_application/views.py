from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2> Ary tô miandry rafraichissement eee !!!</h2>")
