from flask import Blueprint

currencyexchange = Blueprint('currencyexchange', __name__,
                           url_prefix='/currencyexchange',
                           template_folder='templates')

from . import endpoints