import datetime as dt
from marshmallow import Schema, fields

class File():
    def __init__(self, name, content, extension):
        self.name = name
        self.content = content
        self.extension = extension
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<File(name={self.name!r})>'.format(self=self)

class FileSchema(Schema):
    name = fields.Str()
    content = fields.Str()
    extension = fields.Str()
    created_at = fields.Str()
    
