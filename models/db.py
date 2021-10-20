import binascii
import datetime
import hashlib
import uuid
import jwt
import neomodel
import yaml
from neomodel import StructuredNode, StringProperty, UniqueIdProperty, DoesNotExist, DeflateError

from account_pb2 import Token

_TOKEN_EXPIRATION = 24 * 30


def make_password(raw_password, salt, iterations=100000, hash_name='sha256'):
    """
        Secure password hashing using the PBKDF2 algorithm (recommended)
        Configured to use PBKDF2 + HMAC + SHA256.
        The result is a 64 byte binary string.  Iterations may be changed
        safely but you must rename the algorithm if you change SHA256.
    """
    dk = hashlib.pbkdf2_hmac(password=raw_password.encode('utf-8'),
                             salt=salt.encode('utf-8'),
                             iterations=iterations,
                             hash_name=hash_name)
    return binascii.hexlify(dk).decode('ascii')


def generate_token(user):
    with open('./config.yaml') as f:
        config = yaml.safe_load(f)

    user_info = {
        'username': user.username,
        'email': user.email,
        'user_id': user.user_id
    }
    access_token = jwt.encode(user_info, config['jwt']['secret'], algorithm='HS256')
    user_info['grant_type'] = 'refresh'
    refresh_token = jwt.encode(user_info, config['jwt']['secret'], algorithm='HS256')
    Token(access_token=access_token, refresh_token=refresh_token)
    return jwt.encode({
        'user_info': user_info,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=_TOKEN_EXPIRATION)
    }, config['jwt']['secret'], algorithm='HS256')


class Profile(StructuredNode): # noqa
    user_id = UniqueIdProperty()
    username = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    password = StringProperty()
    salt = StringProperty()
    access_token = StringProperty()

    @staticmethod
    def login(username, password):
        try:
            user = Profile.nodes.get(username=username)
            hashed_password = make_password(password, user.salt)
            if user.password != hashed_password:
                return 'user name or password incorrect'
            return f'successfully logged in {user.username}'
        except DoesNotExist:
            return 'not found'


class Account(StructuredNode):  # noqa
    DoesNotExist = DoesNotExist
    DeflateError = DeflateError

    user_id = UniqueIdProperty()
    username = StringProperty(unique_index=True)
    email = StringProperty(unique_index=True)
    password = StringProperty()
    salt = StringProperty()

    @staticmethod
    def validate_email(address):
        assert '@' in address
        return address

    @staticmethod
    def create(username, password, email):
        salt = uuid.uuid4().hex
        hashed_password = make_password(password, salt)
        try:
            new_user = Account(username=username, password=hashed_password, email=email, salt=salt)
            token = generate_token(new_user)
            return token, True, new_user
        except neomodel.DeflateError as e:
            return str(e), False
