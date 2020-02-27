from flask import Flask, Blueprint, url_for, session
from flask_restplus import Api, Resource, fields,apidoc
from flask_cors import CORS
import os, uuid
from basf_auth.flask_restplus_auth import requires_basf_auth

app = Flask(__name__)
app.secret_key = str(uuid.uuid4()) # required by "session"
CORS(app, supports_credentials=True)


if 'REVERSE_PROXY_REQUIRED' in os.environ:
    from myProxyFix import ReverseProxied
    app.wsgi_app = ReverseProxied(app.wsgi_app)

swagger_security_definition = {
    "basf_auth": {"type": "apiKey", "in": "header", "name": "Authorization"}
}

api=Api(app, 
        title="prai_information_desk",
        default="Endpoint",
        default_label="",
        authorizations = swagger_security_definition
)

@api.route('/ping')
class Ping(Resource):
    def get(self):
        """
        A simple GET endpoint
        """
        return {'ping':'PONG'}

@api.route('/auth')
@api.doc(security="basf_auth")
class AuthRoute(Resource):

    @api.response(302, 'Redirected for login')
    @requires_basf_auth
    def get(self):
        """
        A simple GET endpoint that requires BASF authentication.
        """
        return dict(
            message = 'You are authenticated with the information shown here',
            user_id = session['basf_federation']['user_id']
        )

    @requires_basf_auth(['dummy'])
    def post(self):
        """
        A simple POST endpoint that is restricted to authorized users.
        """
        return dict(
            message='You are authorized',
            user_id = session['basf_federation']['user_id']
        )

if __name__ == "__main__":
    app.run(debug=True)
