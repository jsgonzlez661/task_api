# Task API Flask
## Methods 
### GET 
http://jsgonzlez661.pythonanywhere.com/tasks

Get all tasks in the database
```json
[
    {
        "create_date": "2020-07-10T23:03:46",
        "description": "description 1",
        "id": 1,
        "title": "title 1"
    }
    {
        "create_date": "2020-07-10T23:03:46",
        "description": description 2",
        "id": 2,
        "title": "title 2"
    }
]
```

http://jsgonzlez661.pythonanywhere.com/tasks/1

Get the task by your id
```json
{
    "create_date": "2020-07-10T23:03:46",
    "description": "description 1",
    "id": 1,
    "title": "title 1"
}
```
### POST 
http://jsgonzlez661.pythonanywhere.com/tasks

Send JSON
```json
{
    "title": "Title",
    "description": "description"
}
```
### PUT
http://jsgonzlez661.pythonanywhere.com/tasks/1

Updating a task 

Send JSON
```json
{
    "title": "New title",
    "description": "New description"
}
```
### DELETE
http://jsgonzlez661.pythonanywhere.com/tasks/1

Delete the task by its id
