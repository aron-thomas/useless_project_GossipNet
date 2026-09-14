import sys
import os
from pathlib import Path

# Add backend to Python path for Vercel
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))
sys.path.insert(0, str(root_dir / "backend"))

# Import the FastAPI app
from backend.app.main import app

# Vercel needs the app exported as handler
