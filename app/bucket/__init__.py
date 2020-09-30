from flask import Blueprint

# This instance of a Blueprint that represents the authentication Blueprint
bucket_blueprint = Blueprint('bucket', __name__)

from . import views