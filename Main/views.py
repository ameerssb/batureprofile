



from django.shortcuts import render
from .models import Social,HomeInfo,Project,Research as Re,ResearchInterest,Graduate,Publication,Experience as Ex,ExperienceDetail,Photos as P,Footer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def Home(request):
    social = Social.objects.last()
    homeinfo = HomeInfo.objects.last()
    footer = Footer.objects.last()
    context = {'page': 'home', 'social': social, 'homeinfo': homeinfo, 'footer': footer,}
    
    return render(request, 'Main/index.html', context)

def Researchs(request):
    social = Social.objects.last()
    research = Re.objects.last()
    researchinterest = ResearchInterest.objects.all()
    g1 = Graduate.objects.filter(types='In-Progress')
    g2 = Graduate.objects.filter(types='Completed')
    p1 = Publication.objects.filter(types='Journals')
    p2 = Publication.objects.filter(types='Conferences')
    footer = Footer.objects.last()
    context = {'page': 'research', 'social': social, 'research': research, 'researchinterest': researchinterest, 'g1': g1, 'g2': g2, 'p1': p1, 'p2': p2, 'footer': footer,}

    return render(request, 'Main/research.html', context)

def Experiences(request):
    social = Social.objects.last()
    experience = Ex.objects.all()
    experiencedetail = ExperienceDetail.objects.all()
    footer = Footer.objects.last()
    context = {'page': 'experience', 'social': social, 'experience': experience, 'experiencedetail': experiencedetail, 'footer': footer,}

    return render(request, 'Main/experience.html', context)

def Projects(request):

    homeinfo = HomeInfo.objects.last()
    social = Social.objects.last()
    project = Project.objects.all().order_by('-created')
    paginator = Paginator(project, 5)
    page = request.GET.get('page')
    try:
        past = paginator.page(page)
    except PageNotAnInteger:
        past = paginator.page(1)
    except EmptyPage:
        past = paginator.page(paginator.num_pages)    
    # print(past)
    context = {'page': 'project', 'homeinfo': homeinfo,'social':social,'project':project}
    return render(request, 'Main/project.html', context)

def Photoss(request):
    social = Social.objects.last()
    photos = P.objects.all()
    footer = Footer.objects.last()
    context = {'page': 'photos', 'social': social, 'photos': photos, 'footer': footer,}

    return render(request, 'Main/photos.html', context)

def Contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # email_adding = Email(name=name,email=address, subject=subject, message=message)
        # email_adding.save()
        # messages.success(request, "Email Submitted Successfully...")
        # return HttpResponseRedirect('contact-us')

    social = Social.objects.last()
    footer = Footer.objects.last()
    context = {'page': 'contact', 'social': social, 'footer': footer,}

    return render(request, 'Main/contact.html', context)
