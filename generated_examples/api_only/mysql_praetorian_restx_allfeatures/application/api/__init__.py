from flask import Blueprint
from flask_restx import Api
from .resources.auth import Login, Refresh


apibp = Blueprint("restapi", __name__, url_prefix="/api/v1.0")
api = Api(apibp)
api.add_resource(Login, "/login")
api.add_resource(Refresh, "/refresh")


########################################################################
#                                                                      #
#  Please make sure to remove all below lines before go to production  #
#                                                                      #
########################################################################

from .resources.examples.auth_examples import (
    Protected,
    ProtectedAdminRequired,
    ProtectedOperatorAccepted,
)

from .resources.examples.limiter_examples import slow, medium, fast, ping

from .resources.examples.cache_examples import (
    time_caching,
    external_func_caching,
    get_names,
    add_name,
)

api.add_resource(Protected, "/protected")
api.add_resource(ProtectedAdminRequired, "/protected_admin_required")
api.add_resource(ProtectedOperatorAccepted, "/protected_operator_accepted")

apibp.add_url_rule("/slow", view_func=slow)
apibp.add_url_rule("/medium", view_func=medium)
apibp.add_url_rule("/fast", view_func=fast)
apibp.add_url_rule("/ping", view_func=ping)


apibp.add_url_rule("/time_caching", view_func=time_caching)
apibp.add_url_rule("/external_func_caching", view_func=external_func_caching)
apibp.add_url_rule("/get_names", view_func=get_names)
apibp.add_url_rule("/add_name/<string:name>", view_func=add_name)
