from app import app, db
from app.models import  Area, Login1, Rest


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Login1':Login1,'Area':Area,'Rest':Rest}




