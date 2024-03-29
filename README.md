# Connect Four Design &middot; [![Python application](https://github.com/sagerg/connect-four-design/actions/workflows/python-app.yml/badge.svg)](https://github.com/sagerg/connect-four-design/actions/workflows/python-app.yml)

A PvE connect four game running on Python that uses Alpha–beta pruning to determine best next moves. At the time of building this project, it is running on `Python 3.9.6` and using `pip 21.2.4`

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

**Run the game**

```
$ python app.py
```

Run tests with PyTest

```
$ pytest
```

### Contributing

When installing a package, run the `pip freeze` command to update `requirements.txt`

```
$ pip freeze > requirements.txt
```

### License

This project is [MIT licensed](./LICENSE).
