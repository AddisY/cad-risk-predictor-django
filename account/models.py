
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    is_doctor=models.BooleanField(default=False)
    is_ordinary_user=models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    yearsOfExperience=models.IntegerField()
    fieldOfStudy=models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    isApproved=models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

class OrdinaryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber=models.IntegerField()

    def __str__(self):
        return self.user.first_name

class Symptom(models.Model):
    symptomName=models.CharField(max_length=50)

    def __str__(self):
        return self.symptomName

class Data(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),

    )

    CHEST_PAIN_TYPE=(
        (1, 'typical angina'),
        (2, 'atypical angina'),
        (3,'non-anginal pain'),
         (4,'asymptomatic'),
    )
    FASTING_BLOOD_SUGER=(
        (1,'fasting blood sugar > 120 mg/dl'),
        (0,'fasting blood sugar < 120 mg/dl')
    )
    REST_ECG=(
        (0,'normal '),
        (1,'having ST-T wave abnormality'),
        (2,'showing probable '),
    )
    EXERCISE_INDUCED_ANGINA=(
        (1 , 'yes'),
        (0,'no'),
    )
    SLOPE=(
        (1,'upsloping'),
        (2, 'flat'),
        (3, 'downsloping'),
    )

    THAL=(
        (3,'normal'),
        (6,'fixed defect'),
        (7,'reversable defect')
    )

    age=models.IntegerField()
    sex=models.CharField(max_length=1,choices=SEX,default='M')
    cp=models.IntegerField(choices=CHEST_PAIN_TYPE,default=1,help_text='chest pain type')
    trestbps=models.DecimalField(decimal_places=2,max_digits=10,help_text='resting blood pressure (in mm Hg on admission to the hospital) ')#
    chol=models.DecimalField(decimal_places=2,max_digits=10,help_text='serum cholestoral in mg/dl')#
    fbs=models.IntegerField(choices=FASTING_BLOOD_SUGER,default=1)
    restecg=models.IntegerField(choices=REST_ECG,default=0,help_text='resting electrocardiographic results ')
    thalach=models.IntegerField(help_text='maximum heart rate achieved ')
    exang=models.IntegerField(choices=EXERCISE_INDUCED_ANGINA,default=1,help_text='exercise induced angina')
    oldpeak=models.IntegerField(help_text='ST depression induced by exercise relative to rest')  #
    slope=models.IntegerField(choices=SLOPE,default=1,help_text='the slope of the peak exercise ST segment ')
    ca=models.IntegerField(help_text='number of major vessels (0-3) colored by flourosopy')
    thal=models.IntegerField(choices=THAL,default=3,help_text='diagnosis of heart disease (angiographic disease status)')