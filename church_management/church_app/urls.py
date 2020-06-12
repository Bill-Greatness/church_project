from . import views 
from django.urls import path 
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('about-us/', views.about, name='about-church'),
    path('forum/', views.forum, name='forum-home'),
    path('gallery/', views.gallery, name='our-gallery'),
    path('add-to-forum/', views.add_forum_post, name='add-to-forum'),
    path('register/', views.register, name='register'),
    path('user-profile/', views.profile, name='user-profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='church_app/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='church_app/login.html'), name='login'),
    path('post-view/<int:id>/', views.forum_post_view, name='post-view'),
    path('resources/', views.resources, name='resources'),
    path('requests-and/news/', views.requests_and_news, name='requests-and-news'),
    path('received-requests/', views.received_requests, name='received-requests')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
