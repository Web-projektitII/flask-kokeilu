from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User

def users(count=25):
    fake = Faker(['fi_FI'])
    i = 0
    while i < count:
        user = User(
            username=fake.user_name(),
            password='password',
            confirmed=True,
            role_id=1,
            email=fake.email()
            )
        db.session.add(user)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()

