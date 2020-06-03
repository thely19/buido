from django.urls import path
from .views import GroupListView, GroupUpdateView, GroupDetailView, GroupDeleteView, GroupCreateView

urlpatterns = [
    path('<int:pk>/edit/', GroupUpdateView.as_view(), name='group_edit'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
    path('new/', GroupCreateView.as_view(), name='group_new'),
    path('', GroupListView.as_view(), name='group_list'),
]
