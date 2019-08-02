import requests
import json
import common
from common import *
import sys
import logging
logging.captureWarnings(True)

#common.py is the container of all API endpoints
URIs = common.URI()

def rest_login_session():
    global URIs
    AuthURI = URIs["loginSessionURI"]
    url = AuthURI 
    json_body = {'authLoginDomain': '', 
                 'password': 'XXXXXXXX', 
                 'userName': 'XXXXXXXX', 
                 'loginMsgAck': 'true'}
    json_data = json.dumps(json_body)
    reqHeaders = {'Content-type':'application/json',
              'X-Api-Version':'200'}
    try:
        reqPost = requests.post(url=AuthURI,data=json_data,headers=reqHeaders,verify = False)
        #pprint.pprint(reqPost.json())
        #print "Session ID:"
       # print reqPost.json()
    except requests.exceptions.Timeout:
        print "Re-Try Again"
    except requests.exceptions.TooManyRedirects:
        print "Try with a different URL"
    except requests.exceptions.RequestException as e:
        print e 
        sys.exit(1)
    return reqPost.json()

if __name__ == '__main__':
    p1 = rest_login_session()
    # to be used in subsequent .py file or modules
