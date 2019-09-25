from django.db import models
from django.utils import timezone


# Create your models here.
class Application(models.Model):
	first_name=models.CharField(max_length=45)
	middle_name=models.CharField(max_length=45, blank=True, null=True)
	last_name=models.CharField(max_length=45)
	email=models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,)
	gender = models.CharField(max_length=7)
	phone_number=models.CharField(max_length=45)
	date_submitted = models.DateTimeField(('date submitted'),default=timezone.now)
	street_name=models.CharField(max_length=55)
	town=models.CharField(max_length=45)
	state=models.CharField(max_length=45)
	country=models.CharField(max_length=45,default='Nigeria')

	
	class Meta:
		verbose_name_plural = 'Applications'

	def __str__(self):
		return self.id
	def get_absolute_url(self):
		return reverse('application_detail', args=[str(self.id)])
