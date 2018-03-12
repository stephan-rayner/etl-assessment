from flask import Flask, jsonify

app = Flask(__name__)

# Top Level Exception Handler
@app.errorhandler(Exception)
def unhandled_exception(e):
    print("ERROR: TOP LEVEL:", e)
    return jsonify({
        'status_code': 500,
        'status_message': str(e),
    }), 500


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        'status_code': 404,
        'status_message': str(error),
    }), 404


@app.errorhandler(405)
def page_not_found(error):
    return jsonify({
        'status_code': 405,
        'status_message': str(error),
    }), 405


from src.extractor.routes import mod
app.register_blueprint(extractor.routes.mod)