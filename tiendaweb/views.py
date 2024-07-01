from django.shortcuts import render

def home(request):
    context={}
    return render(request, 'tiendaweb/index.html', context)


# Create your views here.
