


from os import environ
from flask import Flask
from flask_cors import CORS


def create_app()-> Flask:
    app = Flask(__name__)
    
    CORS(app)
    
    @app.route("/")
    def root_route():
        return {
            "service": "My Service",
            "version": "0.0.1",
            "health": "OK",
        }, 200


if __name__ == "":
    create_app().run(debug=True, host="0.0.0.0", port=environ.get("PORT", "8080"))