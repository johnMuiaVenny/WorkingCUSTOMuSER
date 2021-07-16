from django.shortcuts import render
from django.http import HttpResponse
from .models import COMMENTT
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


#MODELFORMS. CRUD
class allComments(ListView):
    template_name = 'COMMENTSaPP/allComments.html'
    context_object_name = 'all'

    def get_queryset(self):
        return COMMENTT.objects.order_by('-pk')

class Comment(DetailView):
    model = COMMENTT
    template_name = 'COMMENTSaPP/Comment.html'

class AddComment(CreateView):
    model = COMMENTT
    fields = ['Title', 'Description', 'Picture']

class UpdateComment(UpdateView):
    model = COMMENTT
    fields = ['Title', 'Description', 'Picture']

class DeleteComment(DeleteView):
    model = COMMENTT
    success_url = reverse_lazy('COMMENTS:allComments')

