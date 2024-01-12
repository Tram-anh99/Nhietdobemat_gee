#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from flask import Flask, flash, request, redirect, url_for, make_response, jsonify,render_template
from werkzeug.utils import secure_filename
import json
import uuid
sys.path.append('func/')
from func import GEE_LST

app = Flask(__name__)

UPLOAD_lst_8 = './static/upload//'

OUTPUT_FOLDER = './static/output/'

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])

app = Flask(__name__)
app.config['UPLOAD_lst_8'] = UPLOAD_lst_8

@app.route('/')
def index():
    return 'hahahaha'


#http://flask.pocoo.org/docs/1.0/patterns/fileuploads/

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/lst/landsat8', methods=['GET', 'POST'])
def flower_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
            print('Khong co file')
        file = request.files['file']
        # return 'hahahah'
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            kq_temp=''
            kq_temp+='File: <a href="{}" target="_blank">Download</a>'
            kq_temp+='<br>'
            kq_temp+='<b>Logs</b><br>'
            kq_temp+='<pre>{}</pre>'

            # filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_extension = os.path.splitext(file.filename)[1]
            filename = secure_filename(uuid.uuid4().hex +  file_extension)
            file.save(os.path.join(app.config['UPLOAD_dbgh'], filename))
            # file.save('./static/upload/thuysan/tonghop_thiethaithuysan/hahaha22.xlsx')
            
            imgurl = app.config['UPLOAD_dbgh']+filename
            res = dbgh.trongtrot_dbgh_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./dbgh/dbgh_xl.html')
    return render_template('./dbgh/dbgh.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(host='0.0.0.0', port=1075)
    app.run(port=1075, debug=True)
    # app.run(port=1075)