from flask import Blueprint, render_template, request, redirect, url_for, session, flash

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('dashboard.html')
    




