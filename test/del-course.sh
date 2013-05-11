#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -X DELETE http://localhost:8080/course/518eae39e4c75139a5e7f670
echo -e "\n"
