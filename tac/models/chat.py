import datetime

from flask_mongoengine import Document
from mongoengine import StringField, ReferenceField, DateTimeField

from models.user import User


class Message(Document):
    user = ReferenceField(User, required=True)
    text = StringField(required=True)
    created_at = DateTimeField(required=True)
    # TODO: Extended to support multimedia support

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now(datetime.timezone.utc)
        return super(Message, self).save(*args, **kwargs)


class Room:
    name = "global"
    """
    TODO:
    Once system supports multiform, migrate current message to global room
    then inherit this class from Documents
    Extend the room with necessary property.
    """
