#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Content-Type: application/json" -X PUT --data '{"courseId": "c100","title": "t100","description":"d100","postDate": "05-23-2013","status": 0}'  http://localhost:8080/announcement/update/518eb40ce4c7513adbfa1690
echo -e "\n"
