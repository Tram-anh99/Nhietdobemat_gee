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

@app.route('/longan/channuoi_sanphamlon', methods=['GET', 'POST'])
def flower_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
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
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
            file.save(os.path.join(app.config['UPLOAD_LON'], filename)) 

            imgurl = app.config['UPLOAD_LON']+filename
            res = sanpham_lon.channuoi_sanphamlon_process(imgurl)
            #return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./sanpham_lon/sp_lon_xl.html')
    return  render_template('./sanpham_lon/sp_lon.html')

@app.route('/longan/channuoi_sanphamga', methods=['GET', 'POST'])
def flower1_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
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
            file.save(os.path.join(app.config['UPLOAD_GA'], filename))

            imgurl = app.config['UPLOAD_GA']+filename
            res = sanpham_ga.channuoi_sanphamga_process(imgurl)
            #return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./sanpham_ga/sp_ga_xl.html')
    return render_template('./sanpham_ga/sp_ga.html')

@app.route('/longan/channuoi_sanphamvit', methods=['GET', 'POST'])
def flower2_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
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
            file.save(os.path.join(app.config['UPLOAD_VIT'], filename))

            imgurl = app.config['UPLOAD_VIT']+filename
            res = sanpham_vit.channuoi_sanphamvit_process(imgurl)
            #return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./sanpham_vit/sp_vit_xl.html')
    return render_template('./sanpham_vit/sp_vit.html')


@app.route('/longan/channuoi_sanphamngan', methods=['GET', 'POST'])
def flower3_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
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
            file.save(os.path.join(app.config['UPLOAD_NGAN'], filename))

            imgurl =app.config['UPLOAD_NGAN']+filename
            res = sanpham_ngan.channuoi_sanphamngan_process(imgurl)
            #return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./sanpham_ngan/sp_ngan_xl.html')
    return render_template('./sanpham_ngan/sp_ngan.html')

@app.route('/longan/channuoi_sanphamtrau', methods=['GET', 'POST'])
def flower4_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
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
            file.save(os.path.join(app.config['UPLOAD_TRAU'], filename))

            imgurl = app.config['UPLOAD_TRAU']+filename
            res = sanpham_trau.channuoi_sanphamtrau_process(imgurl)
            #return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./sanpham_trau/sp_trau_xl.html')
    return render_template('./sanpham_trau/sp_trau.html')

@app.route('/longan/channuoi_sanphambo', methods=['GET', 'POST'])
def flower5_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
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
            file.save(os.path.join(app.config['UPLOAD_BO'], filename))

            imgurl = app.config['UPLOAD_BO']+filename
            res = sanpham_bo.channuoi_sanphambo_process(imgurl)
            #return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./sanpham_bo/sp_bo_xl.html')
    return render_template('./sanpham_bo/sp_bo.html')

@app.route('/longan/trongtrot_hangnam_dongxuan_tpkt', methods=['GET', 'POST'])
def flower6_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
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
            file.save(os.path.join(app.config['UPLOAD_hangnam_dongxuan_tpkt'], filename))

            imgurl = app.config['UPLOAD_hangnam_dongxuan_tpkt']+filename
            res = hangnam_dongxuan_tpkt.trongtrot_hangnam_dongxuan_tpkt_process(imgurl)
            #return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./hangnam_dongxuan_tpkt/hangnam_dongxuan_tpkt_xl.html')
    return render_template('./hangnam_dongxuan_tpkt/hangnam_dongxuan_tpkt.html')


@app.route('/longan/trongtrot_hangnam_hethu_tpkt', methods=['GET', 'POST'])
def flower7_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
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
            file.save(os.path.join(app.config['UPLOAD_hangnam_hethu_tpkt'], filename))

            imgurl = app.config['UPLOAD_hangnam_hethu_tpkt']+filename
            res = hangnam_hethu_tpkt.trongtrot_hangnam_hethu_tpkt_process(imgurl)
            #return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./hangnam_hethu_tpkt/hangnam_hethu_tpkt_xl.html')
    return render_template('./hangnam_hethu_tpkt/hangnam_hethu_tpkt.html')

@app.route('/longan/trongtrot_hangnam_thudong_tpkt', methods=['GET', 'POST'])
def flower8_detection():
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
            file.save(os.path.join(app.config['UPLOAD_hangnam_thudong_tpkt'], filename))

            imgurl = app.config['UPLOAD_hangnam_thudong_tpkt']+filename
            res = hangnam_thudong_tpkt.trongtrot_hangnam_thudong_tpkt_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./hangnam_thudong_tpkt/hangnam_thudong_tpkt_xl.html')
    return render_template('./hangnam_thudong_tpkt/hangnam_thudong_tpkt.html')

