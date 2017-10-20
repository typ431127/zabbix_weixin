#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# zabbix notification confirmation script
# Author:   typ431127@gmail.com
# My blog https://www.aityp.com


import requests
import json
import time
import os
import sys


Toparty="2"   #部门id
CropID='xxxxx'
Secret='xxxxx'

Gtoken="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+ CropID + "&corpsecret=" + Secret
Purl="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="
headers = {'Content-Type': 'application/json'}
Time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def _log(info):
    #注意权限,否则写不进去日志
    file = "/tmp/weixin_zabbix.log"
    if os.path.isfile(file) == False:
               f = open(file, 'a+')

    f = open(file,'a+')
    f.write(info)
    f.close()

def msg(user,msg,token):
     weixin_msg = {
         "touser" : user,
         "toparty" : "PartyID1 | PartyID2",
         "totag" : "TagID1 | TagID2",
         "msgtype" : "textcard",
         "agentid" : 1,
         "textcard" : {
             "title" : "报警确认通知",
             "description" : msg,
             "url" : "URL",
             "btntxt":"更多"
          }
      }
     push = requests.post(Purl + token,data=json.dumps(weixin_msg),headers=headers)
     code = json.loads(push.content.decode())
     if code["errcode"] == 0:
         _log(Time + ":消息发送成功\n")
     else:
         _log(Time + ":消息发送失败" + r.content.decode("utf-8") + "\n")

if __name__ == '__main__':
    text = sys.argv[3]
    user = sys.argv[1]
    r = requests.get(Gtoken)
    json_data = json.loads(r.content.decode())
    token = json_data["access_token"]
    msg(user,text,token)
