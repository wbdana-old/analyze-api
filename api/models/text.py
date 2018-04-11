from marshmallow import post_load
from .file import File, FileSchema
from .file_extension import FileExtension

class TextFile(File):
    def __init__(self, name, content):
        super().__init__(name, content, FileExtension.TEXT.value)

    def __repr__(self):
        return '<TextFile(name={self.name!r})>'.format(self=self)

class TextFileSchema(FileSchema):
    @post_load
    def make_textfile(self, data):
        return TextFile(**data)
