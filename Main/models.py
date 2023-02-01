from django.conf import settings
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


def current_user(request):
	return request.user

# Create your models here.
def upload_location(instance, filename):
	s = "%s/%s" %(instance.user.username, filename)
	print(s)
	return s


class User(AbstractUser):
	username = models.CharField(unique=True,max_length=30)
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=True)
	first_name = models.CharField(blank=False,null=False, max_length=50)
	last_name = models.CharField(blank=False,null=False, max_length=50)
	phone = models.CharField(max_length=14, null=True, blank=True)
	class Gender(models.TextChoices):
		SELECT = 'SELECT'
		MALE = 'MALE'
		FEMALE = 'FEMALE'
		UNSPECIFIED = 'PREFERRED NOT TO SAY'
	Gender = models.CharField(choices=Gender.choices, default="Select", max_length=20)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','first_name','last_name']

	def save(self, *args, **kwargs):
		self.password = make_password(self.password)
		super(User, self).save(*args, **kwargs)	

class Post(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	headline=models.CharField(max_length=400, null=False, blank=False)
	body_top=models.TextField(null=True, blank=True)
	body_middle=models.TextField(null=True, blank=True)
	body_bottom=models.TextField(null=True, blank=True)
	views=models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True, auto_created=True)
	urls= models.SlugField(max_length=500, unique=True, blank=True, editable=False)
	image_top=models.ImageField(upload_to='post_images/', blank=True)
	image_middle=models.ImageField(upload_to='post_images/', blank=True)
	image_bottom=models.ImageField(upload_to='post_images/', blank=True)

	def save(self, *args, **kwargs):
		self.urls = self.headline
		self.urls = slugify(self.urls)
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.headline
    
class Department(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	name=models.CharField(max_length=100, unique=True, blank=False, null=False)
	responsible = models.TextField(blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True)
	urls = models.SlugField(max_length=500, unique=True, blank=True, editable=False)
	image =models.ImageField(upload_to='department_images/', blank=True)
	def save(self, *args, **kwargs):
		self.urls = self.name
		self.responsible = self.responsible.capitalize()				
		self.urls = slugify(self.urls)
		super(Department, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Footer(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	body = models.TextField(blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True)
	year = models.DateField(auto_now=True)

	def __str__(self):
		return str(self.year)
	
class About(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	image =models.ImageField(upload_to='about_images/', blank=True)	
	intro = models.CharField(max_length=200, blank=False, null=False)
	body = models.TextField(blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.body[:24] + "..."

class Contact(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	address = models.CharField(max_length=200, blank=False, null=False)
	email = models.CharField(max_length=200, blank=False, null=False)
	call = models.CharField(max_length=200, blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.address

class Email(models.Model):
	name = models.CharField(blank=False, null=False, max_length=100)
	email = models.EmailField(unique=False)
	subject = models.CharField(blank=False, null=False, max_length=200)
	message = models.TextField(blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	def __str__(self):
		return self.email