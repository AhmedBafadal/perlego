# Perlego Test
## Description
The repository includes a containerized django application with an API to read xml data into a postgresql database.
To upload an xml file, please access /upload endpoint, to view countries please use /book and /admin to delete any records.
There were challenges mostly in containerization, as i did not expect django rest framework to have a few bugs in process.

# Installation
```
docker build .
docker-compose build

set up admin user:
docker-compose run app sh -c "python manage.py createsuperuser"

```

# Running
```
docker-compose up
```

# Method
```
1. Please access /upload endpoint to upload xml
2. Uploaded xml files can be viewed at /book endpoint
3. To view admin page please access /admin and login with credentials
4. If any errors please shut down docker service and restart
```

# Testing 
```
docker-compose run app sh -c "python manage.py test"
```

