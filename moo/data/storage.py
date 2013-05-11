"""
Storage interface
"""

import time
from pymongo import Connection

class Storage(object):
 
   def __init__(self):
      # initialize our storage, data is a placeholder
      connection = Connection()              
      db = connection['moocdb']
      self.usercollection = db['usercollection']
      # self.data = {}
      # for demo
      # self.data['created'] = time.ctime()

   def insert_user(self, jsondata):
      print "---> insert:user", jsondata
      try:
          query = {"email":jsondata["email"]}
          cnt = self.usercollection.find(query).count()
          if cnt == 0:
              obj_id = self.usercollection.insert(jsondata)
              obj_id = str(obj_id) 
              respcode = 201     
          else:
              respcode = 409
              userdetails = self.usercollection.find(query)
              obj_id = userdetails["_id"]
              obj_id= str(obj_id)
          return {"resp_code":respcode,"id":obj_id}
      except:
          print "Server Error"
          return {"resp_code":500,"id":obj_id}

   def get_user(self, emailid):
      print "---> get:user", emailid
      try:
          query = {"email":emailid}
          cnt = self.usercollection.find(query).count()
          if cnt == 0:
              return {"resp_code":404}    
          else:
              userdetail = self.usercollection.find(query)
              reponse = {"email": userdetail["email"],"own": userdetail["own"],"enrolled": userdetail["enrolled"],"quizzes": userdetail["quizzes"]}
              return response
      except:
          print "Server Error"
          return {"resp_code":500}

       
   def remove(self, name):
      print "---> remove:", name

   def names(self):
      print "---> names:"
      for k in self.data.iterkeys():
        print 'key:', k

   def find(self, name):
      print "---> storage.find:", name
      if name in self.data:
         rtn = self.data[name]
         print "---> storage.find: got value", rtn
         return rtn
      else:
         return None
