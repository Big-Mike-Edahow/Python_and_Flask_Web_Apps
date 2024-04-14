# init.sh

export FLASP_APP=app.py
if [ ! -d "migrations" ]; then
    echo --------------------
    echo INIT The migrations folder
    echo --------------------
    export FLASK_APP=app.py; flask db init
fi
echo --------------------
echo Generate migration DDL code
echo --------------------
flask db migrate -m "Initial migration"
echo --------------------
echo Run the DDL code and migrate
echo --------------------
echo --------------------
echo This is the DDL code that will be run
echo --------------------
flask db upgrade --sql
flask db upgrade

