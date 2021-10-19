from flask import Flask, render_template, request
import core.recognition as core
import json,os
import shutil
ALLOWED_EXTENSIONS = 'jpg'
app = Flask(__name__)
UPLOAD_FOLDER = '/static'

    

def allowed_file(filename):
    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def driver():
    r=[]  
    if request.method == 'GET':
            return render_template('upload.html')
    
    
    
    if request.method == 'POST':
        worker_id  = request.form.get('worker_id')
        if worker_id== '':
            return render_template('upload.html', msg='Не введен номер')

       
        
        if 'file' not in request.files:
            return render_template('upload.html', msg='Неподдреживемый файл')
       
       
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg='Ничего не отправлено') 
            
            
        t=core.id_check(worker_id)
        if  t==1:
            r=core.json_fun(3)
            with open('data.json', 'w') as outfile:
                json.dump(r, outfile, ensure_ascii=False)
            return render_template('upload.html', msg=r)
      
    
        file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))
        if file and allowed_file(file.filename):
            r=core.face_check(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))
            
            if (r==0):
                r=core.rec(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename),worker_id)
                r=core.json_fun(4,None,r)
                file.save(os.path.join(os.getcwd() + "/good", file.filename))
                with open('data.json', 'w') as outfile:
                    json.dump(r, outfile, ensure_ascii=False)
                return render_template('upload.html', msg=r)
            if (r==1):  
                file.save(os.path.join(os.getcwd() + "/bad", file.filename))
                r=core.json_fun(1,filename=file.filename)
                with open('data.json', 'w') as outfile:
                    json.dump(r, outfile, ensure_ascii=False)

                return render_template('upload.html', msg=r)
            if (r==2):
                file.save(os.path.join(os.getcwd() + "/bad", file.filename))
                r=core.json_fun(2,filename=file.filename)
                 
                with open('data.json', 'w') as outfile:
                    json.dump(r, outfile, ensure_ascii=False)
                return render_template('upload.html', msg=r)
                
  


if __name__ == '__main__':
    app.run(debug=True )