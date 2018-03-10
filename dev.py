"""For running dev mode use app via docker for prod

    This was created as an early part of the build
and will eventually be replaced by the docker system.
"""
from web import app
app.run(debug=True, port=5000)