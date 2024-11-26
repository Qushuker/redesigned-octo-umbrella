from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')
def post(request):
    return render(request, 'main/post.html')