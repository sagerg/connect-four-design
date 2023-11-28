# Connect Four Design

A connect four game running on Flask

## Quick Start

Clone the repository

```
$ git clone https://github.com/sagerg/connect-four-design.git
$ cd connect-four-design
```

Create a virtual environment

```
$ python -m venv venv/
```

Activate your virtual environment for Linux/Mac OS

```
$ source venv/bin/activate
```

Activate your virtual environment for Windows

```
$ venv\Scripts\activate
```

Install python dependencies

```
$ pip install -r requirements.txt
```

Create a `.env` file

```
$ touch .env
$ echo SQLALCHEMY_DATABASE_URI_DEV=\"sqlite:///database.db\" >> .env
$ echo SQLALCHEMY_DATABASE_URI_PRD=\"[Your URL Here]\" >> .env
$ echo SQLALCHEMY_TRACK_MODIFICATIONS=False >> .env
$ echo SECRET_KEY=\"[Your Key Here]\" >> .env
```

Run the server

```
$ python app.py
```

## Database Migrations

The following steps were taken from [this](https://blog.miguelgrinberg.com/post/how-to-add-flask-migrate-to-an-existing-project) blog by **Miguel Greenberg**

Creating the migration repository

```
$ flask db init
```

Creating the initial migration. This step does not work if you have an existing project that has a populated database

```
$ flask db migrate -m "your commit message"
```

Tell Flask-Migrate and Alembic that the database is up to date

```
$ flask db stamp head
```

Final migration step

```
$ flask db upgrade
```

### Python

At the time of building this project, it is running on `Python 3.10.4` and using `pip 22.0.4`

### Contributing

When installing a package, run the `pip freeze` command to update `requirements.txt`

```
$ pip freeze > requirements.txt
```

### Educational Resources

[Flask API Folder Guide 2023](https://github.com/AshleyAlexJacob/Flask-API-Folder-Guide-2023)

[How To Add Flask-Migrate To An Existing Project](https://blog.miguelgrinberg.com/post/how-to-add-flask-migrate-to-an-existing-project)

### License

This project is [MIT licensed](./LICENSE).