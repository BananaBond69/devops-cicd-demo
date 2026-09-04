from flask import Flask, jsonify


def register_routes(app: Flask) -> None:
    @app.get("/")
    def index():
        return jsonify(service="devops-cicd-demo", status="ok")

    @app.get("/health")
    def health():
        return jsonify(status="healthy")

    @app.get("/ready")
    def ready():
        return jsonify(status="ready")
