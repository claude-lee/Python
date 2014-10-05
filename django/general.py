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


./manage.py schemamigration main --auto --update

rm -rf /usr/local/Cellar/mysql/5.6.20_1/
sudo rm /usr/local/mysql
sudo rm -rf /usr/local/mysql*
sudo rm -rf /Library/StartupItems/MySQLCOM
sudo rm -rf /Library/PreferencePanes/MySQL*
vim /etc/hostconfig and removed the line MYSQLCOM=-YES-
rm -rf ~/Library/PreferencePanes/MySQL*
sudo rm -rf /Library/Receipts/mysql*
sudo rm -rf /Library/Receipts/MySQL*
sudo rm -rf /var/db/receipts/com.mysql.*

./mysql -u root -h localhost -p



brew services start postgresql
and

brew services stop postgresql

heroku config | grep HEROKU_POSTGRESQL
heroku config | grep DATABASE_URL



 File "/app/.heroku/python/lib/python2.7/site-packages/django/utils/module_loading.py", line 31, in import_by_path
2014-10-05T10:14:11.831334+00:00 app[web.1]: ImproperlyConfigured: Module "django.contrib.auth.middleware" does not define a "SessionAuthenticationMiddleware" attribute/class

