source venv/bin/activate
./manage.py runserver &

python manage.py inspectdb > somefile.txt
./manage.py shell


./manage.py sqlclear app_name | ./manage.py dbshell 
./manage.py syncdb

./manage.py schemamigration --initial southtut
./manage.py migrate southtut