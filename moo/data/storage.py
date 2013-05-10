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
      respcode = 201
      try:
          query = {"email":jsondata["email"]}
          cnt = self.usercollection.find(query).count()
          if cnt == 0:
              obj_id = self.usercollection.insert(jsondata)
              obj_id = str(obj_id)
              
          else:
              respcode = 409
          return {"resp_code":respcode,"id":obj_id}
      except:
          print "Server Error"
          return {"resp_code":500,"id":obj_id}

    
              
         
       
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
