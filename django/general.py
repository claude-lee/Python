source venv/bin/activate
./manage.py runserver &

python manage.py inspectdb > somefile.txt
./manage.py shell


./manage.py sqlclear app_name | ./manage.py dbshell 
./manage.py syncdb

./manage.py schemamigration --initial southtut
./manage.py migrate southtut

./manage.py schemamigration my_app_name --auto --stdout
./manage.py migrate myapp --db-dry-run
 
./manage.py migrate --list

$ ./manage.py dbshell
psql=# CREATE DATABASE djtest; 
