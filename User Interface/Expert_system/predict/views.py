from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
import numpy as np
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


import joblib

reloadModel=joblib.load('Final_DT_model.sav')

import sys



from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client['mongodbVSCodePlaygroundDB']

collection = db['Expert_System']

symptoms={}
symptoms["Fever"] = 0.75
symptoms["Headache"] = 0.50
symptoms["Nausea"] = 0.25
symptoms["Vomiting"] = 0.25
symptoms["Jaundice"] = 0.75
symptoms["Enlarged_Liver"] = 0.00
symptoms["Joint_Pain"] = 0.50
symptoms["Body_Weakness"] = 0.25
symptoms["Dizziness"] = 0.75
symptoms["Loss_of_Appetite"] = 0.00
symptoms["Mp"] = 0.25

collection.insert_one(symptoms)

def index(request):
    symptoms={}
    symptoms["Fever"] = 0.75
    symptoms["Headache"] = 0.50
    symptoms["Nausea"] = 0.25
    symptoms["Vomiting"] = 0.25
    symptoms["Jaundice"] = 0.75
    symptoms["Enlarged_Liver"] = 0.00
    symptoms["Joint_Pain"] = 0.50
    symptoms["Body_Weakness"] = 0.25
    symptoms["Dizziness"] = 0.75
    symptoms["Loss_of_Appetite"] = 0.00
    symptoms["Mp"] = 0.25

    context = {'symptoms': symptoms}
    return render(request,'index.html',context)

def predictModel(request):
    context = {'a': 'Tears'}
    print(request)
    if request.method == "POST":
        Fever_symptom = request.POST.get('fever')
        headache_symptom =request.POST.get('headache')
        nausea_symptom = request.POST.get('nausea')
        vomiting_symptom= request.POST.get('vomiting')
        jaundice_symptom= request.POST.get('jaundice') 
        enlarged_Liver_symptom =request.POST.get('enlarged_Liver')
        joint_Pain_symptom = request.POST.get('joint_Pain')
        body_Weakness_symptom = request.POST.get('body_Weakness')
        dizziness_symptom = request.POST.get('dizziness')
        loss_of_Appetite_symptom = request.POST.get('loss_of_Appetite')
        mp_symptom = request.POST.get('mp')

        Fever_symptom = np.float64(Fever_symptom)
        headache_symptom = np.float64(headache_symptom)
        nausea_symptom= np.float64(nausea_symptom)
        vomiting_symptom = np.float64(vomiting_symptom)
        jaundice_symptom = np.float64(jaundice_symptom)
        enlarged_Liver_symptom = np.float64(enlarged_Liver_symptom)
        joint_Pain_symptom = np.float64(joint_Pain_symptom)
        body_Weakness_symptom= np.float64(body_Weakness_symptom)
        dizziness_symptom = np.float64(dizziness_symptom)
        loss_of_Appetite_symptom = np.float64(loss_of_Appetite_symptom)
        mp_symptom = np.float64(mp_symptom)
        
        diagnosis = reloadModel.predict([[Fever_symptom,headache_symptom,nausea_symptom,vomiting_symptom,jaundice_symptom,enlarged_Liver_symptom,joint_Pain_symptom,body_Weakness_symptom,dizziness_symptom,loss_of_Appetite_symptom,mp_symptom]])[0]
        context = {'diagnosis': diagnosis}
    return render(request,'index.html',context)

def viewDatabase(request):
    
    
    return render(request,'viewDB.html')

def updateDatabase(request):
    symptoms={}
    symptoms['Fever'] = request.POST.get('fever')
    symptoms['Headache'] =request.POST.get('headache')
    symptoms['Nausea'] = request.POST.get('nausea')
    symptoms['Vomiting']    = request.POST.get('vomiting')
    symptoms['Jaundice']    = request.POST.get('jaundice') 
    symptoms['Enlarged_liver']    =request.POST.get('enlarged_Liver')
    symptoms['Joint_Pain']    = request.POST.get('joint_Pain')
    symptoms['Body_Weakness']     = request.POST.get('body_Weakness')
    symptoms['Dizziness']     = request.POST.get('dizziness')
    symptoms['Loss_of_Appetite']     = request.POST.get('loss_of_Appetite')
    symptoms['Mp']     = request.POST.get('mp')
    
    data = collection.insert_one(symptoms)
    # database = pd.DataFrame.to_dict(data)
    # data = list(database['Expert_System.find()'])
    # context = {'data':data}
    return render(request,'viewDB.html')

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('Homepage')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'profile.html')


