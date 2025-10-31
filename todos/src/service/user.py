import bcrypt
from datetime import datetime, timedelta
from jose import jwt

class UserService:
    encoding: str = "UTF-8"
    secret_key: str = "e6f9b0949dd75a694f9d48556f6aed7588eb7fc8a01c6cdceef6ac0a6546bb99"
    jwt_algorithm: str = "HS256"

    def hash_password(self, plain_password: str) -> str:
        hashed_password: bytes = bcrypt.hashpw(
            plain_password.encode(self.encoding),
            salt=bcrypt.gensalt(),
        )
        return hashed_password.decode("UTF-8")

    def verify_password(
            self, plain_password: str,
            hashed_password: str
    ) -> bool:
        return bcrypt.checkpw(
            plain_password.encode(self.encoding),
            hashed_password.encode(self.encoding)
        )

    def create_jwt(self, username: str) -> str:
        return jwt.encode(
            {
                "sub": username,
                "exp": datetime.now() + timedelta(days=1),
            },
            self.secret_key,
            algorithm=self.jwt_algorithm
        )

    def decode_jwt(self, access_token: str) -> str:
        payload: dict = jwt.decode(
            access_token,self.secret_key, algorithms=[self.jwt_algorithm]
        )

        return payload["sub"]