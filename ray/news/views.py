from django.shortcuts import render
from .models import Articles

# Create your views here.
def newsIndex(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/newsIndex.html', {'news': news})