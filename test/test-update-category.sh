#!/bin/bash
#
# test client access to our service

echo -e "\n"
curl -i -H "Content-Type: application/json" -X PUT --data ''  http://localhost:8080/category/upgate/sushrut
echo -e "\n"
