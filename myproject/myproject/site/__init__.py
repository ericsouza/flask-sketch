from flask import Blueprint
from application_tpl.site.views import index

site = Blueprint("site", __name__)

site.add_url_rule("/", view_func=index)
