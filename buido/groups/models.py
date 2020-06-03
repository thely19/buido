from django.db import models
from django.urls import reverse
from requesters.models import Requester



class Group(models.Model):
    group_name = models.CharField(max_length=250, blank=False, null=False)
    creater = models.ForeignKey(Requester, on_delete=models.SET_NULL, null=True, related_name='group')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.group_name
    
    def get_absolute_url(self):
        return reverse('group_detail', args=[str(self.id)])
    


class Affiliated(models.Model):
	attender = models.ForeignKey(Requester, on_delete=models.SET_NULL, null=True, related_name='user_affiliated')
	group_attender = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='group_affiliated')
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	class Meta:
		unique_together = (('attender','group_attender'),)
		index_together = (('attender','group_attender'),)