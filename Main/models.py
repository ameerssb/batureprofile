from django.conf import settings
from django.db import models
from embed_video.fields import EmbedVideoField

class Social(models.Model):
	office = models.CharField(max_length=250, default="#", blank=True)
	mail = models.CharField(max_length=250, default="#", blank=True)
	twitter=models.CharField(max_length=250, default="#", blank=True)
	facebook=models.CharField(max_length=250, default="#", blank=True)
	youtube=models.CharField(max_length=250, default="#", blank=True)
	instagram=models.CharField(max_length=250, default="#", blank=True)
	telegram=models.CharField(max_length=250, default="#", blank=True)
	linkedin=models.CharField(max_length=250, default="#", blank=True)
	tiktok=models.CharField(max_length=250, default="#", blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)

	def __str__(self):
		return str(self.id)
    
class HomeInfo(models.Model):
	body = models.TextField(blank=True)
	image = models.FileField(blank=True)
	video = EmbedVideoField(blank=True)
	cv = models.FileField(blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)

	def __str__(self):
		return str(self.id)

class Research(models.Model):
	body = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)

	def __str__(self):
		return str(self.id)

class ResearchInterest(models.Model):
	name = models.CharField(max_length=250, blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)

	def __str__(self):
		return str(self.id)

class Graduate(models.Model):
    name = models.CharField(max_length=250, blank=True)
    class Gr_Type(models.TextChoices):
        in_progress = 'In-Progress'
        completed = 'Completed'
    types = models.CharField(choices=Gr_Type.choices, default="__________", max_length=20)
    thesis_title = models.CharField(max_length=250, blank=True)   
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
	    return str(self.id)

class Publication(models.Model):
	class P_Type(models.TextChoices):
		journals = 'Journals'
		conferences = 'Conferences'
	types = models.CharField(choices=P_Type.choices, default="__________", max_length=20)
	thesis_title = models.CharField(max_length=250, blank=True)	
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)

	def __str__(self):
		return str(self.id)

class Experience(models.Model):
	position = models.CharField(max_length=200)
	time = models.CharField(max_length=250)
	place = models.TextField()
	department = models.CharField(max_length=250)
	logo = models.FileField(blank=True, default='default_user.png')
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)

	def __str__(self):
		return str(self.id)

class ExperienceDetail(models.Model):
	experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)

	def __str__(self):
		return str(self.id)

class Photos(models.Model):
	number = models.IntegerField()
	image = models.FileField()	

	def __str__(self):
		return str(self.id)	
	
class Footer(models.Model):
	body = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)

	def __str__(self):
		return str(self.id)
	