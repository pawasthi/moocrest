#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -X GET http://localhost:8080/announcement/518eb40ce4c7513adbfa1690
echo -e "\n"
