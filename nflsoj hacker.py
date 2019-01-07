'''
    NFLSOJ Hacker Python Edition
    By XGN from HHS
    and XGN from NFLS!
'''

import urllib.request
import io  
import sys  
import json

def getURL(url):
    print("访问开始:"+url)
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    html=response.read()
    return html.decode('utf-8')

#http://www.nfls.com.cn:10443/api/back/question?serial=6967
#http://www.nfls.com.cn:10443/api/questionList?pageNum=1&pageSize=999999&orderBy=serial&sequence=ASC&searchName=&searchTag=&sampleCount=null
#'http://www.nfls.com.cn:10443/api/back/questions/2732/answer'

try:
    pid=input("请输入题目ID:")

    print("请稍等...")

    res=json.loads(getURL("http://www.nfls.com.cn:10443/api/back/question?serial="+pid),encoding="utf-8")

    print("[1/2]",res["message"])

    id=res["data"]["id"]
    print("找到问题ID=",id)

    res=json.loads(getURL("http://www.nfls.com.cn:10443/api/back/questions/"+str(id)+"/answer"),encoding="utf-8")
    print("[2/2]",res["message"])

    print("所有题解如下：")
    cnt=1
    for i in res["data"]["solutions"]:
        print("编号:#",cnt,"提交ID=",i["id"],"用户=",i["User"]["nickName"],i["User"]["username"],"得分=",i["score"])
        cnt+=1

    print("*"*20)
except TypeError:
    print("出现了TypeError!可能是题目不存在之类的问题")
    exit(1)

while True:
    
    try:
        sid=int(input("请输入需要查看的题解编号(按下Ctrl+C结束程序)："))
        
        sid-=1
    
        res2=json.loads(getURL("http://www.nfls.com.cn:10443/api/back/solution/"+str(res["data"]["solutions"][sid]["id"])),encoding="utf-8")
        print("[EX]",res2["message"])
        print("程序如下：",res2["data"]["codeRecord"],sep="\n")
    except IndexError:
        print("输入的数字不正确")
    except ValueError:
        print("输入的不是正常人该输入的数字")
    
