from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.forms import PostForm

# Create your views here.
def index(request):
    # site_0\lotto\templates\lotto\default.html
    lottos = GuessNumbers.objects.all()
    sample_str = 'python variable'
    return render(request, "lotto/default.html", {'lottos': lottos})


def hello(request):
    return HttpResponse("<h1 style='color:red;'> Welcome J1</h1>")


def post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            # return render(request, 'lotto/default.html', {})
            return redirect('index')

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form': form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto': lotto})
