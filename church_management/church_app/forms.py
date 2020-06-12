from django import forms
from django.contrib.auth.models import User
from .models import Profile, Forum, Request
# from martor.fields import MartorFormField
from django.contrib.auth.forms import UserCreationForm




class UserFormUpdate(UserCreationForm):
    class Meta: 
        model = User
        fields = ('email','username','password1','password2')


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('email','username')




class UserProfileForm(forms.ModelForm):
    OPTIONS = (("","Gender"),('Male','Male'),('Female','Female'))
    REGIONOPTION = (
        ("","Select Region"),('Western Region','Western'),
        ('Eastern Region','Eastern'),
        ('Upper East Region','Upper East'),
        ('Ahafo Region','Ahafo'),
        ('Upper West Region','Upper West'),
        ('Ashanti Region','Ashanti'),
        ('Northern Region','Northern'),
        ('Accra Region','Accra')
    )
    WINGOPTIONS = (
        ("","Select Fellowship"),
        ('Men Fellowship','Men Fellowship'),
        ('Women Fellowship','Women Fellowship'),
        ('Youth Fellowship','Youth Fellowship'),
        ('Children Fellowship','Children')
        )
    firstname = forms.CharField(label='Firstname', 
                    widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    surname = forms.CharField(label='Surname', 
                    widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    member_id = forms.CharField(label='Member ID', 
                    widget=forms.TextInput(attrs={'placeholder': 'Member ID'}))
    date_of_birth = forms.CharField(label='Birth Date', 
                    widget=forms.TextInput(attrs={'placeholder': 'Date Of Birth', 'type':'date'}))
    region = forms.ChoiceField(choices=REGIONOPTION)
    phone_number= forms.CharField(label='Phone', 
                    widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    resident_address = forms.CharField(label='Address', 
                    widget=forms.TextInput(attrs={'placeholder': 'Residential Address'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'required':'false','accept':'*.jpg,*.png'})) 
    wing_name = forms.ChoiceField(choices=WINGOPTIONS)
    gender = forms.ChoiceField(choices=OPTIONS)


    class Meta:
        model = Profile
        fields = (
        'firstname','surname','member_id','image',
        'date_of_birth','region','phone_number','resident_address','wing_name','gender')


class ForumForm(forms.ModelForm):
    title = forms.CharField(label='Message Title',widget=forms.TextInput(attrs={'placeholder':'Message Title'}))
    content = forms.Textarea(attrs={'placeholder':'Message Content'})
    image = forms.ImageField(widget=forms.FileInput(attrs={'required':'false','accept':'*.jpg,*.png'})) 


    class Meta:
        model = Forum
        fields = ('title','content', 'image')


class RequestForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'placeholder':'Your Full name'}))
    email = forms.EmailField()
    district = forms.CharField(label='District',widget=forms.TextInput(attrs={'placeholder':'Your District'}))
    phone = forms.CharField(label='Your Phone Number',min_length=10, max_length=10)
    request_title = forms.CharField(max_length=50, required=True)
    request_content = forms.Textarea()

    class Meta:
        model = Request
        fields = ('full_name','email','district','phone','request_title','request_content')