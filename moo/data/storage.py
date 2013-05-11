"""
Storage interface
"""

import time
from pymongo import Connection
from bson.objectid import ObjectId

class Storage(object):
 
   def __init__(self):
      # initialize our storage, data is a placeholder
      connection = Connection()              
      db = connection['moocdb']
      self.usercollection = db['usercollection']
      self.categorycollection=db['categorycollection']
      self.coursecollection=db['coursecollection']
      self.quizcollection=db['quizcollection']
      self.announcecollection=db['announcementcollection']
      # self.data = {}
      # for demo
      # self.data['created'] = time.ctime()

##User Collections
   def create_user(self, jsondata):
      print "---> create:user", jsondata
      try:
          cnt = self.usercollection.find({"email":jsondata["email"]}).count()
          #print cnt
          if cnt == 0:
              obj_id = self.usercollection.insert(jsondata)
              obj_id = str(obj_id) 
              respcode = 201     
              return {"resp_code":respcode,"id":obj_id}
          else:
              userdetails = self.usercollection.find({"email":jsondata["email"]})
              #print userdetails
              #obj_id = userdetails["_id"]
              #obj_id= str(obj_id)
              respcode = 409
              return {"resp_code":respcode}
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
              for user in self.usercollection.find({"email":emailid}):
                  return {"email": user["email"],"own": user["own"],"enrolled": user["enrolled"],"quizzes": user["quizzes"]}
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
          print "cnt" , cnt
          if cnt == 0:
              return 201     
          else:
              self.usercollection.update({"email": jsondata["email"]}, jsondata)
              return 200
      except:
          print "Server Error"
          return 500

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

##Course collections

   def add_course(self, jsondata):
      print "---> add_course:", jsondata
      try:
          obj_id = self.coursecollection.insert(jsondata)
          obj_id = str(obj_id) 
          respcode = 201     
          return {"resp_code":respcode,"id":obj_id}
      
      except:
          print "Server Error"
          return 500


   def get_course(self,id):
      print "---> get:course", id
      try:    
          id = ObjectId(id)
          #print id
          cnt = self.coursecollection.find({"_id":id}).count()
          #print "cnt", cnt
          if cnt == 0:
              return 404   
          else:
              for course in self.coursecollection.find({"_id":id}):
                  print course["category"]
                  return {"id":str(id),"category":course["category"],"title":course["title"],"section":course["section"],
                          "dept":course["dept"],"term":course["term"],"year":course["year"],"instructor":course["instructor"],
                          "days":course["days"],"hours":course["hours"],"Description":course["Description"],
                          "attachment":course["attachment"],"version":course["version"]}
      except:
          print "Server Error"
          return 500
      
   def update_course(self,courseid,jsondata):
      print "---> update:course", jsondata
      try:
          id = ObjectId(courseid)
          print id
          cnt = self.coursecollection.find({"_id":id}).count()
          print "cnt" , cnt
          if cnt == 0:
              return 201     
          else:
              self.coursecollection.update({"_id":id}, jsondata)
              return 200
      except:
          print "Server Error"
          return 500

   def delete_course(self, courseid):
      print "---> delete:course", courseid
      try:
          id = ObjectId(courseid)
          print id
          cnt = self.coursecollection.find({"_id":id}).count()
          if cnt == 0:
              return 404   
          else:
              self.coursecollection.remove({"_id":id})     
              return 200 
      except:
          print "Server Error"
          return 500

   def list_course(self):
      print "---> list:course"
      try:    
          courselist = []
          for course in self.coursecollection.find():
               course["_id"] = str(course["_id"])
               courselist.append(course)
          
          return { "success" : True, "list" : courselist };
      
      except:
          print "Server Error"
          return 500

