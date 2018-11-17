import pickle

import numpy as np
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from account.forms import UserForm, DoctorForm
from finalfinalproject import settings
from .serializers import SymptomSerializer, DoctorSerializer, OrdinaryUserSerializer, DataSerializer
from account.models import Symptom, Doctor, OrdinaryUser, Data


# Create your views here.


#@permission_classes([permissions.IsAuthenticated, ])
class SymptomsView(generics.ListAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    model = Symptom


class DoctorSignupView(generics.CreateAPIView):
    serializer_class = DoctorSerializer
    model = Doctor

class OrdinaryUserView(generics.CreateAPIView):
    serializer_class = OrdinaryUserSerializer
    model=OrdinaryUser

@api_view([ 'POST'])
def analyse_data(request):
    '''
    if request.method =='GET':
        snippets = Data.objects.all()
        serializer = DataSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
'''
    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = DataSerializer(data=data)

        if serializer.is_valid():
            new_data=serializer.save()
            #new_data=serializer.data

            if new_data.sex == 'M':
                sex = 1
            else:
                sex = 0

            list = [
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

            filename = settings.STATIC_ROOT + 'finalized_model.sav'
            loaded_model = pickle.load(open(filename, 'rb'))
            result = loaded_model.predict([np.array(list)])

            if result[0] == 0:
                return Response(
                    {
                        "result":True,
                        "message":"Based on the given data the probablilty of having CAD is high"
                     }
                )
            elif result[0] == 1:
                return Response(
                    {
                        "result": False
                        ,
                        "message": "Based on the given data the probablilty of having CAD is low "

                    }
                )

        return Response({"message": "Error",})


class TestDataView(generics.CreateAPIView):
    serializer_class = DataSerializer
    model=Data
