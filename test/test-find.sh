#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" http://localhost:8080/user/xyz@abc.com
echo -e "\n"
