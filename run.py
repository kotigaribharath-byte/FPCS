 import os
from dotenv import load_dotenv

# Load .env first
load_dotenv()

from app import app   # ✅ import app directly

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
