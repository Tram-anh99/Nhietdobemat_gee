#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from flask import Flask, flash, request, redirect, url_for, make_response, jsonify,render_template
from werkzeug.utils import secure_filename
import json
import uuid
sys.path.append('func/')
from func import sanpham_lon
from func import sanpham_ga
from func import sanpham_vit
from func import sanpham_ngan
from func import sanpham_trau
from func import sanpham_bo
from func import hangnam_dongxuan_tpkt
from func import hangnam_hethu_tpkt
from func import hangnam_thudong_tpkt
from func import sanluong_thuysan
from func import lua_vumua
from func import lua_nam
from func import lua_dongxuan
from func import lua_hethu
from func import lua_thudong
from func import lua_mua_tinh
from func import hangnam_thang_tpkt
from func import cayhangnam_huyen_dongxuan
from func import cayhangnam_huyen_canam
from func import cayhangnam_huyen_hethu
from func import launam_thang_tpkt
from func import launam_huyen
from func import thanhphan_kt_chungtraubo
from func import tpkt_chunggiacam
from func import tdsx_huyen
from func import ntts_khongbe_uomnuoigiong
from func import ttnts_longbe_bebon
from func import uomnuoi_thuanduong_giongthuysan
from func import tonghop_thiethaithuysan
from func import trangtraichannuoi
from func import coso_nhayen
from func import dichhaicaytrong
from func import dbgh
app = Flask(__name__)

UPLOAD_SP_BO = './static/upload/channuoi/sanpham_bo/'
UPLOAD_SP_LON = './static/upload/channuoi/sanpham_lon/'
UPLOAD_SP_GA = './static/upload/channuoi/sanpham_ga/'
UPLOAD_SP_VIT = './static/upload/channuoi/sanpham_vit/'
UPLOAD_SP_NGAN = './static/upload/channuoi/sanpham_ngan/'
UPLOAD_SP_TRAU = './static/upload/channuoi/sanpham_trau/'
UPLOAD_hangnam_dongxuan_tpkt = './static/upload/trongtrot/hangnam_dongxuan_tpkt/'
UPLOAD_hangnam_hethu_tpkt = './static/upload/trongtrot/hangnam_hethu_tpkt/'
UPLOAD_hangnam_thudong_tpkt = './static/upload/trongtrot/hangnam_thudong_tpkt/'
UPLOAD_sanluong_thuysan= './static/upload/thuysan/sanluong_thuysan/'
UPLOAD_lua_vumua='./static/upload/trongtrot/lua_vumua/'
UPLOAD_lua_nam='./static/upload/trongtrot/lua_nam/'
UPLOAD_lua_dongxuan='./static/upload/trongtrot/lua_dongxuan/'
UPLOAD_lua_hethu='./static/upload/trongtrot/lua_hethu/'
UPLOAD_lua_thudong='./static/upload/trongtrot/lua_thudong/'
UPLOAD_lua_mua_tinh='./static/upload/trongtrot/lua_mua_tinh/'
UPLOAD_hangnam_thang_tpkt='./static/upload/trongtrot/hangnam_thang_tpkt/'
UPLOAD_cayhangnam_huyen_dongxuan='./static/upload/trongtrot/cayhangnam_huyen_dongxuan/'
UPLOAD_cayhangnam_huyen_canam='./static/upload/trongtrot/cayhangnam_huyen_canam/'
UPLOAD_cayhangnam_huyen_hethu='./static/upload/trongtrot/cayhangnam_huyen_hethu/'
UPLOAD_launam_thang_tpkt='./static/upload/trongtrot/launam_thang_tpkt/'
UPLOAD_launam_huyen='./static/upload/trongtrot/launam_huyen/'
UPLOAD_thanhphan_kt_chungtraubo='./static/upload/channuoi/thanhphan_kt_chungtraubo/'
UPLOAD_tpkt_chunggiacam='./static/upload/channuoi/tpkt_chunggiacam/'
UPLOAD_tdsx_huyen='./static/upload/trongtrot/tdsx_huyen/'
UPLOAD_ntts_khongbe_uomnuoigiong='./static/upload/thuysan/ntts_khongbe_uomnuoigiong/'
UPLOAD_ttnts_longbe_bebon='./static/upload/thuysan/ttnts_longbe_bebon/'
UPLOAD_uomnuoi_thuanduong_giongthuysan='./static/upload/thuysan/uomnuoi_thuanduong_giongthuysan/'
UPLOAD_tonghop_thiethaithuysan='./static/upload/thuysan/tonghop_thiethaithuysan/'
UPLOAD_trangtraichannuoi='./static/upload/channuoi/trangtraichannuoi/'
UPLOAD_coso_nhayen='./static/upload/channuoi/coso_nhayen/'
UPLOAD_dichbenhgayhai='./static/upload/trongtrot/dichbenhgayhai/'
UPLOAD_dbgh='./static/upload/trongtrot/dbgh/'

