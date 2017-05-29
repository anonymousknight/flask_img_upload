import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/senthiran/imgflask/uploadedimage'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app = Flask(__name__)


	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      f.save(os.path.join('./uploadedimage', f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
