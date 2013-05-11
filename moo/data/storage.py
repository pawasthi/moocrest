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
      self.categorycollection=db['categorycollection']
      # self.data = {}
      # for demo
      # self.data['created'] = time.ctime()

   def create_user(self, jsondata):
      print "---> create:user", jsondata
      try:
          cnt = self.usercollection.find({"email":jsondata["email"]}).count()
          if cnt == 0:
              obj_id = self.usercollection.insert(jsondata)
              obj_id = str(obj_id) 
              respcode = 201     
          else:
              userdetails = self.usercollection.find({"email":jsondata["email"]})
              obj_id = userdetails["_id"]
              obj_id= str(obj_id)
              respcode = 409
          return {"resp_code":respcode,"id":obj_id}
      except:
          print "Server Error"
          return 500

   def get_user(self, emailid):
      print "---> get:user", emailid
      try:
          cnt = self.usercollection.find({"email":emailid}).count()
          if cnt == 0:
              return 404   
          else:
              for c in self.usercollection.find({"email":emailid}):
                  return {"email": c["email"],"own": c["own"],"enrolled": c["enrolled"],"quizzes": c["quizzes"]}
      except:
          print "Server Error"
          return 500

   def delete_user(self, emailid):
      print "---> delete:user", emailid
      try:
          cnt = self.usercollection.find({"email":emailid}).count()
          if cnt == 0:
              return 404   
          else:
              self.usercollection.remove({"email":emailid})     
              return 200 
      except:
          print "Server Error"
          return 500

   def update_user(self, jsondata):
      print "---> update:user", jsondata
      try:
          cnt = self.usercollection.find({"email":jsondata["email"]}).count()
          if cnt == 0:
              obj_id = self.usercollection.update(jsondata)
              obj_id = str(obj_id) 
              respcode = 201     
          else:
              userdetails = self.usercollection.find({"email":jsondata["email"]})
              obj_id = userdetails["_id"]
              obj_id= str(obj_id)
              respcode = 409
          return {"resp_code":respcode,"id":obj_id}
      except:
          print "Server Error"
          return {"resp_code":500,"id":obj_id}

   def enroll_course(self, courseid, email):
      try:
         cnt = self.usercollection.find({"email":email}).count()
         print "courseid",courseid
         print "email", email
         print "cnt",cnt
         if cnt == 0:
             return 400     
         else:
             self.usercollection.update({"email":email}, 
                                        {'$push': {'enrolled': courseid}}
                                        )
         return 200
      except:
         print "Server Error"
         return 500


   def drop_course(self, courseid, email):
      try:
         cnt = self.usercollection.find({"email":email}).count()
         print "courseid",courseid
         print "email", email
         print "cnt",cnt
         if cnt == 0:
             return 400     
         else:
             self.usercollection.update({"email":email}, 
                                        {"$pull": {"enrolled": courseid}}
                                        )
         return 200
      except:
         print "Server Error"
         return 500
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
     
   def insert_category(self,category):
        print "---> create:category", category
        query={"name":category["name"]}
        try:
           cnt=self.categorycollection.find(query).count()  
           if cnt==0:
               obj_id = self.categorycollection.insert(category)
               obj_id = str(obj_id)
               respcode=201
           else: 
               categorydetails=self.categorycollection.find(query) 
               obj_id = str(obj_id)
               respcode=409
           return {"resp_code":respcode,"id":obj_id} 
        except:
            print "Server Error"
            return {"resp_code":500,"id":obj_id}
        query={"name":category[""]}
   
   def get_cateogory(self,category):
       print "---> get category", category
        
       
