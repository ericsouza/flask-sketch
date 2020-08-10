from flask import request
from application.ext.auth import guard
from flask_restx import Resource


class Login(Resource):
    def post(self):
        """
        Logs a user in by parsing a POST request containing user credentials and
        issuing a JWT token.
        .. example::
        $ curl http://localhost:5000/login -X POST \
            -d '{"username":"Walter","password":"calmerthanyouare"}'
        """
        req = request.get_json(force=True)
        username = req.get('username', None)
        password = req.get('password', None)
        user = guard.authenticate(username, password)
        token = guard.encode_jwt_token(user)
        return {'access_token': token}, 200


class Refresh(Resource):
    def post(self):
        """
        Refresh a token by parsing a POST request containing old access token and
        issuing a new JWT token.
        .. example::
        $ curl http://localhost:5000/refresh -X POST \
            -d '{"token":"your token"}'
        """

        data = request.get_json()
        token = guard.refresh_jwt_token(data["token"])
        return {'access_token': token}, 200
