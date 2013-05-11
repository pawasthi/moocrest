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
   def createUser(self, inputjson):
      print "In createUser", inputjson
      try:
          cnt = self.usercollection.find({"email":inputjson["email"]}).count()
          #print cnt
          if cnt == 0:
              collid = str(self.usercollection.insert(inputjson))      
              return {"resp_code":201,
                      "id":collid}
          else:
              userdetails = self.usercollection.find({"email":inputjson["email"]})
              return {"resp_code":409}
      except:
          print "Server Error"
          return 500


   def getUser(self, emailid):
      print "In getUser", emailid
      repstr = {}
      try:
          cnt = self.usercollection.find({"email":emailid}).count()
          print cnt
          if cnt == 0:
              return 404   
          else:
              for user in self.usercollection.find({"email":emailid}):
                  repstr = {"email": user["email"],
                            "own": user["own"],
                            "enrolled": user["enrolled"],
                            "quizzes": user["quizzes"]}
                  return repstr
      except:
          print "Server Error"
          return 500

   def deleteUser(self, emailid):
      print "In deleteUser", emailid
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

   def updateUser(self, inputjson):
      print "In updateUser", inputjson
      try:
          cnt = self.usercollection.find({"email":inputjson["email"]}).count()
          print "cnt" , cnt
          if cnt == 0:
              return 201     
          else:
              self.usercollection.update({"email": inputjson["email"]}, inputjson)
              return 200
      except:
          print "Server Error"
          return 500

   def enrollCourse(self, courseid, email):
      print "In enrollCourse", courseid, email
      try:
         cnt = self.usercollection.find({"email":email}).count()
         #print "courseid",courseid
         #print "email", email
         #print "cnt",cnt
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


   def dropCourse(self, courseid, email):
      print "In dropCourse", courseid, email
      try:
         cnt = self.usercollection.find({"email":email}).count()
         #print "courseid",courseid
         #print "email", email
         #print "cnt",cnt
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

   def addCourse(self, inputjson):
      print "In addCourse", inputjson
      try:
          collid = str(self.coursecollection.insert(inputjson))  
          return {"resp_code":201,"id":collid}
      
      except:
          print "Server Error"
          return 500


   def getCourse(self,id):
      print "In getCourse", id
      try:    
          id = ObjectId(id)
          repstr = {}
          #print id
          cnt = self.coursecollection.find({"_id":id}).count()
          #print "cnt", cnt
          if cnt == 0:
              return 404   
          else:
              for course in self.coursecollection.find({"_id":id}):
                  #print course["category"]
                  repstr = {"id":str(id),
                          "category":course["category"],
                          "title":course["title"],
                          "section":course["section"],
                          "dept":course["dept"],
                          "term":course["term"],
                          "year":course["year"],
                          "instructor":course["instructor"],
                          "days":course["days"],
                          "hours":course["hours"],
                          "Description":course["Description"],
                          "attachment":course["attachment"],
                          "version":course["version"]}
                  return repstr
      except:
          print "Server Error"
          return 500
      
   def updateCourse(self,courseid,inputjson):
      print "In updateCourse",courseid, inputjson
      try:
          id = ObjectId(courseid)
          cnt = self.coursecollection.find({"_id":id}).count()
          if cnt == 0:
              return 201     
          else:
              self.coursecollection.update({"_id":id}, inputjson)
              return 200
      except:
          print "Server Error"
          return 500

   def deleteCourse(self, courseid):
      print "In deleteCourse", courseid
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

   def listCourse(self):
      print "In listCourse"
      try:    
          courselist = []
          for course in self.coursecollection.find():
               course["id"] = str(course["_id"])
               course["_id"] = str(course["_id"])
               courselist.append(course)
          
          return { "success" : True, "list" : courselist };
      
      except:
          print "Server Error"
          return 500

##Quiz collection

   def addQuiz(self, inputjson):
      print "In addQuiz:", inputjson
      try:
          collid = str(self.quizcollection.insert(inputjson))      
          return {"resp_code":201,"id":collid}
      
      except:
          print "Server Error"
          return 500

   def getQuiz(self,id):
      print "In getQuiz", id
      try:    
          repstr = {}
          id = ObjectId(id)
          #print id
          cnt = self.quizcollection.find({"_id":id}).count()
          #print "cnt", cnt
          if cnt == 0:
              return 404   
          else:
              for quiz in self.quizcollection.find({"_id":id}):
                  repstr = {"id": str(id),
                          "courseId": quiz["courseId"],
                          "questions": quiz["questions"]}
                  return repstr
      except:
          print "Server Error"
          return 500

   def updateQuiz(self,quizid,inputjson):
      print "In updateQuiz", inputjson
      try:
          id = ObjectId(quizid)
          #print id
          cnt = self.quizcollection.find({"_id":id}).count()
          #print "cnt" , cnt
          if cnt == 0:
              return 201     
          else:
              self.quizcollection.update({"_id":id}, inputjson)
              return 200
      except:
          print "Server Error"
          return 500

   def deleteQuiz(self, quizid):
      print "In deleteQuiz", quizid
      try:
          id = ObjectId(quizid)
          #print id
          cnt = self.quizcollection.find({"_id":id}).count()
          if cnt == 0:
              return 404   
          else:
              self.quizcollection.remove({"_id":id})     
              return 200 
      except:
          print "Server Error"
          return 500

   def listQuiz(self):
      print "In listQuiz"
      try:    
          quizlist = []
          for quiz in self.quizcollection.find():
               quiz["_id"] = str(quiz["_id"])
               quiz["id"] = str(quiz["_id"])
               quizlist.append(quiz)
          
          return { "success" : True, "list" : quizlist };
      
      except:
          print "Server Error"
          return 500
      
##Announcement collection

   def addAnnounce(self, inputjson):
      print "In addAnnounce:", inputjson
      try:
          collid = str(self.announcecollection.insert(inputjson))    
          return {"resp_code":201,"id":collid}
      
      except:
          print "Server Error"
          return 500

   def getAnnounce(self,id):
      print "In getAnnounce", id
      try:    
          repstr = {}
          id = ObjectId(id)
          #print id
          cnt = self.announcecollection.find({"_id":id}).count()
          #print "cnt", cnt
          if cnt == 0:
              return 404   
          else:
              for announce in self.announcecollection.find({"_id":id}):
                  repstr = {"id": str(id),
                          "courseId": announce["courseId"],
                          "title": announce["title"],
                          "description":announce["description"],
                          "postDate": announce["postDate"],
                          "status": announce["status"]}
                  return repstr
      except:
          print "Server Error"
          return 500

   def updateAnnounce(self,announceid,inputjson):
      print "In updateAnnounce",announceid ,inputjson
      try:
          id = ObjectId(announceid)
          #print id
          cnt = self.announcecollection.find({"_id":id}).count()
          #print "cnt" , cnt
          if cnt == 0:
              return 201     
          else:
              self.announcecollection.update({"_id":id}, inputjson)
              return 200
      except:
          print "Server Error"
          return 500

   def deleteAnnounce(self, announceid):
      print "In deleteAnnounce", announceid
      try:
          id = ObjectId(announceid)
          #print id
          cnt = self.announcecollection.find({"_id":id}).count()
          if cnt == 0:
              return 404   
          else:
              self.announcecollection.remove({"_id":id})     
              return 200 
      except:
          print "Server Error"
          return 500

   def listAnnounce(self):
      print "In listAnnounce"
      try:    
          announcelist = []
          for announce in self.announcecollection.find():
               announce["_id"] = str(announce["_id"])
               announce["id"] = str(announce["_id"])
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
   def insertCategory(self,category):
        print "In insertCategory", category
        try:
           collid = str(self.categorycollection.insert(category))
           return {"resp_code":201,"id":collid} 

        except:
            print "Server Error"
            return 500
      
   def getCategory(self,categoryid):
       print "In getCategory", categoryid

       try:
           repstr = {}
           categoryid = ObjectId(categoryid)
           cnt=self.categorycollection.find({"_id":categoryid}).count()
           if cnt==0:
               return 404
           else:
               for cat in self.categorycollection.find({"_id":categoryid}):
                   repstr = {"name":cat["name"],
                          "description":cat["description"],
                          "status":cat["status"],
                          "createDate":cat["createDate"]}
       except:
           print "Server Error"
           return 500
                         
