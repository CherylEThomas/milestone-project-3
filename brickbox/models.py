from brickbox import db


class Theme(db.Model):
    # schema for the Theme model
    id = db.Column(db.Integer, primary_key=True)
    theme_name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.theme_name


class Users(db.Model):
    # schema for the Login model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name