"""
6, Apr 2013

Example bottle (python) RESTful web service.

This example provides a basic setup of a RESTful service

Notes
1. example should perform better content negotiation. A solution is
   to use minerender (https://github.com/martinblech/mimerender)
"""

import time
import sys
import socket

# bottle framework
from bottle import request, response, route, run, template

# moo
from classroom import Room

# virtual classroom implementation
room = None

def setup(base,conf_fn):
   print '\n**** service initialization ****\n'
   global room 
   room = Room(base,conf_fn)

#
# setup the configuration for our service
@route('/')
def root():
   print "--> root"
   return 'welcome'

#
#
@route('/user', method='POST')
def createUser():
    
    respdata=room.createUser(request.json)
    if respdata['resp_code']== 201 :
        status={"success":True,"id":respdata["id"]}
        response.status = 201
    else:
        status ={"success":False}
<<<<<<< HEAD
    response.status=result['resp_code']
=======
        response.status=respdata['resp_code']
>>>>>>> f608465376ced7f5dfb2f60b2abad838603017a2

    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/user/:emailid', method='GET')
def getUser(emailid):

    respdata=room.getUser(emailid)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return respdata

@route('/category',method= 'POST')
def add_category():
    status=None
    result=room.insert_category(request.json)
    if result['resp_code']== 201 :
        status={"success":True,"id":result["id"]}
    else:
        status ={"success":False}
    response.status=result['resp_code']

@route('/category/list',method='GET')
def list_category():
    retcode =200
    list=room.list_category()
    if list == None:
        retcode=500
        list={'success':False}
    else:
        retcode =200

    response.status=retcode
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return list


@route('/category/:name', method='GET')
def get_category(name):
    status=None
    result=room.get_category(name)

    if result == 404 : 
        response.status = 404
        status={"success":False}
    elif result == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return result

@route('/user/:emailid', method='DELETE')
def deleteUser(emailid):

    respdata=room.deleteUser(emailid)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/user/update/:emailid', method='PUT')
def updateUser(emailid):

    respdata=room.updateUser(request.json)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

@route('/course/enroll', method='PUT')
def enrollCourse():
 
    data = request.body.readline()
    data = data.split("?")
    email = data[0].split("=")[1]
    courseid = data[1].split("=")[1]
    respdata=room.enrollCourse(courseid,email)
    if respdata == 500 :
        response.status = 500
        status={"success":False}
    elif respdata == 400 :
        response.status = 400
        status={"success":False}
    elif respdata == 200 :
        response.status = 200
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status
    
    
@route('/course/drop', method='PUT')
def dropCourse():

    data = request.body.readline()
    data = data.split("?")
    email = data[0].split("=")[1]
    courseid = data[1].split("=")[1]
    print email
    print courseid
    respdata=room.dropCourse(courseid,email)
    if respdata == 500 :
        response.status = 500
        status={"success":False}
    elif respdata == 400 :
        response.status = 400
        status={"success":False}
    elif respdata == 200 :
        response.status = 200
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status



#
#
@route('/course', method='POST')
def addCourse():

    respdata=room.addCourse(request.json)
    if respdata['resp_code']== 201 :
        status={"success":True,"id":respdata["id"]}
    else:
        status ={"success":False}
        response.status=respdata['resp_code']

    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/course/:id', method='GET')
def getCourse(id):

    respdata=room.getCourse(id)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return respdata

#
#
@route('/course/update/:id', method='PUT')
def updateCourse(id):

    respdata=room.updateCourse(id,request.json)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/course/:id', method='DELETE')
def deleteCourse(id):

    respdata=room.deleteCourse(id)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/course/list', method='GET')
def listCourse():

    respdata=room.listCourse()

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return respdata

##Quiz collections

#
#
@route('/quizzes', method='POST')
def addQuiz():

    respdata=room.addQuiz(request.json)
    if respdata['resp_code']== 201 :
        status={"success":True,"id":respdata["id"]}
    else:
        status ={"success":False}
        response.status=respdata['resp_code']

    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/quiz/:id', method='GET')
def getQuiz(id):

    respdata=room.getQuiz(id)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return respdata

