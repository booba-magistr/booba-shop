#!/bin/sh

if [ "$POSTGRES_DB" = "shop"]
then
    while ! nc -z "db" $POSTGRES_PORT; do
        sleep 0.5
    done
fi

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/main/stuff.json
python manage.py loaddata fixtures/main/contact.json
python manage.py loaddata fixtures/goods/category.json
python manage.py loaddata fixtures/goods/product.json
python manage.py loaddata fixtures/users/user.json

exec "$@"