import jsonschema


class BaseValidator(object):
    """ This is the base object for Validators for all services"""

    def __init__(self):
        super(BaseValidator, self).__init__()

    def _schema_validate(self, schema, payload):
        """Validate JSON payload against schema"""
        try:
            jsonschema.validate(schema=schema, instance=payload)
            return True
        except:
            return False