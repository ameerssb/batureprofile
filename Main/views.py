from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse
from .models import Hint,Header,Email,Social,HomeInfo,Project,Cat_Projects,Research as Re,ResearchInterest,Graduate,Publication,Experience as Ex,ExperienceDetail,Photos as P,Footer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def Hints(request):
    if  request.method == 'GET':
        otherhint = Hint.objects.order_by('?')[:20]
        otherhint = list(otherhint.values())
        data = {'hint_list':otherhint}
        return JsonResponse(data)
    

def Home(request):
    if  request.method == 'GET':
        hint = Hint.objects.filter(Q(author='Jameleddine Hassine') | Q(author__startswith='Mi')).order_by('?').first()
        print(hint)
        social = Social.objects.last()
        homeinfo = HomeInfo.objects.last()
        header = Header.objects.all().order_by('priority')
        footer = Footer.objects.last()
        context = {'page': 'home', 'social': social, 'homeinfo': homeinfo, 'footer': footer,'header':header,'hint':hint}
    
        return render(request, 'Main/index.html', context)

def Researchs(request):
    social = Social.objects.last()
    research = Re.objects.last()
    researchinterest = ResearchInterest.objects.all()
    g1 = Graduate.objects.filter(types='In-Progress')
    g2 = Graduate.objects.filter(types='Completed')
    p1 = Publication.objects.filter(types='Journals')
    p2 = Publication.objects.filter(types='Conferences')
    header = Header.objects.all().order_by('priority')    
    footer = Footer.objects.last()
    context = {'page': 'research', 'social': social, 'research': research, 'researchinterest': researchinterest, 'g1': g1, 'g2': g2, 'p1': p1, 'p2': p2, 'footer': footer,'header':header,}

    return render(request, 'Main/research.html', context)

def Experiences(request):
    social = Social.objects.last()
    experience = Ex.objects.all().order_by('priority')
    experiencedetail = ExperienceDetail.objects.all()
    footer = Footer.objects.last()
    header = Header.objects.all().order_by('priority')    
    context = {'page': 'experience', 'social': social, 'experience': experience, 'experiencedetail': experiencedetail, 'footer': footer,'header':header,}

    return render(request, 'Main/experience.html', context)

def Cat_Project(request):
    homeinfo = HomeInfo.objects.last()
    social = Social.objects.last()
    cat_project = Cat_Projects.objects.all().order_by('priority')
    print(cat_project[1].name)
    footer = Footer.objects.last()
    header = Header.objects.all().order_by('priority')    
    context = {'page': 'project', 'homeinfo': homeinfo,'social':social,'cat_project':cat_project, 'footer': footer,'header':header,}
    return render(request, 'Main/projectcategory.html', context)

def Projects(request,cat_name):
    homeinfo = HomeInfo.objects.last()
    social = Social.objects.last()
    cat_pro = Cat_Projects.objects.get(slug=cat_name)
    project = Project.objects.filter(cat=cat_pro).order_by('priority')
    footer = Footer.objects.last()
    header = Header.objects.all().order_by('priority')    
    paginator = Paginator(project, 5)
    page = request.GET.get('page')
    # try:
    #     project = paginator.page(page)
    # except PageNotAnInteger:
    #     project = paginator.page(1)
    # except EmptyPage:
    #     project = paginator.page(paginator.num_pages)    
    # print(project)
    context = {'page': 'project', 'homeinfo': homeinfo,'social':social,'cat':cat_pro,'project':project, 'footer': footer,'header':header,}
    return render(request, 'Main/project.html', context)

def ProjectPage(request,cat_name,pk):
    homeinfo = HomeInfo.objects.last()
    social = Social.objects.last()    
    cat_pro = Cat_Projects.objects.get(slug=cat_name)
    projectpage = Project.objects.get(Q(pk=pk) & Q(cat=cat_pro))
    context = {'page': 'project', 'homeinfo': homeinfo,'social':social,'project':projectpage}
    return render(request, 'Main/projectpage.html', context)

def Photoss(request):
    social = Social.objects.last()
    photos = P.objects.all()
    header = Header.objects.all().order_by('priority')    
    footer = Footer.objects.last()
    context = {'page': 'photos', 'social': social, 'photos': photos, 'footer': footer,'header':header,}

    return render(request, 'Main/photos.html', context)

def Contacts(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            address = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            message = message + "\n\n" + "from" + name
            
            email_adding = Email(name=name,email=address, subject=subject, message=message)
            email_adding.save()
            send_mail(subject,message,address,['baturesanisufyan@gmail.com'],fail_silently=True,)
            messages.success(request, "Email Submitted Successfully...")
            return HttpResponseRedirect('contact')
        except:
            messages.success(request, "An error occured while sending email")
            return HttpResponseRedirect('contact')            
    social = Social.objects.last()
    header = Header.objects.all().order_by('priority')    
    footer = Footer.objects.last()
    context = {'page': 'contact', 'social': social, 'footer': footer,'header':header,}

    return render(request, 'Main/contact.html', context)
