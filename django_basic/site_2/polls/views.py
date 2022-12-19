from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from polls.models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # return HttpResponse('wanna go home')

def detail(request, question_id):
    # try:
    #     q = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404('Question {} does not exist'.format(question_id))
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':q})
    # return HttpResponse('youre looking question {}.'.format(question_id))

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question':question})
    # response = 'youre looking the results of question {}.'
    # return HttpResponse(response.format(question_id))

def vote(request, question_id):
    print(request.POST)
    question = get_object_or_404(Question, pk=question_id)

    try:
        select_choice = question.choice_set.get(pk=request.POST['choice_select'])
    except:
        context = {'question':question, 'error_message': 'you need to select a choice'}
        return render(request, 'polls/detail.html', context)
    else:
        select_choice.votes += 1
        select_choice.save()

        return redirect('polls:result', question_id=question.id)
    # return HttpResponse('youre voting on question {}.'.format(question_id))
