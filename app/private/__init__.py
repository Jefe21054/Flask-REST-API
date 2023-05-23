from flask import Blueprint

private_bp = Blueprint('private', __name__)

from . import resources