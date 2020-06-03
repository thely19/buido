import random
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from requesters.models import Requester
from groups.models import Group

class Requisition(models.Model):
	date_request = models.DateField()
	requester = models.ForeignKey(Requester, on_delete=models.SET_NULL, null=True, related_name='requisition')
	narration = models.CharField(max_length=250, blank=False, null=False)
	amount = models.DecimalField(max_digits=19, decimal_places=2)
	is_requested = models.BooleanField(default=False)
	annexe = models.FileField(upload_to='attach/', blank=True, null=True)
	slug = models.SlugField(max_length=130, unique=True, blank=True)
	group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='req_group')
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def save(self, *args, **kwargs):
		randone = ''.join((random.choice(self.narration[:8]) for i in range(8)))
		self.slug = slugify(f'{self.narration[:4]}{random.randint(0,40)}{randone}')
		super(Requisition, self).save(*args, **kwargs)

	def __str__(self):
		return self.narration

	def get_absolute_url(self):
		return reverse('requisition_detail', args=[str(self.id)])

class RequiDetails(models.Model):
	requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE, related_name='details')
	narration = models.TextField()
	quantity = models.DecimalField(max_digits=19, decimal_places=2, default=0)
	unit_price = models.DecimalField(max_digits=19, decimal_places=2, default=0)
	total_price = models.DecimalField(max_digits=19, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def get_absolute_url(self):
		return reverse('requiDetails_detail', args=[str(self.id)])