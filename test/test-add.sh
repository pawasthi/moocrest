#!/bin/bash
#
# test client access to our service

echo -e "\n"
<<<<<<< HEAD
curl -i -H "Content-Type: application/json" -X POST --data '{"name":"sushrut","description":[],"createDate":[],"status":0}'  http://localhost:8080/user
=======
curl -i -H "Content-Type: application/json" -X POST --data '{"email": "xyz@abc.com","own": [],"enrolled": [],"quizzes": []}'  http://localhost:8080/user
>>>>>>> 832a00479a726691f3647f4ee76d48e8a8857250
echo -e "\n"
