#!/bin/bash
#
# test client access to our service

echo -e "\n"

curl -i -H "Content-Type: application/json" -X PUT --data '{"courseId":"518e6077e4c7511b4eba297a","questions": [{"question": "q1","options": ["o3","o4"],"answer": "o3","point": 10},{"question": "q2","options": ["o11","o22"],"answer":"o11","point": 10}]}'  http://localhost:8080/quiz/update/518d6536dbcf6e5b4ba8e0ec

echo -e "\n"
