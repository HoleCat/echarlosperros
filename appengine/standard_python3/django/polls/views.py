from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.http.response import StreamingHttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
import cv2
import numpy as np

def camera(id):
    capture = cv2.inread(0)
    return capture

def IndexView(request):
    latest_question_list = Question.objects.all()
    latest_choice_list = Choice.objects.all()

    context = {'latest_question_list':latest_question_list,'latest_choice_list':latest_choice_list}
    return render(request,'polls/index.html',context)
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,))
        )
