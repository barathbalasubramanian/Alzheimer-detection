# from ultralytics import YOLO
# from PIL import Image
# import cv2
# import io
# import requests , json
import numpy
import seaborn

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

            url = 'https://dokcer-api.onrender.com/upload'

            image_path = 'frontend\static\image\scan_image.png'  

            with open(image_path, 'rb') as image:
                files = {'fileUpload': image}
                response = requests.post(url, files=files)
                print(response.status_code)
                print(response.headers)

                if response.status_code == 200:
                    content_disposition = response.headers.get('Content-Disposition')
                    if content_disposition:
                        filename = content_disposition
                        print('Filename: ', filename)

                    with open('frontend\static\image\save1.png', 'wb') as f:
                        f.write(response.content)
                    print("File downloaded successfully")
                else:
                    print("Failed to download the file")

            img = [0]
            context = {
                'ref' : img,
                'detect': filename
            }
            return render(request, 'index.html' , context)

    return render(request, 'index.html')


# model = YOLO(r'models\weights.pt')
# im2 = cv2.imread(r"frontend\static\image\scan_image.png")
# results = model.predict(source=im2)
# print(results)
# print(results[0],'------')
# pre = results[0].boxes.cls.tolist()
# print(classes[int(pre[0])])
# cv2.imwrite('frontend\static\image\save.png',results.plot())