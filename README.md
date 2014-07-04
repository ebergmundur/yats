YATS
====

yet another (trouble) ticketing system base on Python Django

DEMO
-----
http://yats.mediafactory.de

Staff User:  
Login: staff.user  
Password: qwertz  

Customer User:  
Login: customer.user  
Password: qwertz  

KEY FEATURES
-----
- custom fields (mandatory fields and default values configurable)
- different view of tickets for customers - fields hideable from customers (even in emails)
- mails for ticket changes, comments, close, reopen, reassign
- searchable fields configurable
- searches saveable as reports
- ticket history
- file attachments (optionally virus scanned)
- twitter bootstrapp 2 - responsive layout
- git TAGS from Github as versions example
- simple, but yet powerful! No real magic :-) 2 sourcefiles besides the dajango stuff (tickets.py and shortcuts.py)

INSTALLATION
-----
no pypi package yet!

needs:  
pil or pillow  
rpc4django
httplib2 (if using tags from github)  
django-dashing  
django-wiki  
diff-match-patch  

should need:  
pyclamd (add TCPSocket 3310 and TCPAddr 127.0.0.1 to its config and restart)  
memcache  

There is a debian package which includes parts of all, but is very special designed for our usecase as we make no use of pip. It distributes all packages not available via debian packages.

settings.py reads part of its config data from an inifile (see top of settings.py).

The project is splited into 2 parts:
- the app (yats)
- the web, using the app (web)

Customization is done in the web module - e.g. add more ticket fields (models.py in web) besides the settings itself (settings.py and ini file).
So far the app needs 2 folders (for logging and attachments as defined in the inifile). Make sure the webserver has write access to those folders.
  
./manage.py syncdb  
./manage.py migrate  

OTHER PAGACKES:
-----
https://www.djangopackages.com/grids/g/ticketing/