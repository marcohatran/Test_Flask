from service import *
from flask import Blueprint, request
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)
bp = Blueprint('bp', __name__)

"""
    Controller blueprint
"""


@bp.route('/distance', methods=('GET', 'POST'))
def distance():
    if request.method == 'POST':
        address = request.form['address']
        output = make_request(address)
        logging.info('Input Address : ' + address)
        logging.info('Output : ' + str(output))
        return output
