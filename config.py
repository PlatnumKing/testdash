import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///hotel.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # NEW: Upload Folder config
    # This creates a folder named 'uploads' in your main project directory
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # Limit file size to 16MB