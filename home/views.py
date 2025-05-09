from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import sys
import os
import glob
import re
import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator


model_path=r"D:\Projects\projectsnake\snakebite\snakebite\model\project_gray_scale.h5"

model=keras.models.load_model(model_path)
import sqlite3

import numpy as np
import keras.utils as image


# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
import keras.utils as image

# Flask utils
from django.core.files.storage import FileSystemStorage
predication=0
from .models import Hospital
def homepage1(request):
    global predication
    predication="-1"
    return render(request,"home/snake1.html")
def aboutus(request):
    return render(request,'aboutus/about_us.html')
@csrf_exempt
def hospital_result(request):
        city=request.POST['city']
        hospitals = Hospital.objects.filter(city=city)
        return render(request,'hospital registration/city_selection.html',{'hosp':hospitals})
@csrf_exempt
def nearhospi(request):
    return render(request,'hospital registration/city_selection.html')
@csrf_exempt
def hospital_from(request):
        hospital_name = request.POST['hospital_name']
        city=request.POST['city']
        hospital_address = request.POST['hospital_address']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        antidotes = request.POST.getlist('antidote[]')
        cobra = True if 'cobra' in antidotes else False
        python = True if 'python' in antidotes else False
        russel = True if 'russel' in antidotes else False

        hospital = Hospital(
            hospital_name=hospital_name,
            city=city,
            hospital_address=hospital_address,
            phone_number=phone_number,
            email=email,
            cobra_antidote=cobra,
            python_antidote=python,
            russel_antidote=russel
        )

        hospital.save()

        #import sqlite3
        #c = sqlite3.connect('hospital.db')
        #cr = c.cursor()
        #cr.execute("INSERT INTO hospital VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
          # (hospital_name,city, hospital_address, phone_number, email, cobra, python, russel))
        #c.commit()
        #c.close()
        return render(request,"hospital registration/success.html")




@csrf_exempt
def hospregis(request):
    return render(request,"hospital registration/hospital_registration.html")
@csrf_exempt
def img(request):
    return render(request,"camera/c.html")
@csrf_exempt
def homepage(request):
    global predication
    predication="-1"
    return render(request, "home/snake.html")
@csrf_exempt
def pt(request):
    global predication
    if(predication=="0"):
        return render(request, "Professional Treatment/cobra.html")
    elif(predication=="1"):
        return render(request,"Professional Treatment/python.html")
    elif(predication=="2"):
        return render(request,"Professional Treatment/russel.html")
    a="Please First predict your snake"
    return render(request,"Error/invalidAcess.html",{"message":a})
@csrf_exempt
def firstaid(request):
    global predication
    if(predication=="0"):
        return render(request, "FirstAid/cobra.html")
    elif(predication=="1"):
        return render(request,"FirstAid/python.html")
    elif(predication=="2"):
        return render(request,"FirstAid/russel.html")
    a="Please First predict your snake"
    return render(request,"Error/invalidAcess.html",{"message":a})
@csrf_exempt
def about(request):
        global predication
        if(predication=="0"):
            return render(request, "about/cobra.html")
        elif(predication=="1"):
            return render(request,"about/python.html")
        elif(predication=="2"):
            return render(request,"about/russel.html")
        a="Please First predict your snake"
        return render(request,"Error/invalidAcess.html",{"message":a})



@csrf_exempt
def predict(request):
    global predication
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = "image.jpg"
        fs.delete(filename)
        filename = fs.save("image.jpg", uploaded_file)
        file_path = fs.path(filename)
        import cv2
        image = cv2.imread(file_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('gray.jpg', gray_image)
        file_path1 = fs.path('gray.jpg')
        file_path=convert(file_path1)
        preds = pred(file_path, model)
        predication=pred
        if preds == 0:
            predication="0"
            commom_name = "Cobra"
            scientific_name = "Naja naja"
            Type = "Venomous"
            Anti_Venome = "polyvalent antivenom"
            timing_takes_for_fatality = "30 minutes"
            return render(request, "home/snake1.html", {'cm':commom_name ,'sc':scientific_name,'type':Type,'av':Anti_Venome,'time':timing_takes_for_fatality})
        elif preds == 1:
            predication="1"
            commom_name = "Python"
            scientific_name = "Pythonidae"
            Type = "Non Venomous"
            Anti_Venome = "Not needed"
            timing_takes_for_fatality = "No death due to bite"
            return render(request, "home/snake1.html", {'cm':commom_name ,'sc':scientific_name,'type':Type,'av':Anti_Venome,'time':timing_takes_for_fatality})
        else:
            predication="2"
            commom_name = "Russel Viper"
            scientific_name = "Daboia russelii"
            Type = "Venomous"
            Anti_Venome = "Daboia antivenom"
            timing_takes_for_fatality = "1-14 days"
            return render(request, "home/snake1.html", {'cm':commom_name ,'sc':scientific_name,'type':Type,'av':Anti_Venome,'time':timing_takes_for_fatality})
        # Process your result for human
        # pred_class = preds.argmax(axis=-1)            # Simple argmax
        #pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
        #result = str(pred_class[0][0][1])               # Convert to string
        #return result
    #return None
@csrf_exempt
def pred(pred, model):
    test_image = image.load_img(pred, target_size=(150,150))
    test_image = image.img_to_array(test_image)/255
    test_image = np.expand_dims(test_image, axis=0)

    result = model.predict(test_image)
    predict = np.argmax(result)
    #print(result,"--->>",predict)

    return predict
@csrf_exempt
def convert(file_path):
    from keras_preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    img = load_img(file_path)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)

    # Create a directory to store the transformed image
    fs = FileSystemStorage()
    path = os.path.join('uploads', os.listdir('uploads')[0])
    filename = path
    fs.delete(filename)
    # Save the transformed images to the directory
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir='uploads',
                              save_prefix='1',
                              save_format='jpeg'):
        break


    path = os.path.join('uploads', os.listdir('uploads')[0])
    return path
@csrf_exempt
def remove_file_name(path):
    """
    Removes the filename from the end of a path and returns the directory.
    """
    dir_path, file_name = os.path.split(path)
