from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.extensions import db, migrate, bcrypt, jwt
from app.controllers.auth.auth import auth
from app.controllers.books.book_controller import book_api
from app.controllers.companies.company_controller import company_api
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

# Setting up an application factory function and everything must be within the function
def create_app():
    app = Flask(__name__)
    SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '..'  # Our API url (can of course be a local resource)

    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'

    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
       'clientId': "your-client-id",
       'clientSecret': "your-client-secret-if-required",
       'realm': "your-realms",
       'appName': "your-app-name",
       'scopeSeparator': " ",
       'additionalQueryStringParams': {'test': "hello"}
    }
)

    app.register_blueprint(swaggerui_blueprint)

    
    #  initialising JWTManager with secret key
    app.config['SECRET_KEY'] = 'A0703b91L08e9K9JV'
    jwt = JWTManager(app)
    
    app.config.from_object('config.Config')
    # enables us import our Config class
    # enables us to work with the application without showing our configuration
    # defining the class
    
    # Initialising the third-party libraries. we pass in the app and db
    db.init_app (app) 
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    app.config['JWT_SECRET_KEY'] = 'HS256'
    jwt.init_app(app)
    
    # working with migrations
    
    # importing and registering models
    from app.models.student import Student
    from app.models.course_units import CourseUnit
    from app.models.book import Book
    
   
    # testing whether the application works
    @app.route('/')
    def home():
        return "Authors API setup"
 # # registering blueprints
     # registering the blueprint auth
#    routes for protected resources
   
    app.register_blueprint(auth)
    
    
    @app.route('/protected')
    @jwt_required()
    def protected():
        current_user_id = get_jwt_identity()
        return jsonify(logged_in_as=current_user_id), 200
    
   

    return app

    

