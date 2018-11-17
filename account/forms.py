from random import choice, choices

from django.forms import ModelForm
from django import forms
from account.models import *

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
     #   exclude = ['is_staff','is_doctor','is_superuser','is_active','is_ordinary_user','']
        fields=['first_name','last_name','email','username','password']

class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields=['yearsOfExperience','fieldOfStudy','hospital']


class OrdinaryUserForm(ModelForm):
    class Meta:
        model=OrdinaryUser
        fields=['phoneNumber']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SymptomsFrom(forms.Form):
    symptoms=forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'


class SaveDataForm(forms.ModelForm):
    CHOICES=[(1,'Yes')
        ,
             (0,'No')]

    predicted_risk=forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Data
        fields = '__all__'



class SmokingForm(forms.Form):
    CHOICES=[(1,'Yes ,all most everday'),
             (2,'Yes ,2-4 days a week'),
             (3, 'Yes ,occasionally'),
             (4, 'No ,I donot - drink at all')
             ]
    choices=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,label="Do you drink alcohol?")


class ExerciseForm(forms.Form):
    CHOICES=[(1,'Yes,I exercise everyday'),
             (2,'Yes ,2-3 days a week'),
             (3, 'No,I donot exercise')
             ]
    choices=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,
                              label="Do you exercise?")


class SymptomForm1(forms.Form):
    CHOICES=[('1','chest pain'),
             ('2','indigestion'),
             ('3', 'heartburn'),
             ('4', 'weakness'),
             ('5', 'sweating'),
             ('6', 'shortness of breath'),
             ('7', 'cramping')
             ]
    choices=forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple,
                              label="We are looking for symptoms of Angina.Which symptoms do you experience? ")

class SymptomForm2(forms.Form):
    CHOICES=[('1','chest discomfort'),
             ('2','coughing'),
             ('3', 'dizziness'),
             ('4', 'vomiting'),
             ('5', 'face seems gray'),
             ('6', 'restlessness'),
             ('7', 'perspiration and clammy skin'),
             ('8', 'an overall feeling of being unwell')
             ]
    choices=forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple(),
                              label="We are looking for symptoms of Heart attack.\n Which symptoms do you experience?")

class SymptomForm3(forms.Form):
    CHOICES=[(1,'intense tightening in the chest'),
             (2,'air hunger'),
             (3, 'feeling of suffocation'),
             (4, 'breathless after activity '),
             (5, 'short of breath sooner than you \n used to be  after physical activity'),
             ]
    choices=forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple(),
                              label="What kind of symptoms do you experience ?")
