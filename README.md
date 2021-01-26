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

# Testing 
```
docker-compose run app sh -c "python manage.py test"
```

