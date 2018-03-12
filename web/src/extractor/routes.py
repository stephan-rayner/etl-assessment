from flask import Blueprint, jsonify, request
from .Validation.Validator import Validator
from .ExtractorService import ExtractorService

mod = Blueprint('extractor', __name__)

def _handle_response(code, message, status):
    return jsonify({
        'status_code': code,
        'status_message': message,
    }), status

@mod.route('/', methods=['POST'])
def extract():
    data = request.json
    validator = Validator()
    check = validator.validate(data)
    if not check['valid']:
        return _handle_response(400, check['reason'], 400)

    event_name = data['event_name']
    print("A {} event was recieved".format(event_name))
    
    extractor = ExtractorService()

    if event_name == 'crash_report':
        result = extractor.crash_report(data['user_id'], data['timestamp'],
                                      data['message'])
    if event_name == 'purchase':
        result = extractor.purchase(data['user_id'], data['timestamp'],
                                      data['sku'])
    if event_name == 'install':
        result = extractor.install(data['user_id'], data['timestamp'])

    if result['status'] is 'success':
        return _handle_response(0, "success", 200)


    return jsonify({"CHEESE": "DOODLE"})