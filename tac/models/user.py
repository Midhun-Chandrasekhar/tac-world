import datetime

from flask_mongoengine import Document
from mongoengine import StringField, DateTimeField


class User(Document):
    user_name = StringField(unique=True)
    created_at = DateTimeField(required=True)
    # TODO: Encrypted password store, Extend with profile properties

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now(datetime.timezone.utc)
        return super(User, self).save(*args, **kwargs)
