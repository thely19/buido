from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


from .models import Requisition, RequiDetails


class RequisitionListView(LoginRequiredMixin, ListView):
    model = Requisition
    template_name = 'requisitions/requisition_list.html'
    login_url = 'login'


class RequisitionDetailView(LoginRequiredMixin, DetailView):
    model = Requisition
    template_name = 'requisitions/requisition_detail.html'
    login_url = 'login'


class RequisitionUpdateView(LoginRequiredMixin, UpdateView):
    model = Requisition
    fields = ('date_request', 'narration', 'amount','is_requested', 'annexe', 'group')
    template_name = 'requisitions/requisition_update.html'
    login_url = 'login'


class RequisitionDeleteView(LoginRequiredMixin, DeleteView):
    model = Requisition
    template_name = 'requisitions/requisition_delete.html'
    success_url = reverse_lazy('requisition_list')
    login_url = 'login'


class RequisitionCreateView(LoginRequiredMixin, CreateView):
    model = Requisition
    fields = ('date_request', 'narration', 'amount','is_requested', 'annexe', 'group')
    template_name = 'requisitions/requisition_new.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)