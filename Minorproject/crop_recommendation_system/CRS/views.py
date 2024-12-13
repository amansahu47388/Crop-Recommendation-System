from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
import numpy as np
import pickle




# ====================== HOME PAGE =============================#
def Home(request):
    return render(request, 'home.html')







#======================= PREDICTION PAGE ========================#
def Predict(request):
    return render(request, 'production.html')


#====================== CROP PREDICT =========================== #
# Rfr = pickle.load(open('models/crop_production_Rfr.pkl','rb'))
# crop_production_encoder = pickle.load(open('models/crop_production_encoder.pkl','rb'))
# crop_producion_mx = pickle.load(open('models/crop_production_mx.pkl','rb'))


def CropPredict(request):
    # if request.method=='POST':
    #     State_name = (request.POST['state_name'])
    #     District_name = (request.POST['district_name'])
    #     Crop_year = int(request.POST['crop_year'])
    #     Season = (request.POST['season'])
    #     Crop = (request.POST['crop'])
    #     Area = float(request.POST['area'])
      

    #     # Create an array of the input features
    #     features = np.array([[ State_name, District_name,Crop_year, Crop, Season, Area]],dtype=object).astype(str)
    #     # Transform the features using the preprocessor

    #     transformed_features = crop_production_encoder.fit_transform(features)
    #     transformed_features = crop_producion_mx.fit_transform(transformed_features).reshape(1,-1)
    #     # Make the prediction
    #     predicted_yield = Rfr.predict(transformed_features.reshape(1,-1))
    #     result = predicted_yield[0]
    
    #     return render(request, 'prediction.html' , {'result': result})

    # else:
    #     pass
    pass













#=================== RECOMMENDATION PAGE =========================#
def Crop(request):
    return render(request, 'crop.html')


#====================== CROP RECOMMEND  ==========================#

crop_recommend_Lr = pickle.load(open('models/crop_recommend_Lr.pkl','rb'))

def CropRecomend(request):
    if request.method=='POST':
        N = int(request.POST['Nitrogen'])
        P = int(request.POST['Phosphorous'])
        K = int(request.POST['Potassium'])
        Temperature = float(request.POST['Temperature'])
        Humidity = float(request.POST['Humidity'])
        pH = float(request.POST['pH'])
        Rainfall = float(request.POST['Rainfall'])

        feature_list = [N,P,K,Temperature,Humidity,pH,Rainfall]
        # single_predict = np.array([feature_list]).reshape(-1,1)
        prediction = crop_recommend_Lr.predict([feature_list])

        crop_dict = {0:'apple', 1:'banana', 2:'blackgram', 3:'chickpea', 4:'coconut', 5:'coffee',
       6:'cotton', 7:'grapes', 8:'jute', 9:'kidneybeans', 10:'lentil', 11:'maize',
       12:'mango', 13:'mothbeans', 14:'mungbean', 15:'muskmelon', 16:'orange', 17:'papaya',
       18:'pigeonpeas', 19:'pomegranate', 20:'rice', 21:'watermelon'}

        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result ="{} is the best crop to be cultivated ".format(crop)
        else:
            result = "Sorry are not able to recommend a proper crop for this environment"

        return render(request, 'crop.html',{'result':result})
    else:
        pass

#============== CROP RECOMMENDATION PAGE END ================#







#=================== FERTILIZER PAGE =========================#
def Fertilizer(request):
    return render(request, 'fertilizer.html')


#====================== FERTILIZER RECOMMEND  ==========================#

# fertilizer_recommend = pickle.load(open('models/fertilizer.pkl','rb'))
# fertilizer_encoding = pickle.load(open('models/fertilizer_encode.pkl','rb'))

