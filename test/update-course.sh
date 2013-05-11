#!/bin/bash
#
# test client access to our service

echo -e "\n"

curl -i -H "Content-Type: application/json" -X PUT --data '{"category":"category1xxx","title":"cmpe275xxx","section":1,"dept":"enggxxx","term":"Sprxxx","year":2013,"instructor":[{"name":"prof","id":1}],"days":["Monday","Wednesday"],"hours":["6:00PM","9:00PM"],"Description":"cmpe275","attachment":"xxxx","version":"1"}'  http://localhost:8080/course/update/518e6077e4c7511b4eba297a

echo -e "\n"
