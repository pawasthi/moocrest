#!/bin/bash
#
# test client access to our service

echo -e "\n"

curl -i -X GET http://localhost:8080/quiz/518e7d79e4c751270e80a5fe

echo -e "\n"
