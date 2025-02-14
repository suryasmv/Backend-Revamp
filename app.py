from flask import Flask
from routes.batch_routes import batch_routes
from routes.patient_routes import patient_bp

app = Flask(__name__)

# Register the batch routes
app.register_blueprint(batch_routes)
app.register_blueprint(patient_bp)


if __name__ == '__main__':
    app.run(debug=True)
