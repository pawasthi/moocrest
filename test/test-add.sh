#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Content-Type: application/json" -X POST --data '{"name":"sushrut","description":[],"createDate":[],"status":0}'  http://localhost:8080/user
echo -e "\n"
