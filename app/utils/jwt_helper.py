import jwt
from app.config import config
import datetime
import time


def encode_token(user_id: int):
    try:
        """Generete Token by User Id"""
        payload = {
            "expire": time.mktime(
                (
                    datetime.datetime.utcnow()
                    + datetime.timedelta(hours=int(config.JWT_HOUR))
                ).timetuple()
            ),
            "created_at": time.mktime(datetime.datetime.utcnow().timetuple()),
            "user": user_id,
        }

        return jwt.encode(payload=payload, key=config.JWT_KEY, algorithm="HS256")
    except Exception as ex:
        print(ex)
        return None


def decode_token(token):
    try:
        data = jwt.decode(token, config.JWT_KEY)
        return data["user"]
    except jwt.ExpiredSignatureError:
        return "Token Expired"
    except jwt.InvalidTokenError:
        return "Token invalid, please login again"
