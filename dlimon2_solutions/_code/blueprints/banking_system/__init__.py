from flask import Blueprint

bankingsystem = Blueprint('bankingsystem', __name__,
                           url_prefix='/bankingsystem',
                           template_folder='templates',)

from . import endpoints