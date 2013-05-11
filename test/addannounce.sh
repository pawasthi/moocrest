#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST --data '{"courseId": "c1","title": "t1","description":"d1","postDate": "05-09-2013","status": 0}'  http://localhost:8080/announcements
echo -e "\n"
