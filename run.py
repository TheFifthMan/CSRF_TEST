from app import app
from app.models import User

@app.cli.command()
def deploy():
    User.insert_user()