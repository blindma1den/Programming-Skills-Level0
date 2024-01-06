from flask import Blueprint

shippingsystem = Blueprint('shippingsystem', __name__,
                           url_prefix='/shippingsystem',
                           template_folder='templates')

from . import endpoints