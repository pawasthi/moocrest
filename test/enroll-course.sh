#!/bin/bash
#
# test client access to our service

echo -e "\n"
#curl -i -X PUT --data 'email=xyz@abc.com?courseId=xxx' http://localhost:8080/course/enroll
#curl -i -X PUT http://localhost:8080/course/enroll

curl -i -H "Accept: application/json" -X PUT  -d 'email=xyz@abc.com?courseid=xxx' http://localhost:8080/course/enroll
echo -e "Pratibha\n"

