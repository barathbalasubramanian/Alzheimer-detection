from ultralytics import YOLO
from PIL import Image
import cv2
import io

from django.shortcuts import render

classes = ['MildDemented' , 'ModerateDemented' , 'NonDemented' ,'SevereDemented' , 'VeryMildDemented']

def index(request) :

    global classes

    if request.method == "POST" :
        if 'file' in request.POST :
            print('File ..')
            myfile = request.FILES['fileUpload']
            content = myfile.read()
            image = Image.open(io.BytesIO(content))
            image.save('frontend\static\image\scan_image.png')

            model = YOLO(r'models\weights.pt')
            im2 = cv2.imread(r"frontend\static\image\scan_image.png")
            results = model.predict(source=im2)
            pre = results[0].boxes.cls.tolist()
            print(classes[int(pre[0])])

            cv2.imwrite('frontend\static\image\save.png',results[0].plot())

            img = [0]
            context = {
                'ref' : img
            }
            return render(request, 'index.html' , context)

    return render(request, 'index.html')