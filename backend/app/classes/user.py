
from email.policy import default
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from app import db, ma, login_manager
from datetime import datetime
from uuid import uuid4

def get_uuid():
    return uuid4().hex

class AuthUser(UserMixin, db.Model):
    __tablename__ = 'auth_users'
    __bind_key__ = 'clearnet'
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer,
                   autoincrement=True,
                   primary_key=True,
                   unique=True)
    uuid = db.Column(db.String(32), default=get_uuid)
    api_key = db.Column(db.TEXT)
    username = db.Column(db.VARCHAR(40))
    password_hash = db.Column(db.TEXT)
    member_since = db.Column(db.TIMESTAMP(), default=datetime.utcnow())
    email = db.Column(db.VARCHAR(350))
    country = db.Column(db.INTEGER)
    admin = db.Column(db.INTEGER)
    admin_role = db.Column(db.INTEGER)

    def __init__(self,
                 user_name,
                 password_hash,
                 member_since,
                 email,
                 api_key,
                 country,
                 admin,
                 admin_role,
                 ):
        self.user_name = user_name
        self.password_hash = password_hash
        self.member_since = member_since
        self.email = email
        self.api_key= api_key
        self.country = country
        self.admin = admin
        self.admin_role = admin_role
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)

        return s.dumps({'id': self.id}).decode('ascii')

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])

        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False

        self.confirmed = True
        db.session.add(self)

        return True

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return Auth_User.query.get(data['id'])


class Auth_User_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Auth_User

    uuid = ma.auto_field()
    api_key = ma.auto_field()
    user_name = ma.auto_field()
    member_since = ma.auto_field()
    country = ma.auto_field()
    currency = ma.auto_field()
    currency = ma.auto_field()
    admin_role = ma.auto_field()
    admin = ma.auto_field()


class AnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'


login_manager.anonymous_user = AnonymousUser