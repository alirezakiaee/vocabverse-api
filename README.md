# Dummy text

docker build .
docker-compose build
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "django-admin startproject app."
docker-compose up
docker-compose run --rm app sh -c "python manage.py test"
docker-compose down
docker-compose build
docker volume ls
docker volume rm inventorysm_dev-db-data
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
