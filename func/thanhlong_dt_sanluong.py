# khai báo kết nối với database
from tkinter.font import names
from unicodedata import name
import sqlalchemy
from sqlalchemy import null, text
from sqlalchemy import create_engine
# import psycopg2
engine = create_engine('postgresql+psycopg2://postgres:TrungT%40mV13nTh%40m@s1.dothanhlong.org:10067/quanly_thanhlong')
import datetime
from datetime import datetime
import numpy as np
import pandas as pd
import os
import psycopg2
import random
import openpyxl
import calendar
import time

def import_dtsanluongthanhlong_process(imgurl):
      # Process files here
    wb = openpyxl.load_workbook(imgurl)
    #give the full path of the file here
    a=wb.sheetnames
    #đọc từng sheet trong file exccel
    for sheet in wb:
        print(sheet.title)

        # đọc file excel
        df = pd.read_excel(imgurl, sheet.title, index_col = 0)
        print(df)

         # Xuất ra file csv, excel
        df.to_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_1.csv')
        df.to_excel('./static/output/nonglamthuy/excel/'+ sheet.title +'_1.xlsx')

         # doc lại file csv vừa xuất
        df1 = pd.read_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_1.csv',index_col = 0,sep=',')

      #   #xoá dòng trống
      #   fw1=df1.drop(df1.index[[0,1]])
      #   print(fw1)
        print(df1)
        fw1=df1.drop(df1.index[[0,1]])
        print(fw1)

         #xuất file csv và excel sau khi xoá dòng trống
        fw1.to_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_2.csv')
        fw1.to_excel('./static/output/nonglamthuy/excel/'+ sheet.title +'_2.xlsx')


        #đọc lại file excel sau khi xoá dòng trống
        df2 = pd.read_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_2.csv',index_col = 0,header=None,sep=',')
        print(df2)

        #Chì lấy dl có giá trị
        df3 = df2[2:]
        print(df2[2:])

        #Xuất file csv excel sau khi lấy giá trị
        df3.to_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_3.csv')
        df3.to_excel('./static/output/nonglamthuy/excel/'+ sheet.title +'_3.xlsx')

        #đọc lại file sau khi lấy giá trị
        df4 = pd.read_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_3.csv',index_col = 0,header=0,sep=',')

         #đổi tên cột
        df5=df4.rename(columns={'1': 'tenhuyen','2': '2010','3':'2011','4':'2012','5':'2013','6':'2014','7':'2015','8':'2016','9':'2017','10':'2018','11':'2019','12':'2020','13':'2021'})
        df6=df5[2:]

         #xuất file excel csv sau khi doi ten cột
        df6.to_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_4.csv')
        df6.to_excel('./static/output/nonglamthuy/excel/'+ sheet.title +'_4.xlsx')

         #đọc lại file sau khi đổi tên cột
        df7 = pd.read_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_4.csv',index_col = 1,header=0,sep=',')
        print(df7)

        # Stack
        df8 =  df7.stack()

          #xuất file excel csv sau khi stack
        df8.to_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_5.csv')
        df8.to_excel('./static/output/nonglamthuy/excel/'+ sheet.title +'_5.xlsx')

        #đọc lại file sau khi stack
        df9 = pd.read_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_5.csv',header=None,sep=',')

        #Filter
        df10=df9[1:]

         #xuất file excel csv sau khi filter
        df10.to_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_6.csv')
        df10.to_excel('./static/output/nonglamthuy/excel/'+ sheet.title +'_6.xlsx')

        #đọc lại file sau khi fillter
        df11 = pd.read_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_6.csv',index_col = 0,header=0,sep=',')

        #đổi tên cột
        df12=df11.rename(columns={'0': 'tenhuyen','1': 'nam','2':'dt_sanluong'})

        #xuất file excel csv sau khi filter
        df12.to_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_7.csv')
        df12.to_excel('./static/output/nonglamthuy/excel/'+ sheet.title +'_7.xlsx')

        #đọc lại file sau khi cap nhật tên cột
        df13 = pd.read_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_6.csv',index_col = 0,header=0,sep=',')
       
        #đổi tên cột
        df14=df13.rename(columns={'0': 'tenhuyen','1': 'nam','2':'dt_sanluong'})
        #thêm cột
        df14['date'] = sheet.title
        df14['fdate'] =  df14['date'].map(str) + "-01-01" 
        df14['tdate'] =  None
        df14['edittime'] =  datetime.today().strftime('%Y-%m-%d')
        df14['editby'] = "Tramanh"
        # df13['id']=None
        df14['maso']=None
        df14["isvalid"] = "1"
        df14["ghichu"] =None
        df14["tenfile"]=imgurl
        df14['id_nguoi_upload']=None
        df14.pop('date')
        df14['nam'] = df14['nam'].astype(int)

      #   #xoá dòng có đk
      #   df13.drop(df13[df13['nam'] == '0'].index, inplace = True)
               
         #xuất file excel csv sau khi xoá dòng có đk
        df14.to_csv('./static/output/nonglamthuy/csv/'+ sheet.title +'_8.csv')
        df14.to_excel('./static/output/nonglamthuy/excel/'+ sheet.title +'_8.xlsx')
        #nhập dl vào database
        df14.to_sql(name='dt_sanluong_thanhlong',con=engine, schema = 'import_data',if_exists='append',index=False)
    sql = text('update import_data.dt_sanluong_thanhlong Set maso=MD5(id::text || RANDOM()::text || CURRENT_TIMESTAMP::text) where maso is Null ;')
    result = engine.execute(sql)

    logs = 'bla bla bla...'
    return [imgurl,logs]




