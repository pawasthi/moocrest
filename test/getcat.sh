#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -X GET http://localhost:8080/category/518ebc31e4c7513ec90e9a15
echo -e "\n"
