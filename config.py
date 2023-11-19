import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456789'
    UPLOAD_FOLDER = r'C:\Users\willi\OneDrive\appProjeto\uploads'
