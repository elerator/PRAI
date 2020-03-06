from flask import Flask, Blueprint, url_for, session
from flask_restplus import Api, Resource, fields,apidoc
from flask_cors import CORS
import os, uuid

app = Flask(__name__)
app.secret_key = str(uuid.uuid4()) # required by "session"
CORS(app, supports_credentials=True)


if 'REVERSE_PROXY_REQUIRED' in os.environ:
    from myProxyFix import ReverseProxied
    app.wsgi_app = ReverseProxied(app.wsgi_app)

api=Api(app,
        title="prai_information_desk",
        default="Endpoint",
        default_label="",
)

@api.route('/ping')
class Ping(Resource):
    def get(self):
        """
        A simple GET endpoint
        """
        return {'ping':'PONG'}

if __name__ == "__main__":
    app.run(debug=True)
    for x in range(1000):
        print("Hello world from Michael")
