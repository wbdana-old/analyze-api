from marshmallow import post_load
from .file import File, FileSchema
from .file_extension import FileExtension

class PythonFile(File):
    def __init__(self, name, content):
        # super(File, self).__init__(name, content, FileExtension.PYTHON)
        super().__init__(name, content, FileExtension.PYTHON)

    def __repr__(self):
        return '<PythonFile(name={self.name!r})>'.format(self=self)

class PythonFileSchema(FileSchema):
    @post_load
    def make_pythonfile(self, data):
        return PythonFile(**data)
