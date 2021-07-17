from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),    
    path('signInPage/',views.signInPage,name="signInPage"),    
    path('signUpPage/',views.signUpPage,name="signUpPage"),    
    path('logOutPage/',views.logOutPage,name="logOutPage"),    
    path('recommendationPage/',views.recommendationPage,name="recommendationPage"),
    path('ratingPredictorPage/',views.ratingPredictorPage,name="ratingPredictorPage"),

]