#
#
@route('/quiz/:id', method='DELETE')
def deleteQuiz(id):

    respdata=room.deleteQuiz(id)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/quiz/update/:id', method='PUT')
def updateQuiz(id):

    respdata=room.updateQuiz(id,request.json)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/quiz/list', method='GET')
def listQuiz():

    respdata=room.listQuiz()

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return respdata


##Announcement collections

#
#
@route('/announcements', method='POST')
def addAnnounce():

    respdata=room.addAnnounce(request.json)
    if respdata['resp_code']== 201 :
        status={"success":True,"id":respdata["id"]}
    else:
        status ={"success":False}
        response.status=respdata['resp_code']

    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/announcement/:id', method='GET')
def getAnnounce(id):

    respdata=room.getAnnounce(id)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return respdata

#
#
@route('/announcement/:id', method='DELETE')
def deleteAnnounce(id):

    respdata=room.deleteAnnounce(id)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/announcement/update/:id', method='PUT')
def updateAnnounce(id):

    respdata=room.updateAnnounce(id,request.json)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

#
#
@route('/announcement/list', method='GET')
def listAnnounce():

    respdata=room.listAnnounce()

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return respdata


##Category collections

@route('/category',method= 'POST')
def addCategory():

    respdata=room.insertCategory(request.json)
    if respdata['resp_code']== 201 :
        status={"success":True,"id":respdata["id"]}
    else:
        status ={"success":False}
    response.status=respdata['resp_code']
    
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return status

@route('/category/:name', method='GET')
def getCategory(name):

    respdata=room.getCategory(name)

    if respdata == 404 : 
        response.status = 404
        status={"success":False}
    elif respdata == 500 :
        response.status = 500
        status={"success":False}
    else :
        status={"success":True}
        
    fmt = __format(request)
    response.content_type = __response_format(fmt)
    return respdata



@route('/moo/ping', method='GET')
def ping():
   return 'ping %s - %s' % (socket.gethostname(),time.ctime())

#
# Development only: echo the configuration of the virtual classroom.
#
# Testing using curl:
# curl -i -H "Accept: application/json" http://localhost:8080/moo/conf
#
# WARN: This method should be disabled or password protected - dev only!
#
@route('/moo/conf', method='GET')
def conf():
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   return room.dump_conf(fmt)

#
# example of a RESTful method. This example is very basic, it does not 
# support much in the way of content negotiation.
#
@route('/moo/echo/:msg')
def echo(msg):
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   if fmt == Room.html:
      return '<h1>%s</h1>' % msg
   elif fmt == Room.json:
      rsp = {}
      rsp["msg"] = msg
      return json.dumps(all)
   else:
      return msg


#
# example of a RESTful query
#
@route('/moo/data/:name', method='GET')
def find(name):
   print '---> moo.find:',name
   return room.find(name)

#
# example adding data using forms
#
@route('/moo/data', method='POST')
def add():
   print '---> moo.add'

   # example list form values
   for k,v in request.forms.allitems():
      print "form:",k,"=",v

   name = request.forms.get('name')
   value = request.forms.get('value')
   return room.add(name,value)

#
# Determine the format to return data (does not support images)
#
# TODO method for Accept-Charset, Accept-Language, Accept-Encoding, 
# Accept-Datetime, etc should also exist
#
def __format(request):
   #for key in sorted(request.headers.iterkeys()):
   #   print "%s=%s" % (key, request.headers[key])

   types = request.headers.get("Accept",'')
   subtypes = types.split(",")
   for st in subtypes:
      sst = st.split(';')
      if sst[0] == "text/html":
         return Room.html
      elif sst[0] == "text/plain":
         return Room.text
      elif sst[0] == "application/json":
         return Room.json
      elif sst[0] == "*/*":
         return Room.json

      # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc

   # default
   return Room.html

#
# The content type on the reply
#
def __response_format(reqfmt):
      if reqfmt == Room.html:
         return "text/html"
      elif reqfmt == Room.text:
         return "text/plain"
      elif reqfmt == Room.json:
         return "application/json"
      else:
         return "*/*"
         
      # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc
