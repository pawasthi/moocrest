"""
6, Apr 2013

Example domain logic for the RESTful web service example.

This class provides basic configuration, storage, and logging.
"""

import sys
import os
import socket
import StringIO
import json

# moo 
from data.storage import Storage

#
# Room (virtual classroom -> Domain) functionality - note this is separated 
# from the RESTful implementation (bottle)
#
# TODO: only return objects/data and let moo.py handle formatting through 
# templates
#
class Room(object):
   # very limited content negotiation support - our format choices 
   # for output. This also shows _a way_ of representing enums in python
   json, xml, html, text = range(1,5)
   
   #
   # setup the configuration for our service
   #
   def __init__(self,base,conf_fn):
      self.host = socket.gethostname()
      self.base = base
      self.conf = {}
      
      # should emit a failure (file not found) message
      if os.path.exists(conf_fn):
         with open(conf_fn) as cf:
            for line in cf:
               name, var = line.partition("=")[::2]
               self.conf[name.strip()] = var.strip()
      else:
         raise Exception("configuration file not found.")

      # create storage
      self.__store = Storage()

##user Collection
   def create_user(self,jsondata):
        return self.__store.create_user(jsondata)
    
   def get_user(self,emailid):
        return self.__store.get_user(emailid)
    
   def update_user(self,emailid):
        return self.__store.update_user(emailid)
    
   def delete_user(self,emailid):
        return self.__store.delete_user(emailid)

   def enroll_course(self,courseid, emailid):
        return self.__store.enroll_course(courseid, emailid)

   def drop_course(self,courseid, emailid):
        return self.__store.drop_course(courseid, emailid)

##Category Collection
   def insert_category(self,category):
       return self.__store.insert_category(category) 
    
   def get_category(self,category):
       return self.__store.get_category(category) 

##Course Collection
   def add_course(self,jsondata):
        return self.__store.add_course(jsondata)

   def get_course(self,courseid):
        return self.__store.get_course(courseid)
    
   def update_course(self,courseid,jsondata):
        return self.__store.update_course(courseid,jsondata)
    
   def delete_course(self,courseid):
        return self.__store.delete_course(courseid)

   def list_course(self):
        return self.__store.list_course()

##Quiz collections
   def add_quiz(self,jsondata):
        return self.__store.add_quiz(jsondata)

   def get_quiz(self,quizid):
        return self.__store.get_quiz(quizid)
    
#   def insert_quiz(self, json_obj):
 #      return self.__store.insert_quiz(json_obj) 
#
   def list_category(self):
       return self.__store.list_category()
   
   def update_quiz(self,quizid,jsondata):
        return self.__store.update_quiz(quizid,jsondata)
    
   def delete_quiz(self,quizid):
        return self.__store.delete_quiz(quizid)

   def list_quiz(self):
        return self.__store.list_quiz()

##Announcement collections
   def add_announce(self,jsondata):
        return self.__store.add_announce(jsondata)

   def get_announce(self,announceid):
        return self.__store.get_announce(announceid)
    
   def update_announce(self,announceid,jsondata):
        return self.__store.update_announce(announceid,jsondata)
    
   def delete_announce(self,announceid):
        return self.__store.delete_announce(announceid)

   def list_announce(self):
        return self.__store.list_announce()

   # example: find data
   #
   def find(self,name):
      print '---> classroom.find:',name
      return self.__store.find(name)

   #
   # example: add data
   #
   def add(self,name,value):
      try:
         self.__store.insert(name,value)
         self.__store.names();
         return 'success'
      except:
         return 'failed'

      # TODO success|failure

   #
   # dump the configuration in the requested format. Note placing format logic
   # in the functional code is not really a good idea. However, it is here to
   # provide an example.
   #
   #
   def dump_conf(self,format):
      if format == Room.json:
         return self.__conf_as_json()
      elif format == Room.html:
         return self.__conf_as_html()
      elif format == Room.xml:
         return self.__conf_as_xml()
      elif format == Room.text:
         return self.__conf_as_text()
      else:
         return self.__conf_as_text()

   #
   # output as xml is supported through other packages. If
   # you want to add xml support look at gnosis or lxml.
   #
   def __conf_as_json(self):
      return "xml is hard"

   #
   #
   #
   def __conf_as_json(self):
      try:
         all = {}
         all["base.dir"] = self.base
         all["conf"] = self.conf
         return json.dumps(all)
      except:
         return "error: unable to return configuration"

   #
   #
   #
   def __conf_as_text(self):
      try:
        sb = StringIO.StringIO()
        sb.write("Room Configuration\n")
        sb.write("base directory = ")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("configuration:\n")
        
        for key in sorted(self.conf.iterkeys()):
           print >>sb, "%s=%s" % (key, self.conf[key])
        
        str = sb.getvalue()
        return str
      finally:
        sb.close()

#
      return "text"

   #
   #
   #
   def __conf_as_html(self):
      try:
        sb = StringIO.StringIO()
        sb.write("<html><body>")
        sb.write("<h1>")
        sb.write("Room Configuration")
        sb.write("</h1>")
        sb.write("<h2>Base Directory</h2>\n")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("<h2>Configuration</h2>\n")
        
        sb.write("<pre>")
        for key in sorted(self.conf.iterkeys()):
           print >>sb, "%s=%s" % (key, self.conf[key])
        sb.write("</pre>")
     
        sb.write("</body></html>")

        str = sb.getvalue()
        return str
      finally:
        sb.close()

#
# test and demonstrate the setup
#
if __name__ == "__main__":
  if len(sys.argv) > 2:
     base = sys.argv[1]
     conf_fn = sys.argv[2]
     svc = Room(base,conf_fn)
     svc.dump_conf()
  else:
     print "usage:", sys.argv[0],"[base_dir] [conf file]"
