"""

This is only examples endpoints, please delete this file before
deploying to production

"""

from flask_restx import Resource
from flask_praetorian import (
    auth_required,
    current_user,
    roles_required,
    roles_accepted,
)


class Protected(Resource):
    @auth_required
    def get(self):
        """
        A protected endpoint. The auth_required decorator will require a header
        containing a valid JWT
        .. example::
        $ curl http://localhost:5000/protected -X GET \
            -H "Authorization: Bearer <your_token>"
        """

        return {
            "message": "protected endpoint (allowed user {})".format(
                current_user().username
            )
        }


class ProtectedAdminRequired(Resource):
    @roles_required('admin')
    def get(self):
        """
        A protected endpoint that requires a role. The roles_required decorator
        will require that the supplied JWT includes the required roles
        .. example::
        $ curl http://localhost:5000/protected_admin_required -X GET \
            -H "Authorization: Bearer <your_token>"
        """

        return {
            "message": "protected_admin_required endpoint (allowed user {})".format(
                current_user().username,
            )
        }


class ProtectedOperatorAccepted(Resource):
    @roles_accepted("operator", "admin")
    def get(self):
        """
        A protected endpoint that accepts any of the listed roles. The
        roles_accepted decorator will require that the supplied JWT includes at
        least one of the accepted roles
        .. example::
        $ curl http://localhost/protected_operator_accepted -X GET \
            -H "Authorization: Bearer <your_token>"
        """

        return {
            "message": "protected_operator_accepted endpoint (allowed usr {})".format(
                current_user().username
            )
        }

