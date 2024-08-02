Install library Jose
=> pip install "python-jose[cryptography]"

Create venv folder
=> python -m venv venv

Activated
=> .\venv\Scripts\activate

datetime update data validation
=> https://stackoverflow.com/questions/73128975/pydantic-created-at-and-updated-at-fields

Connect to Postgresql
=> 1. pip install psycopg2-binary 2. SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost/UserRolesDatabase' 3. engine = create_engine(SQLALCHEMY_DATABASE_URL)

Create requirements.txt
=> pip freeze >requirements.txt

install requirements.txt
=> In terminal type pip install -r requirements.txt

python testing use pytest
=> pytest file_name.py pytest .\tests\auth_test.py pytest .\tests\masters\ms_category_test.py

Run uvicorn
=> uvicorn api.main:app --reload

fastapi location
=> c:\user\samuel\Document\fastapi

activate fastapi in command prompt
=> fastapienv\scripts\activate.bat

open uvicorn
=> uvicorn file_name:app --reload

open fastapi document
=> 127.0.0.1:8000/docs

open sqlite in project
=> sqlite3 db_name.db

look table values
=> .schema

Sqlite insert Data
=> insert into todos (title,description,priority,complete) values ('Go to the store', 'Pick up eggs', 5, False);

Sqlite Delete Data
=> Delete from todos where id = 4;

Mode table sqlite
=> .mode column, .mode markdown, .mode box, .mode table

Run Multiple command testing in terminal
=> 1. Create master_testing.sh 2. open file location 3. run master_testing.sh

user admin
=> username : sofian, pass : admin

Make alembic revision
=> alembic revision -m "Create phone number for ms_user col"

alembic upgrade code
=> alembic upgrade 6b7d77829f0b(revision code)

alembic downgrade code
=> alembic downgrade -1

Mengatasi error Import Module saat testing
=> Tambahkan file **init**.py pada folder tests dan masters

Library Oath Google python
=> pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib pyjwt
pip install google-auth
pip install --upgrade google-api-python-client
pip install --upgrade google-auth google-auth-oauthlib

Run FastAPI in Flutter
=> uvicorn api.main:app --host 0.0.0.0 --port 8000
=> di flutter alamat url nya menggunakan alaman IPV4 wireless Connection, check di ipconfig
=> https://stackoverflow.com/questions/71195390/my-flutter-app-fails-to-connect-to-fastapi

Convert Excel to Json
=> https://codebeautify.org/excel-to-json

Convert Json to SQL Query
=> https://konbert.com/convert/json/to/sqlite?file_id=9d267e58-e6c8-4d47-a98a-ff390781a871

Open SQLite Database (In Terminal)
=> sqlite3 borrowApp.db

Open API from another PC
=> dont use https, use http instead

Check Total User that connect to Postgresql
=> SELECT \* FROM pg_stat_activity;

Install Google API Library
=> pip install google-api-python-client

Learn Connect Python to google Drive
=> https://www.youtube.com/watch?v=tamT_iGoZDQ&t=187s
