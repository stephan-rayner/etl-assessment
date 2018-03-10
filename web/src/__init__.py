from flask import Flask

app = Flask(__name__)

# from src.module_name.routes import mod
# app.register_blueprint(module_name.routes.mod)

from src.extractor.routes import mod
app.register_blueprint(extractor.routes.mod)