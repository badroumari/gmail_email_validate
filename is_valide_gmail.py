import requests
import random
import time
from time import sleep
from email.header import Header
from requests.structures import CaseInsensitiveDict


#contact the admin on ing.badr01@gmail.com to the the last and working version
def check_gmail(mail):

    mail = mail.split("@")[0]
    #input(mail)
    url = "https://accounts.google.com/_/lookup/accountlookup?hl=fr&_reqid=580148&rt=a"

    headers = CaseInsensitiveDict()
    headers["authority"] = "accounts.google.com"
    headers["x-same-domain"] = "1"
    headers["content-type"] = "application/x-www-form-urlencoded;charset=UTF-8"
    headers["google-accounts-xsrf"] = "1"
    headers["sec-ch-ua-mobile"] = "?0"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    headers["accept"] = "/"
    headers["origin"] = "https://accounts.google.com"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-dest"] = "empty"
    headers["referer"] = "https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    headers["accept-language"] = "fr"
    headers["cookie"] = "NID=511=d0lEFX-Kb6cDa5g1ntTqKDv4-nlYCkdWSRYA6411P5RXA1KtwG6LzRtXh2a2A_lay3gMcFqkTu7Vg9GbaH2Ex3tCAXLN5tKIm0k5q-1ze1e5kKpyQi9L1RTSlBbnGWk4bepY1khHrRJOK-7HSlrruwWDzfv3GIp5jKVUxMQtOkY; __Host-GAPS=1:T1zmaRoWY0ggl24Fn9xJYQOw0eDB7Q:eyRyMdok-GXfviW7"

    data="" #contact the admin on ing.badr01@gmail.com to the the last and working version

    resp = requests.post(url, headers=headers, data=data)

    #print(resp.status_code)
    #input(str(resp.text))
    if("google" in str(resp.text)):
       return 1
    else:
       return 0  