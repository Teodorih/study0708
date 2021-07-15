from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        q = Question.objects.order_by('-pub_date')[:5]
        return q


class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class QuestionCreate(generic.CreateView):
    model = Question
    fields = ['question_text']
    template_name = 'polls/question_form.html'
    success_url = reverse_lazy('polls:index')


class QuestionUpdate(generic.UpdateView):
    model = Question
    fields = ['question_text']
    template_name = 'polls/question_form.html'
    success_url = reverse_lazy('polls:index')


class QuestionDelete(DetailView):
    model = Question
    template_name = 'polls/question_confirm_delete.html'
    success_url = reverse_lazy('polls:index')


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
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))