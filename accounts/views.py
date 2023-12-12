# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView
from .models import Issue, Status
from .forms import IssueForm
from django.urls import reverse_lazy, reverse

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


class StatusUpdateView(UpdateView):

    template_name = 'issues/board.html'
    model = Issue
    fields = ['summary', 'description', 'status',]

    def form_valid(self, form):
        form.instance.status = Status.objects.get(name='In Progress')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('board')
    
def issue_new(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.reporter = request.user
            issue.save()
            return redirect('board')
    else:
        form = IssueForm()
    return render(request, 'issues/issue_new.html', {'form': form})

def issue_edit(request, pk):

    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "POST":
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.reporter = request.user
            issue.save()
            return redirect('board')
    else:
        form = IssueForm(instance=issue)
    return render(request, 'issues/issue_new.html', {'form': form})