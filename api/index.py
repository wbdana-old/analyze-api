from flask import Flask, jsonify, request

from api.models.python import PythonFile, PythonFileSchema
from api.models.javascript import JavaScriptFile, JavaScriptFileSchema
from api.models.file_extension import FileExtension
app = Flask(__name__)

files = [
    PythonFile('sample file 1', 'test content 1'),
    PythonFile('sample file 2', 'test content 2')
]

@app.route("/files/python")
def get_python_files():
    schema = PythonFileSchema(many=True)
    result = schema.dump(
        filter(lambda t: t.extension == FileExtension.PYTHON, files)
    )
    return jsonify(result.data)

# @app.route("/files/python", methods=['POST'])
# def add_python_file():
#     files.append(request.get_json())
#     return '', 204