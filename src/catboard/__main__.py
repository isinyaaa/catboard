from .main import app
from uvicorn import run


run(app, host="0.0.0.0", port=8000, log_level="info")