@app.route('/longan/thuysan_sanluong_thuysan', methods=['GET', 'POST'])
def flower9_detection():
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
            file.save(os.path.join(app.config['UPLOAD_sanluong_thuysan'], filename))

            imgurl = app.config['UPLOAD_sanluong_thuysan']+filename
            res = sanluong_thuysan.thuysan_sanluong_thuysan_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./sanluong_thuysan/sanluong_thuysan_xl.html')
    return render_template('./sanluong_thuysan/sanluong_thuysan.html')

@app.route('/longan/trongtrot_lua_vumua', methods=['GET', 'POST'])
def flower10_detection():
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
            file.save(os.path.join(app.config['UPLOAD_lua_vumua'], filename))

            imgurl = app.config['UPLOAD_lua_vumua']+filename
            res = lua_vumua.trongtrot_lua_vumua_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./lua_vumua/lua_vumua_xl.html')
    return render_template('./lua_vumua/lua_vumua.html')

@app.route('/longan/trongtrot_lua_nam', methods=['GET', 'POST'])
def flower11_detection():
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
            file.save(os.path.join(app.config['UPLOAD_lua_nam'], filename))

            imgurl = app.config['UPLOAD_lua_nam']+filename
            res = lua_nam.trongtrot_lua_nam_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./lua_nam/lua_nam_xl.html')
    return render_template('./lua_nam/lua_nam.html')

@app.route('/longan/trongtrot_lua_dongxuan', methods=['GET', 'POST'])
def flower12_detection():
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
            file.save(os.path.join(app.config['UPLOAD_lua_dongxuan'], filename))

            imgurl = app.config['UPLOAD_lua_dongxuan']+filename
            res = lua_dongxuan.trongtrot_lua_dongxuan_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./lua_dongxuan/lua_dongxuan_xl.html')
    return render_template('./lua_dongxuan/lua_dongxuan.html')

@app.route('/longan/trongtrot_lua_hethu', methods=['GET', 'POST'])
def flower13_detection():
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
            file.save(os.path.join(app.config['UPLOAD_lua_hethu'], filename))

            imgurl = app.config['UPLOAD_lua_hethu']+filename
            res = lua_hethu.trongtrot_lua_hethu_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./lua_hethu/lua_hethu_xl.html')
    return render_template('./lua_hethu/lua_hethu.html')

@app.route('/longan/trongtrot_lua_thudong', methods=['GET', 'POST'])
def flower14_detection():
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
            file.save(os.path.join(app.config['UPLOAD_lua_thudong'], filename))

            imgurl = app.config['UPLOAD_lua_thudong']+filename
            res = lua_thudong.trongtrot_lua_thudong_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./lua_thudong/lua_thudong_xl.html')
    return render_template('./lua_thudong/lua_thudong.html')

@app.route('/longan/trongtrot_lua_mua_tinh', methods=['GET', 'POST'])
def flower15_detection():
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
            file.save(os.path.join(app.config['UPLOAD_lua_mua_tinh'], filename))

            imgurl = app.config['UPLOAD_lua_mua_tinh']+filename
            res = lua_mua_tinh.trongtrot_lua_mua_tinh_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./lua_mua_tinh/lua_mua_tinh_xl.html')
    return render_template('./lua_mua_tinh/lua_mua_tinh.html')

@app.route('/longan/trongtrot_hangnam_thang_tpkt', methods=['GET', 'POST'])
def flower16_detection():
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
            file.save(os.path.join(app.config['UPLOAD_hangnam_thang_tpkt'], filename))

            imgurl = app.config['UPLOAD_hangnam_thang_tpkt']+filename
            res = hangnam_thang_tpkt.trongtrot_hangnam_thang_tpkt_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./hangnam_thang_tpkt/hangnam_thang_tpkt_xl.html')
    return render_template('./hangnam_thang_tpkt/hangnam_thang_tpkt.html')

@app.route('/longan/trongtrot_cayhangnam_huyen_dongxuan', methods=['GET', 'POST'])
def flower17_detection():
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
            file.save(os.path.join(app.config['UPLOAD_cayhangnam_huyen_dongxuan'], filename))

            imgurl = app.config['UPLOAD_cayhangnam_huyen_dongxuan']+filename
            res = cayhangnam_huyen_dongxuan.trongtrot_cayhangnam_huyen_dongxuan_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./cayhangnam_huyen_dongxuan/cayhangnam_huyen_dongxuan_xl.html')
    return render_template('./cayhangnam_huyen_dongxuan/cayhangnam_huyen_dongxuan.html')

