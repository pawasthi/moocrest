#!/bin/bash
#
# test client access to our service

echo -e "\n"

curl -i -H "Content-Type: application/json" -X POST --data '{"courseId": "518e6077e4c7511b4eba297a","questions": [{"question": "q1","options": ["o1","o2"],"answer": "o2","point": 5},{"question": "q2","options": ["o1","o2"],"answer":"o2","point": 5}]}'  http://localhost:8080/quizzes

echo -e "\n"
