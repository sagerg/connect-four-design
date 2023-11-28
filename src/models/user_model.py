from flask_login import UserMixin

from src import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False, unique=True)
    lastname = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=False)
    active = db.Column(db.Boolean, nullable=False, default=True)

    @property
    def is_active(self) -> bool:
        # override UserMixin property which always returns true
        # return the value of the active column instead
        return self.active