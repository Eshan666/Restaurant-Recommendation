from django.shortcuts import render,redirect
from restaurantapp.models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
import joblib


# Create your views here.
def home(request):
    return render(request,'restaurantapp/home.html')


def signInPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =  authenticate(request, username=username, password=password)
            

        if user is not None:
            login(request,user)
            messages.success(request,"Login Successful")
            return redirect('home')
        else:
            messages.info(request,"username or password is incorrect")
    return render(request,'restaurantapp/signIn.html')


def signUpPage(request):
    form =  CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form }
    return render(request,'restaurantapp/signUp.html',context)


def recommendationPage(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            searchValue = request.POST.get('search')
            context = {}
      
            if searchValue == 'burger':
                items = Burger.objects.all()
                list = True
            elif searchValue == 'pizza':
                items = Pizza.objects.all()
                list = True
            elif searchValue == 'sandwich':
                items = Sandwich.objects.all()
                list = True
            elif searchValue == 'pasta':
                items = Pasta.objects.all()
                list = True
            elif searchValue == 'biriyani':
                items = Biriyani.objects.all()
                list = True
            else:
                items = "Nothing to show.Please search for a different food"
                list = False


            context = {'items' : items,'list' : list}

            return render(request,'restaurantapp/recommendationPage.html',context)
            

        return render(request,'restaurantapp/recommendationPage.html')

    else:
        return redirect('signInPage')

    

def logOutPage(request):

    logout(request)
    return redirect('signInPage')



def ratingPredictorPage(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            context = {}
            price = request.POST.get('price')
            print(price)
        
            service = request.POST.get('service')
            print(service)
       
            pipeline = joblib.load('pipeline')
            model = joblib.load('model')
            prep_data = pipeline.transform([[price,service]])
            result = model.predict(prep_data)[0]
            result = round(result, 2)

            context = {'result' : result}
            return render(request,'restaurantapp/ratingPredictor.html',context)
        return render(request,'restaurantapp/ratingPredictor.html')

    else:
        
        return redirect('signInPage')

    