from django.urls import path
from .views import RequisitionListView, RequisitionDetailView, RequisitionUpdateView, RequisitionDeleteView, RequisitionCreateView


urlpatterns = [
    path('<int:pk>/edit/',RequisitionUpdateView.as_view(), name='requisition_edit'),
    path('<int:pk>/',RequisitionDetailView.as_view(), name='requisition_detail'),
    path('<int:pk>/delete/',RequisitionDeleteView.as_view(), name='requisition_delete'),
    path('new/',RequisitionCreateView.as_view(), name='requisition_new'),
    path('',RequisitionListView.as_view(), name='requisition_list'),
]
