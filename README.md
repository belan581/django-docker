# Django Docker
## Code based on:
### https://github.com/testdrivenio/django-on-docker
### https://github.com/archatas/django-myproject

## 1. Create executable build_dev.sh
### For linux
Copy `build_dev_example.sh` to `build_dev.sh`.

Edit the `build_dev.sh` file and add sensible values there.

Add execution permissions:

```bash
$ chmod +x build_dev.sh
```
### For windows
Copy `build_dev_example.bat` to `build_dev.bat`.

Edit the `build_dev.bat` file and add sensible values there.

## 2. Build the Docker containers

Run `build_dev.bat`:

```bash
c:/build_dev.bat
```

## 3. Check if the build was successful

If you now go to `http://0.0.0.0/` you should see a "Hello, World!" page there.

If you now go to `http://0.0.0.0/admin/`, you should see 


# Notes
## Run migration and collectstatic commands

SSH into the gunicorn container and run the necessary Django management commands:

```bash
$ docker exec -it "container_name" bash
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py createsuperuser
```

Answer all the questions asked by the management commands.

Press [Ctrl + D] twice to logout of the Docker container.

If you now go to `http://0.0.0.0/admin/`, you should see the Django administration where you can login with the super user's credentials that you have just created.

## 6. Overview of useful commands

### Rebuild docker containers

```bash
$ docker-compose down
$ ./build_dev.sh
```

### SSH to the Docker containers

```bash
$ docker exec -it "container_webapp_name" bash
$ docker exec -it "container_nginx_name" bash
$ docker exec -it "container_db_name" bash
```

### View logs

```bash
$ docker-compose logs nginx
$ docker-compose logs gunicorn
$ docker-compose logs db
```

### Copy files and directories to and from Docker container

```bash
$ docker cp ~/avatar.png django_docker_gunicorn_1:/home/project/media/
$ docker cp django_docker_gunicorn_1:/home/project/media ~/Desktop/
```

## Create analogous scripts for staging, production, and test environments

Copy `build_dev.sh` to `build_staging.sh`, `build_production.sh`, and `build_test.sh` and change the environment variables analogously.
