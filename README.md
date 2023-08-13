# Beauty salon managing system
This app will help with beauty salon management - to create, to update or to delete Workers, Clients and the Procedures
with a simple and intuitive interface.




# The applicatios has following database structure:
![ScreenShot](/Schema.jpg)




## Installing / Getting started

A quick introduction of the minimal setup you need to get a beauty salon up &
running. With this You will run server with cleane Database.

```shell
git clone https://github.com/arturiermolenko/beauty_salon
cd beauty_salon
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
touch .env
python manage.py migrate
python manage.py runserver
```
Instead of "touch .env" use, please, command "echo > .env" for Windows.
Fill .env file in according to .env.sample



Use the following command to load prepared data from fixture:
```shell
python manage.py loaddata beauty_salon_data.json
```

## Features
With this application it will be easy to:
- create Employee-profile for all Your staff,
- add Clients to Database, 
- create, update or delete Appointments(Procedures)
- authorisation system for workers

## Links

- Project homepage: ""ToDo - add after deploy""
- Repository: https://github.com/arturiermolenko/beauty_salon
- Author's GitHub page: https://github.com/arturiermolenko/

## Demo User credentials
Use next user credentials for the test entry
- Login: admin
- Password: a1d1m1i1n1