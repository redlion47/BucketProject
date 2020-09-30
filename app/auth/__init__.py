from flask import Blueprint

# This instance of a Blueprint that represents the authentication Blueprint
auth_blueprint = Blueprint('auth', __name__)

from . import views