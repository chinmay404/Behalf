# lambda_handler.py
from mangum import Mangum
from API.main import app  # Import your FastAPI instance

# Create a Mangum handler
handler = Mangum(app)
