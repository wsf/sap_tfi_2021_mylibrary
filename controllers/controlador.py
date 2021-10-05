import random

from odoo import http
from odoo.http import request
from .tools.tools import info_clientes, contador, reloj, barra
from .tools.filter_query import filter_query

import werkzeug
from werkzeug import urls
