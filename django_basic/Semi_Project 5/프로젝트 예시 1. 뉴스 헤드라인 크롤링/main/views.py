from django.shortcuts import render
from . import crawl_main

def crawl_keyword(request):
    return render(request, 'main/crawl_keyword.html', {})

def crawl_keyword_result(request):
    keyword_submitted = request.POST['input_keyword']
    print(keyword_submitted)

    crawl_result = crawl_main.naver_keyword(keyword_submitted)

    context = {'keyword': keyword_submitted, 'crawl_result': crawl_result}
    return render(request, 'main/crawl_keyword_result.html', context)
