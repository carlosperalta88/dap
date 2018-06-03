from flask import Blueprint

hello_resource = Blueprint('hello_resource', __name__)

@hello_resource.route('/')
def hello():
    return "Hy I'm using Docker!"

@hello_resource.route('/bla', methods=['POST'])
def bla():
    return "blabla"

