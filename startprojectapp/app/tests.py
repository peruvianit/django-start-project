import datetime

from django.test import TestCase

from django.utils import timezone
from django.urls import reverse

from .models import Question

#Test Models
class QuestionModelTest(TestCase):
    def test_was_published_recently_with_questions(self):
        ''' Verifica se la data di pubblicazione è recente da un giorno'''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Il modelo di Django è MVC o MVT ?", pub_date=time)

        self.assertIs(future_question.was_published_recented(), False)

#Test View
class QuestionViewTest(TestCase):
    def test_no_question(self):
        ''' Verifica il messaggio da mostrare se  non esiste una domanda '''
        response = self.client.get(reverse("app:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Non ci sono domande disponibili")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
