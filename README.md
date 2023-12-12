# Connect Four Design

A connect four game running on PyGame. At the time of building this project, it is running on `Python 3.9.6` and using `pip 21.2.4`

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

Run game

```
$ python app.py
```

Run tests with PyTest

```
$ pytest -v
```

### Contributing

When installing a package, run the `pip freeze` command to update `requirements.txt`

```
$ pip freeze > requirements.txt
```

### License

This project is [MIT licensed](./LICENSE).
