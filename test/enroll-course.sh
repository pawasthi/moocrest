#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -X PUT http://localhost:8080/course/enroll --data 'email=xyz@abc.com?courseid=course111'
echo -e "\n"

