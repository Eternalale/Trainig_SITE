from django.shortcuts import render, redirect
from django.contrib.auth import  logout
from django.views.generic import ListView, CreateView,UpdateView, View, DetailView, DeleteView
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import  RegistrationForm , LoginForm, TaskForm


class IndexView(ListView):
    model = Task
    template_name = 'base.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'tasks/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    

class LoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'tasks/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

def logout_view(request):
    logout(request)
    return redirect('login')


# class TaskCreateView(LoginRequiredMixin,CreateView):
#     model = Task
#     template_name = 'tasks/create.html'
#     fields =  ['title', 'description', 'owner']
#     login_url =  reverse_lazy('login')

#     def form_valid(self, form):
#         messages.success(self.request, 'Super, new task added!')
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse('index')
@login_required
def taskcreate(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('/tasks/')
    return render(request, "tasks/create.html", context={"form":form}) 

class TaskView(ListView):
    model = Task
    template_name = 'tasks/exercises.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.all()
        return context  
    

class TaskDetailView(DetailView):
    model = Task
    template_name  = 'tasks/view.html'
    context_object_name  = 'task' 
    pk_url_kwarg = 'task_id'   


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    fields = ['title', 'description', 'start_or_end_task']
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'task_pk'
    login_url = reverse_lazy('login')
