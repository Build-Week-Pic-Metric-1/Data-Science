"""Entry point for predictor-api Flask application."""
from .app import create_app

APP = create_app()