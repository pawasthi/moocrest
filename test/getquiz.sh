#!/bin/bash
#
# test client access to our service

echo -e "\n"

curl -i -X GET http://localhost:8080/quiz/518eb2bbe4c7513a1964aef7

echo -e "\n"