##Quiz collection

   def add_quiz(self, jsondata):
      print "---> add_quiz:", jsondata
      try:
          obj_id = self.quizcollection.insert(jsondata)
          obj_id = str(obj_id) 
          respcode = 201     
          return {"resp_code":respcode,"id":obj_id}
      
      except:
          print "Server Error"
          return 500

   def get_quiz(self,id):
      print "---> get:course", id
      try:    
          id = ObjectId(id)
          #print id
          cnt = self.quizcollection.find({"_id":id}).count()
          #print "cnt", cnt
          if cnt == 0:
              return 404   
          else:
              for quiz in self.quizcollection.find({"_id":id}):
                  return {"id": str(id),"courseId": quiz["courseId"],"questions": quiz["questions"]}
      except:
          print "Server Error"
          return 500

   def update_quiz(self,quizid,jsondata):
      print "---> update:quiz", jsondata
      try:
          id = ObjectId(quizid)
          print id
          cnt = self.quizcollection.find({"_id":id}).count()
          print "cnt" , cnt
          if cnt == 0:
              return 201     
          else:
              self.quizcollection.update({"_id":id}, jsondata)
              return 200
      except:
          print "Server Error"
          return 500

   def delete_quiz(self, quizid):
      print "---> delete:quiz", quizid
      try:
          id = ObjectId(quizid)
          print id
          cnt = self.quizcollection.find({"_id":id}).count()
          if cnt == 0:
              return 404   
          else:
              self.quizcollection.remove({"_id":id})     
              return 200 
      except:
          print "Server Error"
          return 500

   def list_quiz(self):
      print "---> list:quiz"
      try:    
          quizlist = []
          for quiz in self.quizcollection.find():
               quiz["_id"] = str(quiz["_id"])
               quizlist.append(quiz)
          
          return { "success" : True, "list" : quizlist };
      
      except:
          print "Server Error"
          return 500
      
##Announcement collection

   def add_announce(self, jsondata):
      print "---> add_announce:", jsondata
      try:
          obj_id = self.announcecollection.insert(jsondata)
          obj_id = str(obj_id) 
          respcode = 201     
          return {"resp_code":respcode,"id":obj_id}
      
      except:
          print "Server Error"
          return 500

   def get_announce(self,id):
      print "---> get:announce", id
      try:    
          id = ObjectId(id)
          #print id
          cnt = self.announcecollection.find({"_id":id}).count()
          print "cnt", cnt
          if cnt == 0:
              return 404   
          else:
              for announce in self.announcecollection.find({"_id":id}):
                  return {"id": str(id),"courseId": announce["courseId"],"title": announce["title"],"description":announce["description"],"postDate": announce["postDate"],"status": announce["status"]}
      except:
          print "Server Error"
          return 500

   def update_announce(self,announceid,jsondata):
      print "---> update:announce", jsondata
      try:
          id = ObjectId(announceid)
          print id
          cnt = self.announcecollection.find({"_id":id}).count()
          print "cnt" , cnt
          if cnt == 0:
              return 201     
          else:
              self.announcecollection.update({"_id":id}, jsondata)
              return 200
      except:
          print "Server Error"
          return 500

   def delete_announce(self, announceid):
      print "---> delete:announce", announceid
      try:
          id = ObjectId(announceid)
          print id
          cnt = self.announcecollection.find({"_id":id}).count()
          if cnt == 0:
              return 404   
          else:
              self.announcecollection.remove({"_id":id})     
              return 200 
      except:
          print "Server Error"
          return 500

   def list_announce(self):
      print "---> list:announce"
      try:    
          announcelist = []
          for announce in self.announcecollection.find():
               announce["_id"] = str(announce["_id"])
               announcelist.append(announce)
          
          return { "success" : True, "list" : announcelist };
      
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
     
## category collections
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
               obj_id = ObjectId(catgorydetails)
               respcode=409
           return {"resp_code":respcode,"id":obj_id} 
        except:
            print "Server Error"
            return {"resp_code":500,"id":obj_id}
<<<<<<< HEAD
   
=======
        
>>>>>>> 3691921b11031e122a5aedf0eafa040abaad3ee6
   
   def get_category(self,category):
       print "---> get category", category
       query={"name":category}
       try:
           cnt=self.categorycollection.find(query).count()
           if cnt==0:
               return 404
           else:
               for cat in self.categorycollection.find(query):
                   return{"name":cat["name"],"description":cat["description"],"status":cat["status"],"createDate":cat["createDate"]}
       except:
           print "Server Error"
           return 500
       
   def insert_quiz(self, jsondata):
       print "---> add:Quiz", jsondata
       try:
           obj_id = self.quizcollection.insert(jsondata)
           obj_id= str(obj_id)
           respcode = 201
           return {"res_code":respcode,"id":obj_id}
       except:
           print "Server Error"
           return {"res_code":500,"id":obj_id}






                  
            
   
   
       
