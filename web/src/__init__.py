from flask import Flask, jsonify

app = Flask(__name__)

# Top Level Exception Handler
@app.errorhandler(Exception)
def unhandled_exception(e):
    return jsonify({
        'status_code': 500,
        'status_message': str(e),
    }), 500

from src.extractor.routes import mod
app.register_blueprint(extractor.routes.mod)