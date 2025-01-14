from flask import Flask
from flasgger import Swagger
from blueprints.animals import animals_bp
from blueprints.employees import employees_bp

app = Flask(__name__)
swagger = Swagger(app)

# Register blueprints
app.register_blueprint(animals_bp)
app.register_blueprint(employees_bp)

@app.route('/Home', methods=['GET'])
def dashboard():
    return "Welcome to the zoo"

if __name__ == '__main__':
    app.run(debug=True, port=5000)