OUTPUT_FOLDER = './static/output/'

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])

app = Flask(__name__)
app.config['UPLOAD_BO'] = UPLOAD_SP_BO
app.config['UPLOAD_LON'] = UPLOAD_SP_LON
app.config['UPLOAD_GA'] = UPLOAD_SP_GA
app.config['UPLOAD_VIT'] = UPLOAD_SP_VIT
app.config['UPLOAD_NGAN'] = UPLOAD_SP_NGAN
app.config['UPLOAD_TRAU'] = UPLOAD_SP_TRAU
app.config['UPLOAD_hangnam_dongxuan_tpkt'] = UPLOAD_hangnam_dongxuan_tpkt
app.config ['UPLOAD_hangnam_hethu_tpkt'] = UPLOAD_hangnam_hethu_tpkt
app.config ['UPLOAD_hangnam_thudong_tpkt'] = UPLOAD_hangnam_thudong_tpkt
app.config['UPLOAD_sanluong_thuysan'] = UPLOAD_sanluong_thuysan
app.config['UPLOAD_lua_vumua']=UPLOAD_lua_vumua
app.config['UPLOAD_lua_nam']=UPLOAD_lua_nam
app.config['UPLOAD_lua_dongxuan']=UPLOAD_lua_dongxuan
app.config['UPLOAD_lua_hethu']=UPLOAD_lua_hethu
app.config['UPLOAD_lua_thudong']=UPLOAD_lua_thudong
app.config['UPLOAD_lua_mua_tinh']=UPLOAD_lua_mua_tinh
app.config['UPLOAD_hangnam_thang_tpkt']=UPLOAD_hangnam_thang_tpkt
app.config['UPLOAD_cayhangnam_huyen_dongxuan']=UPLOAD_cayhangnam_huyen_dongxuan
app.config['UPLOAD_cayhangnam_huyen_canam']=UPLOAD_cayhangnam_huyen_canam
app.config['UPLOAD_cayhangnam_huyen_hethu']=UPLOAD_cayhangnam_huyen_hethu
app.config['UPLOAD_launam_thang_tpkt']=UPLOAD_launam_thang_tpkt
app.config['UPLOAD_launam_huyen']=UPLOAD_launam_huyen
app.config['UPLOAD_thanhphan_kt_chungtraubo']=UPLOAD_thanhphan_kt_chungtraubo
app.config['UPLOAD_tpkt_chunggiacam']=UPLOAD_tpkt_chunggiacam
app.config['UPLOAD_tdsx_huyen']=UPLOAD_tdsx_huyen
app.config['UPLOAD_ntts_khongbe_uomnuoigiong']=UPLOAD_ntts_khongbe_uomnuoigiong
app.config['UPLOAD_ttnts_longbe_bebon']=UPLOAD_ttnts_longbe_bebon
app.config['UPLOAD_uomnuoi_thuanduong_giongthuysan']=UPLOAD_uomnuoi_thuanduong_giongthuysan
app.config['UPLOAD_tonghop_thiethaithuysan']=UPLOAD_tonghop_thiethaithuysan
app.config['UPLOAD_trangtraichannuoi']=UPLOAD_trangtraichannuoi
app.config['UPLOAD_coso_nhayen']=UPLOAD_coso_nhayen
app.config['UPLOAD_dichbenhgayhai']=UPLOAD_dichbenhgayhai
app.config['UPLOAD_dbgh']=UPLOAD_dbgh
@app.route('/')
def index():
    return 'hahahaha'


#http://flask.pocoo.org/docs/1.0/patterns/fileuploads/

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/longan/trongtrot_dbgh', methods=['GET', 'POST'])
def flower32_detection():
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