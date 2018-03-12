crash_report_schema = {
    "type": "object",
    "properties": {
        "event_name": {
            "type": "string"
        },
        "user_id": {
            "type": "integer"
        },
        "timestamp": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        }
    },
    "required": ["event_name", "user_id", "timestamp", "message"]
}

purchase_schema = {
    "type": "object",
    "properties": {
        "event_name": {
            "type": "string"
        },
        "user_id": {
            "type": "integer"
        },
        "timestamp": {
            "type": "integer"
        },
        "sku": {
            "type": "string"
        }
    },
    "required": ["event_name", "user_id", "timestamp", "sku"]
}

install_schema = {
    "type": "object",
    "properties": {
        "event_name": {
            "type": "string"
        },
        "user_id": {
            "type": "integer"
        },
        "timestamp": {
            "type": "integer"
        }
    },
    "required": ["event_name", "user_id", "timestamp"]
}

event_name_schema_mapper = {
    "crash_report": crash_report_schema,
    "purchase": purchase_schema,
    "install": install_schema
}
