from flask import Blueprint

universityenrollment = Blueprint('universityenrollment',
                                  __name__,
                                  url_prefix='/universityenrollment',
                                  template_folder='templates')

from . import endpoints