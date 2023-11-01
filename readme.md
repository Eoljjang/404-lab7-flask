Hi there! Please note that for some reason when I run the POST and PUT curl commands I get a ""Did not attempt to load JSON data because the request Content-Type was not 'application/json'." error.

To get around this problem, I have to change the curl command to specify that it's a JSON-type, and submit the new input in JSON format. As such =>

1) curl -v -X POST localhost:8000/todos -d "task=make sure to do lab 7 questions"
Will turn into
2) curl -v -X POST localhost:8000/todos -H "Content-Type: application/json" -d '{"task":"make sure to do lab 7 questions"}'

AND 

3) curl -v -X PUT localhost:8000/todos/3 -d "task=profit more"
Will turn into
4) curl -v -X PUT -H "Content-Type: application/json" -d '{"task": "profit more"}' localhost:8000/todos/3

Finally, I used port 8000 instead of 5000 because of some errors setting up my server on 5000 (i'm on MacOS). 
To change it back to port 5000, remove the "port=8000" parameter in the last line of hello.py