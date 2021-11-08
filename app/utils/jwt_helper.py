import jwt
from app.config import config
import datetime
import time


def encode_token(user_id: int):
    try:
        """Generete Token by User Id"""
        payload = {
            "exp": time.mktime(
                (
                    datetime.datetime.utcnow()
                    + datetime.timedelta(hours=int(config.JWT_HOUR))
                ).timetuple()
            ),
            "iat": time.mktime(datetime.datetime.utcnow().timetuple()),
            "iss": user_id,
        }

        return jwt.encode(payload=payload, key=config.JWT_KEY, algorithm="HS256")
    except Exception as ex:
        print(ex)
        return None


def decode_token(token):
    try:
        return jwt.decode(jwt=token, key=config.JWT_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "Token Expired"
    except jwt.InvalidTokenError:
        return "Token invalid, please login again"
