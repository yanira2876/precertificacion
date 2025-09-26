from flask import Flask, render_template
from datetime import datetime
from base.controllers import citas, usuarios

def format_date(value, format='%Y-%m-%d'):
    """Convierte una cadena de fecha en un objeto datetime y lo formatea."""
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                value = datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                return value
    return value.strftime(format)

def format_travel_date(value):
    """Formatea fechas específicamente para el travel dashboard"""
    if not value:
        return 'N/A'
    

    if isinstance(value, str):
        try:
            date_obj = datetime.strptime(value, '%Y-%m-%d')
            return date_obj.strftime('%b %d %Y')
        except ValueError:
            return value
    

    if hasattr(value, 'strftime'):
        return value.strftime('%b %d %Y')
    
    return str(value)


def create_app():
    app = Flask (__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG=True,
    )

    
    app.register_blueprint(usuarios.bp)
    app.register_blueprint(citas.bp)

    app.add_template_filter(format_date, 'format_date')
    app.add_template_filter(format_travel_date, 'format_travel_date')


    @app.route('/')
    def index():
        return render_template('auth.html')

    return app