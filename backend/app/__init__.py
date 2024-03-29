# coding=utf-8
from flask import Flask, jsonify, json
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy.orm import sessionmaker
from werkzeug.routing import BaseConverter
import decimal
from config import ApplicationConfig
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')


app.config.from_object(ApplicationConfig)
session = sessionmaker()

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


app.url_map.converters['regex'] = RegexConverter
app.json_encoder = DecimalEncoder
app.jinja_env.autoescape = True

# configuration
UPLOADED_FILES_DEST =   ApplicationConfig.UPLOADED_FILES_DEST
UPLOADED_FILES_ALLOW =  ApplicationConfig.UPLOADED_FILES_ALLOW

app.config['UPLOADED_FILES_DEST_USER'] = ApplicationConfig.UPLOADED_FILES_DEST_USER
app.config['UPLOADED_FILES_DEST_ITEM'] = ApplicationConfig.UPLOADED_FILES_DEST_ITEM
app.config['UPLOADED_FILES_DEST'] = ApplicationConfig.UPLOADED_FILES_DEST
app.config['UPLOADED_FILES_ALLOW'] = ApplicationConfig.UPLOADED_FILES_ALLOW
app.config['MAX_CONTENT_LENGTH'] = ApplicationConfig.MAX_CONTENT_LENGTH
app.config['SECRET_KEY'] = ApplicationConfig.SECRET_KEY
app.config['DEBUG'] = ApplicationConfig.DEBUG

app.config['SESSION_TYPE'] = ApplicationConfig.SESSION_TYPE
app.config['SESSION_COOKIE_NAME'] = ApplicationConfig.SESSION_COOKIE_NAME
app.config['SESSION_COOKIE_SECURE'] = ApplicationConfig.SESSION_COOKIE_SECURE
app.config['SESSION_COOKIE_HTTPONLY'] = ApplicationConfig.SESSION_COOKIE_HTTPONLY
app.config['SESSION_COOKIE_SAMESITE'] = ApplicationConfig.SESSION_COOKIE_SAMESITE
app.config['SESSION_PERMANENT'] = ApplicationConfig.SESSION_PERMANENT
app.config['SESSION_USE_SIGNER'] = ApplicationConfig.SESSION_USE_SIGNER
app.config['SESSION_REDIS'] = ApplicationConfig.SESSION_REDIS


session.configure(bind=ApplicationConfig.SQLALCHEMY_DATABASE_URI_0)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
server_session = Session(app)
mail = Mail(app)
ma = Marshmallow(app)
#csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.anonymous_user = "Guest"

@login_manager.request_loader
def load_user_from_request(request):
    # loads the user to currenct_user
    from app.classes.auth import Auth_User
    api_key = request.args.get('api_key')
    if api_key:
        user = Auth_User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key_auth = request.headers.get('Authorization')
    if api_key_auth:
        api_key = api_key_auth.replace('bearer ', '', 1)
        user = Auth_User.query.filter_by(api_key=api_key).first()
        if user:
            return user
    return None

api_main = {
    "origins": ['http://localhost:8080'],
    "methods": ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"],
    "allow_headers": ['Authorization, authorization, Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers']
}
# allows cors on all blueprints
cors = CORS(app,  supports_credentials=True, resources={r'/*': api_main})


# bind a function after each request, even if an exception is encountered.
@app.teardown_request
def teardown_request(response_or_exc):
    db.session.remove()

@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    db.session.remove()

@app.errorhandler(500)
def internal_error500():
    return jsonify({"error": "Internal Error 500"}), 500

@app.errorhandler(502)
def internal_error502(error):
    return jsonify({"error": "Internal Error 502"}), 502

@app.errorhandler(404)
def internal_error404(error):
    return jsonify({"error": "Internal Error 400"}), 400

@app.errorhandler(401)
def internal_error404(error):
    return jsonify({"error": "Internal Error 401"}), 401

@app.errorhandler(400)
def internal_error400(error):
    return jsonify({"error": "Internal Error 400"}), 400

@app.errorhandler(413)
def to_large_file(error):
    return jsonify({"error": "File is too large.  Use a smaller image/file."}), 413

@app.errorhandler(403)
def internal_error403(error):
    return jsonify({"error": "Internal Error 403"}), 403

@app.errorhandler(405)
def internal_error(error):
    return jsonify({"error": "Internal Error 405"}), 405

# link locations
from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

with app.app_context():
    db.create_all()
