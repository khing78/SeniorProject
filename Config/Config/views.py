import pyrebase 
from django.http import HttpResponse
from django.shortcuts import render
config = {
    'apiKey': "AIzaSyBeronCsNPS_TdrgUPV-3nYK68PKnq0WMM",
    'authDomain': "cassava-8ae86.firebaseapp.com",
    'projectId': "cassava-8ae86",
    'storageBucket': "cassava-8ae86.appspot.com",
    'messagingSenderId': "672705670329",
    'appId': "1:672705670329:web:a38dfa7392ecef56dfff68",
    'measurementId': "G-TMZ7M1SJ9G"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
 
def home(request): 
    return render(request, "index.html")
 
def signin(request):
    return render(request, "signin.html")
 
 
def result(request):
    email = request.POST.get('email')
    password = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except:
        message = "invalid cerediantials"
        return render(request, "signin.html",{"msg":message})
    print(user)
    return render(request, "main.html",{"e":email})