@app.route('/longan/trongtrot_cayhangnam_huyen_canam', methods=['GET', 'POST'])
def flower18_detection():
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
            file.save(os.path.join(app.config['UPLOAD_cayhangnam_huyen_canam'], filename))

            imgurl = app.config['UPLOAD_cayhangnam_huyen_canam']+filename
            res = cayhangnam_huyen_canam.trongtrot_cayhangnam_theohuyen_canam_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./cayhangnam_huyen_canam/cayhangnam_huyen_canam_xl.html')
    return render_template('./cayhangnam_huyen_canam/cayhangnam_huyen_canam.html')

@app.route('/longan/trongtrot_cayhangnam_huyen_hethu', methods=['GET', 'POST'])
def flower19_detection():
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
            file.save(os.path.join(app.config['UPLOAD_cayhangnam_huyen_hethu'], filename))

            imgurl = app.config['UPLOAD_cayhangnam_huyen_hethu']+filename
            res = cayhangnam_huyen_hethu.trongtrot_cayhangnam_huyen_hethu_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./cayhangnam_huyen_hethu/cayhangnam_huyen_hethu_xl.html')
    return render_template('./cayhangnam_huyen_hethu/cayhangnam_huyen_hethu.html')


@app.route('/longan/trongtrot_launam_thang_tpkt', methods=['GET', 'POST'])
def flower20_detection():
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
            file.save(os.path.join(app.config['UPLOAD_launam_thang_tpkt'], filename))

            imgurl = app.config['UPLOAD_launam_thang_tpkt']+filename
            res = launam_thang_tpkt.trongtrot_launam_thang_tpkt_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./launam_thang_tpkt/launam_thang_tpkt_xl.html')
    return render_template('./launam_thang_tpkt/launam_thang_tpkt.html')

@app.route('/longan/trongtrot_launam_huyen', methods=['GET', 'POST'])
def flower21_detection():
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
            file.save(os.path.join(app.config['UPLOAD_launam_huyen'], filename))

            imgurl = app.config['UPLOAD_launam_huyen']+filename
            res = launam_huyen.trongtrot_launam_huyen_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./launam_huyen/launam_huyen_xl.html')
    return render_template('./launam_huyen/launam_huyen.html')

@app.route('/longan/channuoi_thanhphan_kt_chungtraubo', methods=['GET', 'POST'])
def flower22_detection():
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
            file.save(os.path.join(app.config['UPLOAD_thanhphan_kt_chungtraubo'], filename))

            imgurl = app.config['UPLOAD_thanhphan_kt_chungtraubo']+filename
            res = thanhphan_kt_chungtraubo.channuoi_thanhphan_kt_chungtraubo_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./thanhphan_kt_chungtraubo/thanhphan_kt_chungtraubo_xl.html')
    return render_template('./thanhphan_kt_chungtraubo/thanhphan_kt_chungtraubo.html')

@app.route('/longan/channuoi_tpkt_chunggiacam', methods=['GET', 'POST'])
def flower23_detection():
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
            file.save(os.path.join(app.config['UPLOAD_tpkt_chunggiacam'], filename))

            imgurl = app.config['UPLOAD_tpkt_chunggiacam']+filename
            res = tpkt_chunggiacam.channuoi_tpkt_chunggiacam_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./tpkt_chunggiacam/tpkt_chunggiacam_xl.html')
    return render_template('./tpkt_chunggiacam/tpkt_chunggiacam.html')

@app.route('/longan/trongtrot_tdsx_huyen', methods=['GET', 'POST'])
def flower24_detection():
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
            file.save(os.path.join(app.config['UPLOAD_tdsx_huyen'], filename))

            imgurl = app.config['UPLOAD_tdsx_huyen']+filename
            res = tdsx_huyen.trongtrot_tdsx_huyen_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./tdsx_huyen/tdsx_huyen_xl.html')
    return render_template('./tdsx_huyen/tdsx_huyen.html')

