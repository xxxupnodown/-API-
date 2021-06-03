import requests
import base64
import json
import cv2
import datetime
import image
import pandas
from mysqldb import *
from com import *
# from err import *

def 识别(cap):
    ret, frame = cap.read()
    if ret:
        name = str(datetime.datetime.now()).replace('.','').replace(':','-')
        cv2.imwrite('./images/' + name + r".jpg", frame)
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = ''
        response = requests.get(host)
        if response:
            request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient"
            # request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal" #动物
            f = open('./images/'+ name +'.jpg', 'rb')
            img = base64.b64encode(f.read())

            params = {"image":img, "top_num": 2}
            access_token = response.json()['access_token']
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            newresponse = requests.post(request_url, data=params, headers=headers)
            if newresponse:
                return newresponse.json()
    '''
                for item in newresponse.json()['result']:
                    if item['score'] > 0.6:
                        if item['name'] != '非果蔬食材':
                            return item['name']
                    else:
                        return "识别失败！"
'''

def 启动相机():
    cap = cv2.VideoCapture(1)
    return cap

def kaishi(cap, Log,ser, Weight, LogCost, LogSolo):
    # 初始化
    Log.insert('insert','nmd ,dsb')
    Log.edit_undo()
    Weight.insert('insert','nmd ,dsb')
    Weight.edit_undo()
    LogCost.insert('insert','nmd ,dsb')
    LogCost.edit_undo()
    LogSolo.insert('insert','nmd ,dsb')
    LogSolo.edit_undo()
    
    result = 识别(cap)
    # if result['result'][0]['score'] > 0.6:
    
    cost = 获取单价(result['result'][0]['name'])
    if (cost == '无菜品') :
        # showErr(result['result'][0]['name'])
        print(result)
        return
    # 读取串口数据
    print(result)
    ser.flushInput() # 清除输入缓冲区数据
    data = getData(ser)
    allCost = (int(data) / 500) * float(cost)
    log = result['result'][0]['name'] + ',总价：' + str(round(allCost,2)) + '￥' + '\n单价：' + cost 
    
    Log.insert('insert',result['result'][0]['name'])
    Weight.insert('insert',str(round(int(data) / 1000, 2)) + 'kg')
    LogCost.insert('insert',str(round(allCost,2)) + '￥')
    LogSolo.insert('insert',str(cost) + '￥')
    print(data)
    添加记录(result['result'][0]['name'], data)
    '''result = { 'result' : [
    {'test': 123, 'name': 'test'},{ 'test': 456, 'name': 'why'}
    ]}'''
    # datatostr(result)
            
def datatostr(result):
    sr = pandas.Series(result)
    print(sr)
