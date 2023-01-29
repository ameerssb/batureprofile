from django.shortcuts import render, get_object_or_404
from .models import Post,Footer,Email
from .models import Department as dept
from .models import Contact as Cont
from .models import About as Abt
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def Home(request):
    recent_news = Post.objects.all().order_by('-created')[:2]
    slider = Post.objects.all().order_by('-views')[:5]
    most_views = Post.objects.all().order_by('-views')[:2]
    others1 = Post.objects.all().order_by('-created')[2:4]
    others2 = Post.objects.all().order_by('-created')[4:6]
    footer = Footer.objects.last()
    contact = Cont.objects.last()
    context = {'footer': footer, 'recent':recent_news, 'most':most_views, 'others1':others1, 'others2':others2, 'slider':slider, 'contact':contact}
    
    return render(request, 'Main/index.html', context)

def All_News(request):
    queryset_list=Post.objects.all().order_by('-created')
    most_views = Post.objects.all().order_by('-views')[:5]
    contact = Cont.objects.last()
    footer=Footer.objects.last()    
    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {'list': queryset, 
                'footer': footer, 
                'recent':most_views,
                "page":"page",
                'contact':contact,
              }
    return render(request, 'Main/all-news.html', context)

def News(request, urls):
    instance = get_object_or_404(Post,urls=urls)
    instance.views = instance.views + 1
    instance.save()
    most_views = Post.objects.all().order_by('-views')[:5]
    footer=Footer.objects.last()    
    contact = Cont.objects.last()
    context = {'list': instance, 'footer': footer, 'recent':most_views,'contact':contact}
    return render(request, 'Main/news.html', context)

def Department(request):
    queryset_list=dept.objects.all()
    most_views = Post.objects.all().order_by('-views')[:5]
    contact = Cont.objects.last()    
    footer=Footer.objects.last()    
    context = {'list': queryset_list, 'footer':footer, 'recent':most_views, 'contact':contact}
    return render(request, 'Main/departments.html', context)

def DepartmentDetail(request, urls):
    dept_list = get_object_or_404(dept,urls=urls)
    most_views = Post.objects.all().order_by('-views')[:5]
    contact = Cont.objects.last()
    footer=Footer.objects.last()    
    context = {'list': dept_list, 'footer':footer, 'recent':most_views, 'contact':contact}
    return render(request, 'Main/dept-details.html', context)

def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        email_adding = Email(name=name,email=address, subject=subject, message=message)
        email_adding.save()
        messages.success(request, "Email Submitted Successfully...")
        return HttpResponseRedirect('contact-us')

    contact = Cont.objects.last()
    footer=Footer.objects.last()    
    context = {'footer':footer,'contact':contact}

#    return HttpResponse('ready to start')
    return render(request, 'Main/contact-us.html', context)

def About(request):

    footer=Footer.objects.last()
    contact = Cont.objects.last()
    about = Abt.objects.last()
    context = {'footer':footer,'about':about, 'contact': contact}

#    return HttpResponse('ready to start')
    return render(request, 'Main/about-us.html', context)