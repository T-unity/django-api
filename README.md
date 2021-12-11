# command

## base
docker-compose build
docker-compose up
docker-compose down

## django

<!-- make PJ -->
<!-- django-admin startproject testproject -->
docker-compose run --rm app django-admin startproject testproject

prefix: docker-compose run --rm app
prefix: python manage.py

example: docker-compose run --rm app python manage.py

after
<!-- make application -->
startapp test
<!-- make pre migrate file -->
makemigrations
<!-- exec migrate -->
migrate
<!-- make admin user -->
createsuperuser