def FertilizerRecomend(request):
    # if request.method=='POST':
    #     Temparature = int(request.POST['temparature'])
    #     Humidity = int(request.POST['humidity'])
    #     Moisture = int(request.POST['moisture'])
    #     Soil_Type = request.POST['soil_type']
    #     Crop_Type = request.POST['crop_type']
    #     Nitrogen = int(request.POST['nitrogen'])
    #     Potassium = int(request.POST['potassium'])
    #     Phosphorous = int(request.POST['phosphorous'])

    #    # Create input array
    #     feature_list = np.array([[Temparature, Humidity, Moisture, Soil_Type,Crop_Type, Nitrogen, Potassium, Phosphorous]],dtype=object)

    #     # feature_list['Soil_Type'] = fertilizer_encoding.transform(feature_list['Soil_Type'])
    #     # feature_list['Crop_Type'] = fertilizer_encoding.transform(feature_list['Crop_Type'])

    #     feature_list = fertilizer_encoding.transform(feature_list)

    #     prediction = fertilizer_recommend.predict([feature_list]).reshape(1,-1)

    #     fertilizer_dict = {0:'10-10-10', 1:'10-26-26', 2:'14-14-14', 3:'14-35-14', 4:'15-15-15', 5:'17-17-17',
    #    6:'20-20', 7:'28-28', 8:'DAP', 9:'Potassium chloride', 10:'Potassium sulfate.', 11:'Superphosphate',
    #    12:'TSP', 13:'Urea'}

    #     if prediction[0] in fertilizer_dict:
    #         fertilizer = fertilizer_dict[prediction[0]]
    #         result ="{} is the best fertilizer to be cultivated ".format(fertilizer)
    #     else:
    #         result = "Sorry are not able to recommend a proper fertilizer for this environment"

    #     return render(request, 'fertilizer.html',{'result':result})
    # else:
        pass

#============== FERTILIZER RECOMMENDATION PAGE END ================#











#======================= About PAGE ===========================#
def About(request):
    return render(request, 'about.html')

 
 #==================== CONTACT PAGE START ========================#
def Contact(request):
    return render(request, 'contact.html')



 #==================== PASSWORD UPDATE  START =====================#


# User = get_user_model()  # Get your custom user model

def PasswordUpdate(request):
    # user = get_object_or_404(User, id=id)  # Get the user by ID

    # if request.method == 'POST':
    #     old_password = request.POST.get('old_password')
    #     new_password = request.POST.get('new_password')
    #     confirm_password = request.POST.get('confirm_password')

    #     # Check if the old password is correct
    #     if user.check_password(old_password):
    #         # Check if new password and confirm password match
    #         if new_password == confirm_password:
    #             user.set_password(new_password)  # Set and hash the new password
    #             user.save()  # Save the user with the new password
    #             return HttpResponse('Password changed successfully!')
    #         else:
    #             return HttpResponse('New password and confirm password do not match.')
    #     else:
    #         return HttpResponse('Old password is incorrect.')

    return render(request, 'password_update.html')







# ==================== PROFILE PAGE START =========================#

def Profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('/login')
    



#=================== PROFILE UPDATE ==============================#


 # Assuming you are using Django's default User model

def ProfileUpdate(request, id):
    user = get_object_or_404(User, id=id)  # Fetch the existing user object

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        image = request.FILES.get('image')  # Fetch image from request.FILES

        # Update user fields if provided in the form
        if fname:
            user.first_name = fname
        if lname:
            user.last_name = lname
        if phone:
            user.phone = phone
        if email:
            user.email = email
        if image:
            user.image = image 

        user.save()  
        messages.success(request,"Your Profile update Successfully")
        return redirect('/profile')

    return render(request, 'profile_update.html', {'user': user}) 







 
 #=========== REGISTER PAGE ===========================#
def Register(request):
    # check user is already register
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        fname = request.POST['fname'] 
        lname = request.POST['lname'] 
        phone = request.POST['phoneNumber']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        # gender = request.POST['gender']
       
        phone_check = User.objects.filter(phone=phone).exists()
        email_check = User.objects.filter(email=email).exists()


        if phone_check == True:
            messages.error(request,'Phone number already exists')
            return redirect('/register')

        elif email_check == True:
            messages.error(request,'Email already exists')
            return redirect('/register')
 
        elif len(phone) != 10:
            messages.error(request,'Number should be 10 Digit')
            return redirect('/register')
        
        elif password != confirm_password:
            messages.error(request,'Password & confirm password did not match.')
            return redirect('/register')

        else:
            user = User.objects.create_user(email=email,password=password,phone=phone)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request,"Your account successfully created")
            return redirect('/register')
            
    return render(request,'register.html')

#====================== REGISTRATION PAGE START +==================#
 









 
 #==================== LOGIN PAGE ===========================#
def Login(request):
    # check user is already login 
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST['email']
        password  = request.POST['password']

        user = authenticate(request,email=email,password=password)

        if user is not None:
            auth_login(request,user)
            messages.success(request,"Successfully Login")
            return redirect('/')

        else:
            messages.error(request,"Invalid Email & Password ")
            return redirect('/login')

    return render(request,'login.html')
  
#======================= LOGIN PAGE END =========================#



#=====================  LOGOUT PAGE START ======================#
def Logout(request):
    auth_logout(request)
    return render(request, 'home.html')