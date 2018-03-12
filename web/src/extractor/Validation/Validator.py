from src.BaseValidator import BaseValidator
from .schemas import *


class Validator(BaseValidator):
    """Validation for the transaction module happens here"""

    def __init__(self):
        super(Validator, self).__init__()

    def validate(self, payload):
        
        if "event_name" not in payload:
            return {"valid": False, "reason": "event_name was not submitted"}

        if  payload['event_name'] not in event_name_schema_mapper:
            return {"valid": False, "reason": "event_name not supported."}

        schema = event_name_schema_mapper[payload['event_name']]
        valid_schema, e = self._schema_validate(schema, payload)
        if not valid_schema:
            return {
                "valid": False,
                "reason": "Payload did not conform to the schema: {}".format(e)
            }
        return {"valid": True}