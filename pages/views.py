from django.shortcuts import render
from django.views.generic import ListView
from .models import Status, Issue




# Create your views here.



class BoardView(ListView):
    template_name ='issues/board.html'
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_do = Status.objects.get(name='To Do')
        in_prog = Status.objects.get(name='In Progress')
        done = Status.objects.get(name='Done')  
        context['to_do_list'] = Issue.objects.filter(
            status=to_do
        ).order_by('-created_on').reverse()
        context['in_prog_list'] = Issue.objects.filter(
            status=in_prog
        ).order_by('-created_on').reverse()
        context['done_list'] = Issue.objects.filter(
            status=done
        ).order_by('-created_on').reverse()
        return context
    
