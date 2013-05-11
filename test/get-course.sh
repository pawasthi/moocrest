#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -X GET http://localhost:8080/course/518eae3fe4c75139a5e7f671
echo -e "\n"
