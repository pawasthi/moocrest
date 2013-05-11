#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Content-Type: application/json" -X PUT --data '{"email":"xyz@abc.com","own":["course11","course12"],"enrolled":["course1","course2"],"quizzes":[]}'  http://localhost:8080/user/update/xyz@abc.com
echo -e "\n"
