from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .serializers import GroupSerializer
from rest_framework import viewsets


from .models import Group


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serialize_class = GroupSerializer

class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups/group_list.html'
    login_url = 'login'

class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/group_detail.html'
    login_url = 'login'

class GroupUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Group
    fields = ('group_name',)
    template_name = 'groups/group_edit.html'
    login_url = 'login'

class GroupDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Group
    template_name = 'groups/group_delete.html'
    success_url = reverse_lazy('group_list')
    login_url = 'login'

class GroupCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Group
    fields = ('group_name',)
    template_name = 'groups/group_new.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)