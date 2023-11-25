# Event Management App


## How to setup the Project

```bash
Clone the project
```
Move to the project folder and type the following command.

```bash
docker-compose up -d --build
```

Then, two container will be created,
1. web container
2. db container

Go inside the db container.
```bash
docker exec -it <container_id> bash 
```
(Note: You will get the container id by running the **docker ps** command)

Type psql, after that execute the following query. It will create the database, user and password.

```bash
create database core_db;
create user core_user with password 'core_password';
GRANT ALL PRIVILEGES ON DATABASE core_db TO core_user;
ALTER USER core_user WITH SUPERUSER;
```

Go inside the web container and type the following command.


```bash
docker exec -it <container_id> bash
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver 0.0.0.0:8000
```
After running the above command you can access the project by http://localhost:8000/



## API Details
### Admin API

Create event.

```bash
http://127.0.0.1:8000/api/events/create/
Request type: POST
payload: {
    "title": "Dzancing",
    "description": "Dancing competition....",
    "event_type": "online",
    "max_seats": 10,
    "booking_open_window_start": "2023-11-23T07:39:50Z",
    "booking_open_window_end": "2023-11-25T07:39:56Z",
    "created_by": 3
}
event_type value: online or offline
```

List events.

```bash
http://127.0.0.1:8000/api/events/
Request type: GET
```

Update events.

```bash
http://127.0.0.1:8000/api/events/<event_id>/update/
Request type: PUT
Payload: {
    "title": "Dancing",
    "description": "Dancing competition....",
    "event_type": "online",
    "max_seats": 10,
    "booking_open_window_start": "2023-11-23T07:39:50Z",
    "booking_open_window_end": "2023-11-25T07:39:56Z",
    "created_by": 1
}
```


View a summary of an event.

```bash
http://127.0.0.1:8000/api/events/1/summary/
Request type: GET
```

Sample script for API request
```bash
import requests

url = 'http://your_api_url/events/create/'
headers = {'Authorization': 'Bearer your_access_token'}
data = {
    "title": "Dancing",
    "description": "Dancing competition....",
    "event_type": "online",
    "max_seats": 10,
    "booking_open_window_start": "2023-11-23T07:39:50Z",
    "booking_open_window_end": "2023-11-25T07:39:56Z",
    "created_by": 1
}

response = requests.post(url, headers=headers, json=data)
```
### User API

View events
```bash
http://127.0.0.1:8000/api/allevents/
Request type: GET
```

Book a ticket for a event
```bash
http://127.0.0.1:8000/api/events/book/
Request type: POST
Payload: {
    "event_id": 3 
}
```

View ticket
```bash
http://127.0.0.1:8000/api/user/bookings/
Request type: GET
```

View all registered event
```bash
http://127.0.0.1:8000/api/user/events/
Request type: GET
```

## User Registration

For booking ticket user should be registered.
```bash
http://127.0.0.1:8000/api/register/
Request type: POST
Payload: {
    "email": "a@a.com",
    "user_name": "aaaa",
    "password": "admin"
}
```

## Create admin user

To create admin user
```bash
python manage.py createsuperuser
```

Admin user can call the API using the access token, which can be get by calling the below API
```bash
http://127.0.0.1:8000/api/token/
Request type: POST
Payload: {
    "email": "k@gmail.com",
    "password": "krishna"
}
```