from marshmallow import post_load
from .file import File, FileSchema
from .file_extension import FileExtension

class JavaScriptFile(File):
    def __init__(self, name, content):
        super(File, self).__init__(name, content, FileExtension.JAVASCRIPT)

    def __repr__(self):
        return '<JavaScriptFile(name={self.name!r})>'.format(self=self)

class JavaScriptFileSchema(FileSchema):
    @post_load
    def make_javascriptfile(self, data):
        return JavaScriptFile(**data)
        