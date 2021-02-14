# Contains the routes for the Spam Net frontend
from flask import Blueprint, render_template, request

frontend_bp = Blueprint("frontend", __name__)

@frontend_bp.route('/')
def home():
   return render_template('index.html')
