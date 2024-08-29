from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.shortcuts import redirect, get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Task, Category, Comment
from .forms import TaskForm, CategoryForm, CommentForm
from .filters import TaskFilter, CategoryFilter
from .serializers import TaskSerializer

def list_tasks(request):
    tasks_list = Task.objects.filter(user=self.request.user)
    paginator = Paginator(tasks_list, 10)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    return render(request, 'task_list.html', {'tasks': tasks})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        task.completed = not task.completed
        task.save()
        return Response({'status': 'completed status updated', 'completed': task.completed})

class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    login_url = 'accounts:login'
    filterset_class = TaskFilter

    def get_queryset(self):
        tasks_list = Task.objects.filter(user=self.request.user)
        return tasks_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), 10)
        page = self.request.GET.get('page')
        try:
            tasks = paginator.page(page)
        except PageNotAnInteger:
            tasks = paginator.page(1)
        except EmptyPage:
            tasks = paginator.page(paginator.num_pages)

        context['tasks'] = tasks
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')
    login_url = 'accounts:login'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        return form

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')
    login_url = 'accounts:login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        return form
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    login_url = 'accounts:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = self.object
            comment.user = request.user
            comment.save()
            return redirect('todo:task_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')
    login_url = 'accounts:login'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.can_be_deleted():
            self.object.delete()
            return redirect(self.get_success_url())
        else:
            return HttpResponseForbidden("Esta task não pode ser excluída porque está marcada como completa.")

class CategoryListView(LoginRequiredMixin, FilterView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    login_url = 'accounts:login'
    filterset_class = CategoryFilter

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('todo:category_list')
    login_url = 'accounts:login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('todo:category_list')
    login_url = 'accounts:login'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('todo:category_list')
    login_url = 'accounts:login'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
