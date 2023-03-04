import datetime
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from ..models import Question, Choice
# Create your views here.

def list(request):
    logger.info('Index was accessed at ' + str(datetime.datetime.now()) + ' hours!')
    latest_question_list = Question.objects.filter(pub_date__lt=timezone.now()).order_by("pub_date")[:5]
    return render(request, "app/questions/list.html", {
        "latest_question_list": latest_question_list
    })


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "app/questions/details.html", {
        "question": question
    })


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "app/questions/results.html", {
        "question" : question
    })

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        select_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "app/questions/details.html", {
            "question": question,
            "error_message": "Non hai scelto una risposta"
        })
    else:
        select_choice.votes = select_choice.votes + 1
        select_choice.save()
        return HttpResponseRedirect(reverse("app:results", args=(question_id,)))
