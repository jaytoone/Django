from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'attends/index.html', {})

def result(request):
    print()
    print(request.POST)
    print(request.POST['name'])
    print()
    user_name = request.POST['name']

    return render(request, 'attends/result.html', {'name':user_name})
