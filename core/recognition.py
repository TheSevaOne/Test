from deepface import DeepFace
import os
import cv2 as c
import glob   

def rec(image,id):
      result = DeepFace.verify(image, "database/"+str(id)+".jpg" ,detector_backend = "mtcnn")
     
      return result



def json_fun(status,filename,*deepface):
    if status==1:
        msg= {
    "info": {
        "error": "yes",
        "status": "больше одного лица в кадре",
        "path": str(os.getcwd() + "/bad/"+ filename)
    }
}
        return msg 
    if status == 2:

        msg= {
    "info": {
        "error": "yes",
        "status": "«нет лиц в кадре»",
        "path": str(os.getcwd() + "/bad/"+ filename)
    }
}
        return msg

    if status == 3:

        msg= {
    "info": {
        "error": "yes",
        "status": "«идентификационный номер отсутствует в БД»",
        "path": str(os.getcwd() + "/bad/"+ filename)
    }
}
        return msg
    
    if status == 4:    
        deepface
        return deepface
    
    

def face_check(image):
    print(image)
    image= c.imread(str(image))
    image=c.cvtColor(image, c.COLOR_BGR2GRAY)
    har = c.CascadeClassifier(os.getcwd()+"/core/haarcascade_frontalface_default.xml")
    faces = har.detectMultiScale(image,scaleFactor=1.2,minNeighbors=5)
    if len(faces)==1:
        return int(0)
    if len(faces)>1:
        return int(1)
    if len (faces)==0:
        return int(2)

   

def id_check(id):
    l=[]
    list = os.listdir('database')
    for f in list:
        f_name =os.path.splitext(f)[0]
        l.append(f_name)
        print(f_name)
    exists = str(id) in str(l) 
    print(l)
    if exists==False: 
        return int(1)
    else:
        return int(0)

        

