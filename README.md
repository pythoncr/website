PythonCR

Create a symlink

ln -s path-to-project/resources/settings/local.py path-to-project/resources/settings/application.py

Create/Modify your path-to-project/resources/settings/.env file to match your conf

DEBUG=on
SECRET_KEY=******
DATABASE_URL=postgres://pythoncr:pythoncr@127.0.0.1:5432/pythoncr

Install mailcatcher

apt install build-essential libsqlite3-dev ruby-dev
gem install mailcatcher --no-ri --no-rdoc
mailcatcher --ip=0.0.0.0

ENJOY!!