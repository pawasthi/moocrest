#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST --data '{"name":"sushrut_1","description":[],"status":0,"createDate":[]}'  http://localhost:8080/category
echo -e "\n"
