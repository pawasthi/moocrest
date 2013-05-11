#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST --data '{"status": 1, "createDate": "05-09-2013", "name": "test", "description": "test"}'  http://localhost:8080/category
echo -e "\n"
