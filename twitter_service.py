from flask import Flask
from authCache import AuthCache


api = Flask(__name__)
auth_server = AuthCache("auth.db")


@api.route("/")
def serve_():
    return '{"impressions": 0, "clicks": 0, "ctr": 0, "cpc": 0}'

api.run()