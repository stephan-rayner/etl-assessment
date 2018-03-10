from flask import Flask

app = Flask(__name__)

# from src.module_name.routes import mod
# app.register_blueprint(module_name.routes.mod)

from web.extractor.routes import mod
app.register_blueprint(extractor.routes.mod)