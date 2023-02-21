from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
# Create your views here.


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "app/index.html", {
        "latest_question_list": latest_question_list
    })


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "app/details.html", {
        "question": question
    })


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "app/results.html", {
        "question" : question
    })

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        select_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "app/details.html", {
            "question": question,
            "error_message": "Non hai scelto una risposta"
        })
    else:
        select_choice.votes = select_choice.votes + 1
        select_choice.save()
        return HttpResponseRedirect(reverse("app:results", args=(question_id,)))
