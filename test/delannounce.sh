#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -X DELETE http://localhost:8080/announcement/518eb40de4c7513adbfa1691
echo -e "\n"
