# src/core/hashing.py
import bcrypt

class Hash:
    @staticmethod
    def get_password_hash(password: str) -> str:
        """Generate a hashed password."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a hashed password against a plain password."""
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