@app.route('/longan/thuysan_ntts_khongbe_uomnuoigiong', methods=['GET', 'POST'])
def flower25_detection():
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
            file.save(os.path.join(app.config['UPLOAD_ntts_khongbe_uomnuoigiong'], filename))

            imgurl = app.config['UPLOAD_ntts_khongbe_uomnuoigiong']+filename
            res = ntts_khongbe_uomnuoigiong.thuysan_ntts_khongbe_uomnuoigiong_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./ntts_khongbe_uomnuoigiong/ntts_khongbe_uomnuoigiong_xl.html')
    return render_template('./ntts_khongbe_uomnuoigiong/ntts_khongbe_uomnuoigiong.html')


@app.route('/longan/thuysan_ttnts_longbe_bebon', methods=['GET', 'POST'])
def flower26_detection():
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
            file.save(os.path.join(app.config['UPLOAD_ttnts_longbe_bebon'], filename))
            imgurl = app.config['UPLOAD_ttnts_longbe_bebon']+filename
            res = ttnts_longbe_bebon.thuysan_ttnts_longbe_bebon_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./ttnts_longbe_bebon/ttnts_longbe_bebon_xl.html')
    return render_template('./ttnts_longbe_bebon/ttnts_longbe_bebon.html')

@app.route('/longan/thuysan_uomnuoi_thuanduong_giongthuysan', methods=['GET', 'POST'])
def flower27_detection():
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
            file.save(os.path.join(app.config['UPLOAD_uomnuoi_thuanduong_giongthuysan'], filename))

            imgurl = app.config['UPLOAD_uomnuoi_thuanduong_giongthuysan']+filename
            res = uomnuoi_thuanduong_giongthuysan.thuysan_uomnuoi_thuanduong_giongthuysan_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./uomnuoi_thuanduong_giongthuysan/uomnuoi_thuanduong_giongthuysan_xl.html')
    return render_template('./uomnuoi_thuanduong_giongthuysan/uomnuoi_thuanduong_giongthuysan.html')

@app.route('/longan/thuysan_tonghop_thiethaithuysan', methods=['GET', 'POST'])
def flower28_detection():
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
            file.save(os.path.join(app.config['UPLOAD_tonghop_thiethaithuysan'], filename))
            # file.save('./static/upload/thuysan/tonghop_thiethaithuysan/hahaha22.xlsx')
            
            imgurl = app.config['UPLOAD_tonghop_thiethaithuysan']+filename
            res = tonghop_thiethaithuysan.thuysan_tonghop_thiethaithuysan_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./tonghop_thiethaithuysan/tonghop_thiethaithuysan_xl.html')
    return render_template('./tonghop_thiethaithuysan/tonghop_thiethaithuysan.html')

@app.route('/longan/channuoi_trangtraichannuoi', methods=['GET', 'POST'])
def flower29_detection():
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
            file.save(os.path.join(app.config['UPLOAD_trangtraichannuoi'], filename))
            # file.save('./static/upload/thuysan/tonghop_thiethaithuysan/hahaha22.xlsx')
            
            imgurl = app.config['UPLOAD_trangtraichannuoi']+filename
            res = trangtraichannuoi.channuoi_trangtraichannuoi_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./trangtraichannuoi/trangtraichannuoi_xl.html')
    return render_template('./trangtraichannuoi/trangtraichannuoi.html')


@app.route('/longan/channuoi_coso_nhayen', methods=['GET', 'POST'])
def flower30_detection():
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
            file.save(os.path.join(app.config['UPLOAD_coso_nhayen'], filename))
            # file.save('./static/upload/thuysan/tonghop_thiethaithuysan/hahaha22.xlsx')
            
            imgurl = app.config['UPLOAD_coso_nhayen']+filename
            res = coso_nhayen.channuoi_coso_nhayen_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./coso_nhayen/coso_nhayen_xl.html')
    return render_template('./coso_nhayen/coso_nhayen.html')

@app.route('/longan/trongtrot_dichbenhgayhai', methods=['GET', 'POST'])
def flower31_detection():
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
            file.save(os.path.join(app.config['UPLOAD_dichbenhgayhai'], filename))
            # file.save('./static/upload/thuysan/tonghop_thiethaithuysan/hahaha22.xlsx')
            
            imgurl = app.config['UPLOAD_dichbenhgayhai']+filename
            res = dichhaicaytrong.trongtrot_dichbenhgayhai_process(imgurl)
            # return kq_temp.format(res[0],res[1])
            # return kq_temp.format(res[0],res[1])
            return render_template('./dichbenhgayhai/dichbenhgayhai_xl.html')
    return render_template('./dichbenhgayhai/dichbenhgayhai.html')


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