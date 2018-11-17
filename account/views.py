from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pickle
from account.decorators import doctor_required,ordinary_user_required
#from account.forms import DoctorForm,OrdinaryUserForm,UserForm,LoginForm,SymptomsFrom,DataForm
from account.forms import *
from django.conf import settings
import numpy as np
# Create your views here.


def user_login(request):
    if request.method =='POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            cd=form.cleaned_data

            user=authenticate(username=cd['username'],password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('account:home')
                    #return HttpResponse('logged in succesfully')
                else:
                    return HttpResponse('disabled account')
            else :
                return render(request, 'account/login.html', {'form':form,'error':'your username and password didnot match .Please try again'})

    else:
        form=LoginForm()

        return  render(request, 'account/login.html', {'form':form})

def signup_doctor(request):
    if request.method =='POST':

        user_form = UserForm(request.POST)
        doctor_form = DoctorForm(request.POST,request.FILES)

        if user_form.is_valid() and doctor_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.is_doctor=True
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_doctor=doctor_form.save(commit=False)
            new_doctor.user=new_user
            new_doctor.save()

            return HttpResponse("successful")
        else:
            return HttpResponse("error")

    else:
        user_form=UserForm()
        doctor_form=DoctorForm()

        return render(request, 'account/signup_doctor.html',
                      {'user_form': user_form, 'doctor_form':doctor_form})


def signup_ordinary_user(request):
    if request.method =='POST':

        user_form = UserForm(request.POST)
        ordianary_user_form = OrdinaryUserForm(request.POST)

        if user_form.is_valid() and ordianary_user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.is_ordinary_user=True
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_ordinary_user=ordianary_user_form.save(commit=False)
            new_ordinary_user.user=new_user
            new_ordinary_user.save()

            return HttpResponse("successful")
        else:
            return HttpResponse("error")

    else:
        user_form=UserForm()
        ordianary_user_form=OrdinaryUserForm()

        return render(request, 'account/signup_ordinary_user.html',
                      {'user_form': user_form, 'ordianary_user_form':ordianary_user_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('account:login')

@login_required
def home_page(request):
    return render(request,'account/home.html')


@login_required
@ordinary_user_required
def check_symptoms_view(request,pk=1):
    if request.method=='GET':
        '''
        if pk==1:
            form= SmokingForm()
            next=2
            previous=0
        elif pk==2:
            form=ExerciseForm()
            next = 3
            previous = 1
        elif pk==3:
            form=SymptomForm1()
            next = 4
            previous = 2
        elif pk==4:
            form=SymptomForm2()
            next = 5
            previous = 3
        elif pk==5:
            form=SymptomForm3()
            next = 0
            previous = 4
        else:
            form=SmokingForm()
            next = 2
            previous = 0 '''
        form1 = SmokingForm(prefix="form1")
        form2 = ExerciseForm(prefix="form2")
        form3 = SymptomForm1(prefix="form3")
        form4 = SymptomForm2(prefix="form4")
        form5 = SymptomForm3(prefix="form5")

       #symptoms_form=SymptomForm1()
        return render(request,'account/check_symptoms.html',{
            'form1':form1,
            'form2': form2,
            'form3': form3,
            'form4': form4,
            'form5': form5,


        })

    elif request.method == 'POST':

        form1 = SmokingForm(request.POST, prefix="form1")
        form2 = ExerciseForm(request.POST, prefix="form2")
        form3 = SymptomForm1(request.POST, prefix="form3")
        form4 = SymptomForm2(request.POST,prefix="form4")
        form5 = SymptomForm3(request.POST,prefix="form5")

        angina = False
        heart_attack = False
        dyspnea = False

        if form3.is_valid():
            if len(form3.cleaned_data['choices']) >= 4:
                angina = True

        if form4.is_valid():
            if len(form4.cleaned_data['choices']) >=4:
                heart_attack=True

        if form5.is_valid():
            if len(form4.cleaned_data['choices']) >=3:
                dyspnea=True

        return render(request, 'account/symptoms_result.html',{
            'angina':angina,
            'heart_attack':heart_attack,
            'dyspnea':dyspnea
        })




@login_required
@doctor_required
def save_data(request):
    if request.method=='GET':
        return render(request,'account/save_data.html')

@login_required
@doctor_required
def save_data(request):
    if request.method=='GET':
        data_from = SaveDataForm()
        return render(request, 'account/save_data.html', {
            'data_form': data_from
        })

    elif request.method=='POST':
        form=DataForm(request.POST)

        if form.is_valid():
            form.save()
        return render(request, 'account/save_data.html', {
            'message': "Data saved succesfully "
        })


@login_required
def analyze_data(request):
    if request.method =='GET':
        data_from=DataForm()
        return render(request,'account/analyze_data.html',{
            'data_form':data_from
        })

    elif request.method=='POST':
        filename=settings.STATIC_ROOT+'finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))

        data=DataForm(request.POST)
        new_data=data.save(commit=False)

        if new_data.sex=='M':
            sex=1
        else:
            sex=0
        #d=serializers.serialize('json',[new_data,])
        #return HttpResponse(d)

        list=[
            new_data.age,
            sex,
            new_data.cp,
            new_data.trestbps,
            new_data.chol,
            new_data.fbs,
            new_data.restecg,
            new_data.thalach,
            new_data.exang,
            new_data.oldpeak,
            new_data.slope,
            new_data.ca,
            new_data.thal,
        ]

        result=loaded_model.predict([np.array(list)])
        #result = loaded_model.predict([[63.0, 1.0, 1.0, 145.0, 233.0, 1.0, 2.0, 150.0, 0.0, 2.3, 3.0, 0.0, 6.0]])
        #result = loaded_model.predict([[67.0, 1.0, 4.0, 160.0, 286.0, 0.0, 2.0, 108.0, 1.0, 1.5, 2.0, 3.0, 3.0]])

        if result[0]==0:
            result=True
            #return HttpResponse('result no')
        elif result[0]==1:
            result=False
            #return HttpResponse('result yes')

        return render(request, 'account/analysis_result.html', {
                    'result': result
                })

