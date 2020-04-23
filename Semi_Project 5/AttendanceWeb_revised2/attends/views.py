from django.shortcuts import render
from django.http import HttpResponse
from .absent_check import absent_check
# Create your views here.
def index(request):
    return render(request, 'attends/index.html', {})

def result(request):
    print()
    print(request.POST)
    print(request.POST['name'])
    print()
    user_name = request.POST['name']
    user_data = absent_check(user_name)
    print(user_data)

    return render(request, 'attends/result.html', user_data)
