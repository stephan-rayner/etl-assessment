from web.BaseValidator import BaseValidator
from .schemas import *


class Validator(BaseValidator):
    """Validation for the transaction module happens here"""

    def __init__(self):
        super(Validator, self).__init__()

    def validate_extract_request(self, payload):
        event_name_validator_mapper = {
            "crash_report": self.validate_crash_report,
            "purchase": self.validate_purchase,
            "install": self.validate_install
        }

        if "event_name" not in payload:
            return {"valid": False, "reason": "event_name was not submitted"}

        if  payload['event_name'] not in event_name_validator_mapper:
            return {"valid": False, "reason": "event_name not supported."}

        return event_name_validator_mapper[payload['event_name']](payload)

    def validate_crash_report(self, payload):
        """ Input Validation for /Transaction"""
        valid_schema = self._schema_validate(crash_report_schema, payload)
        if not valid_schema:
            return {
                "valid": False,
                "reason": "The payload does not conform to the schema."
            }
        return {"valid": True}

    def validate_purchase(self, payload):
        """ Input Validation for /Transaction"""
        valid_schema = self._schema_validate(purchase_schema, payload)
        if not valid_schema:
            return {
                "valid": False,
                "reason": "The payload does not conform to the schema."
            }
        return {"valid": True}

    def validate_install(self, payload):
        """ Input Validation for /Transaction"""
        valid_schema = self._schema_validate(install_schema, payload)
        if not valid_schema:
            return {
                "valid": False,
                "reason": "The payload does not conform to the schema."
            }
        return {"valid": True}