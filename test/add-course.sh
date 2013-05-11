#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST --data '{"category":"category1","title":"cmpe275","section":1,"dept":"engg","term":"Spr","year":2013,"instructor":[{"name":"prof","id":1}],"days":["Monday","Wednesday"],"hours":["6:00PM","9:00PM"],"Description":"cmpe275","attachment":"xxxx","version":"1"}'  http://localhost:8080/course

echo -e "\n"
