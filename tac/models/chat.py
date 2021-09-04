import datetime

from flask_mongoengine import Document
from mongoengine import StringField, ReferenceField, DateTimeField

from models.user import User


class Message(Document):
    user = ReferenceField(User, required=True)
    text = StringField(required=True)
    created_at = DateTimeField(required=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now(datetime.timezone.utc)
        return super(Message, self).save(*args, **kwargs)


class Room:
    name = "global"
