from flask import Flask, request

from aws_es_auth_proxy.extensions import config
from aws_es_auth_proxy.proxy import proxy_request


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route("/", defaults={"path": ""})
    @app.route(
        "/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"]
    )
    def handle_request(path):
        url = request.url.replace(
            request.host_url, f"https://{config.ES.credentials['host']}/"
        )
        forbidden_headers = ["host"]
        headers = {
            k: v
            for k, v in request.headers.items()
            if k.lower() not in forbidden_headers
        }
        return proxy_request(
            url, headers, request.get_data(), request.cookies, request.method
        )

    return app
