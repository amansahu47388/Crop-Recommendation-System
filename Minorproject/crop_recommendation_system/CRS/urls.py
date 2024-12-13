from django.contrib import admin
from django.urls import path
from CRS.views import *
app_name='CRS'

urlpatterns = [
    # path('',Landing,name='landing'),
    path('',Home,name='home'),

    # path('predction',Predict,name='predict'),
    # path('cyp',CropPredict,name='croppridict'),

    path('crop_recomend',Crop,name='crop_recomend'),
    path('crs',CropRecomend,name='croprecomend'),

    # path('fertilizier_recomend',Fertilizer,name='fertilizer_recomend'),
    # path('frs',FertilizerRecomend,name='fertilizerrecomend'),

    path('about', About,name='about'),
    path('contact', Contact,name='contact'),

    path('profile',Profile,name='profile'),
    path('profileupdate/<int:id>/', ProfileUpdate,name='profileupdate'),

    path('passwordupdate', PasswordUpdate , name='passwordupdate'),



    # Authentication 
    path('register', Register,name='register'),
    path('login', Login,name='login'),
    path('logout',Logout, name='logout'),
  
]

