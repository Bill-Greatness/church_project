from django.shortcuts import render, redirect
from .forms import ForumForm,\
     UserProfileForm, UserFormUpdate,\
     ProfileUpdateForm, RequestForm
from .models import Forum, Request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def homepage(request):
    return render(request, 'church_app/index.html')


def about(request):
    return render(request, 'church_app/about.html')


@login_required
def register(request):
    if request.method == 'POST':    
        update_form = UserFormUpdate(request.POST)
        if update_form.is_valid():
            update_form.save()
            username = update_form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('home-page')
        else:
            print(update_form.error_messages)
    else:
        update_form = UserFormUpdate()
    context = {'form':update_form, 'title':'New Registration'}
    return render(request, 'church_app/register.html', context)

@login_required
def forum(request):
    forum_posts = Forum.objects.all()
    context={'posts':forum_posts, 'title':'Forum Posts'}
    return render(request, 'church_app/forum.html', context)

def gallery(request):
    return render(request, 'church_app/gallery.html')

@login_required
def forum_post_view(request, id):
    current_post = Forum.objects.get(id=id)
    context={'title':current_post.title, 'current_post':current_post}
    return render(request, 'church_app/post_view.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST,request.FILES, instance=request.user.profile)
        updated_form = ProfileUpdateForm(request.POST, instance=request.user)

        if profile_form.is_valid() and updated_form.is_valid():
            profile_form.save()
            updated_form.save()
            return redirect('user-profile')
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
        updated_form = ProfileUpdateForm(instance=request.user)
    context={'title':'User Profile', 'updated_form': updated_form, 'profile_form':profile_form}
    return render(request, 'church_app/profile.html', context)

def login(request):
    return render(request, 'church_app/login.html')

@login_required
def add_forum_post(request):
    if request.method == 'POST':
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('forum-home')
        else:
            print(form.errors)
    else:
        form = ForumForm()
    context = {'form': form, 'title':'Add Forum Post'}
    return render(request, 'church_app/new-forum-post.html', context)


def requests_and_news(request):
    if request.method == 'POST':
        r_form = RequestForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            return redirect('home-page')
    else:
        r_form = RequestForm()
    return render(request, 'church_app/requests.html',{"title":"Request and News", 'form':r_form})

def received_requests(request):
    messages_recieved = Request.objects.all()
    print(messages_recieved)
    return render(request, 'church_app/received_requests.html',{'requests': messages_recieved, 'title': 'Received Requests'})

def resources(request):
    return render(request, 'church_app/resources.html', {'title':"Resources - Music and More"})