from flask import request, session, jsonify
from flask_login import current_user, logout_user, login_user
from flask_cors import cross_origin
from app.auth import auth
from app import db, bcrypt
from datetime import datetime
from app.common.decorators import login_required
# models
from app.classes.models import Query_Country_Schema, Query_Country
from app.classes.auth import Auth_User
from uuid import uuid4


@auth.route("/whoami", methods=["GET"])
@login_required
def check_session():
    if request.method == 'GET':

        api_key = request.headers.get('Authorization')
        if api_key:
            api_key = api_key.replace('Basic ', '', 1)
            user_exists = Auth_User.query.filter(Auth_User.api_key==api_key).first() is not None
            if user_exists:
                user = Auth_User.query.filter(Auth_User.api_key==api_key).first()

                return jsonify({
                "login": True,
                'user': {'user_id': user.uuid,
                        'user_name': user.username,
                        'user_email': user.email,
                        'country': user.country,
                        'currency': user.currency,
                        'token': user.api_key
                },
                'token': user.api_key
                    }), 200
            else:
                return jsonify({"status": "error. user not found"})
        else:
            return jsonify({"status": "error"})



@auth.route("/logout", methods=["POST"])
def logout():
    if request.method == 'POST':
        try:
            logout_user()
            return jsonify({'status': 'logged out'}), 200
        except Exception as e:
            return jsonify({"error", 'error'}), 400


@auth.route("/login", methods=["POST"])
def login():
    if request.method == 'POST':
        username = request.json["username"]
        password = request.json["password"]
        user = Auth_User.query.filter_by(username=username).first() is not None
        
        if not user:
            return jsonify({"error": "Unauthorized"}), 401
        user = Auth_User.query.filter_by(username=username).first()
        if not bcrypt.check_password_hash(user.password_hash, password):
            current_fails = int(user.fails)
            new_fails = current_fails + 1
            user.fails = new_fails
            db.session.add(user)
            db.session.commit()
            return jsonify({"error": "Unauthorized"}), 401

        user.locked = 0
        user.fails = 0
        db.session.add(user)
        db.session.commit()
    
        login_user(user)
        current_user.is_authenticated()
        current_user.is_active()
        return jsonify({
            "login": True,
            'user': {'user_id': user.uuid,
                    'user_name': user.username,
                    'user_email': user.email,
                    'profile_image': user.profileimage,
                    'country': user.country,
                    'currency': user.currency,
                    'token': user.api_key
            },
            'token': user.api_key
        }), 200


@auth.route("/register", methods=["POST"])
def register_user():
    if request.method == 'POST':
        now = datetime.utcnow()

        username = request.json["username"]
        email = request.json["email"]
        password = request.json["password"]
        country = request.json["country"]

        part_one_code =  uuid4().hex
        part_two_code = uuid4().hex
        part_three_code = uuid4().hex
        key = part_one_code + part_two_code + part_three_code

        user_exists_email = Auth_User.query.filter_by(email=email).first() is not None
        if user_exists_email:
            return jsonify({"error": "User already exists"}), 409
        user_exists_username = Auth_User.query.filter_by(username=username).first() is not None
        if user_exists_username:
            return jsonify({"error": "User already exists"}), 409

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = Auth_User(
                username=username,
                api_key=key,
                email=email,
                password_hash=hashed_password,
                member_since=now,
                country=country,
                admin=0,
                admin_role=0,
                )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        current_user.is_authenticated()
        current_user.is_active()
        return jsonify({
            "login": True,
            'user': {'user_id': new_user.uuid,
                    'user_name': new_user.username,
                    'user_email': new_user.email,
                    'profile_image': new_user.profileimage,
                    'country': new_user.country,
                    'currency': new_user.currency,
            },
            'token':  new_user.currency
        }), 200


@auth.route('/change-password', methods=['POST'])
@login_required
def change_password():
    if request.method == 'POST':
        user = Auth_User.query \
            .filter(Auth_User.id == current_user.id) \
            .first()
        if user.passwordpinallowed == 1:
            new_password = request.json["password"]
            new_password_confirm = request.json["password"]
            if str(new_password) == str(new_password_confirm):
                hashed_password = bcrypt.generate_password_hash(new_password)

                user.password_hash = hashed_password
                user.passwordpinallowed = 0
                db.session.add(user)
                db.session.commit()

                return jsonify({"status": "success"}), 200
            else:
                return jsonify({"error": "Password Error"}), 401
        else:
            return jsonify({"error": "Must unlock account to change password"}), 409




@auth.route('/query/country', methods=['GET'])
def get_country_list():
    """
    Returns list of Countrys
    :return:
    """
    if request.method == 'GET':
        country_list = Query_Country.query.order_by(Query_Country.name.asc()).all()
        country_schema = Query_Country_Schema(many=True)
        return jsonify(country_schema.dump(country_list))
