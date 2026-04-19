import os
from datetime import timedelta
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def _build_db_url():
    """Build MySQL URI from individual env vars, or fall back to DATABASE_URL / SQLite."""
    from urllib.parse import quote_plus

    # Priority 1: explicit full URL (e.g. mysql+pymysql://root:pass@localhost/price_comparison)
    if os.environ.get("DATABASE_URL"):
        return os.environ["DATABASE_URL"]

    # Priority 2: individual MySQL settings from .env
    mysql_user = os.environ.get("MYSQL_USER", "root")
    mysql_pass = os.environ.get("MYSQL_PASSWORD", "")
    mysql_host = os.environ.get("MYSQL_HOST", "localhost")
    mysql_port = os.environ.get("MYSQL_PORT", "3306")
    mysql_db   = os.environ.get("MYSQL_DATABASE", "price_comparison")

    if mysql_pass or mysql_user != "root":
        # URL-encode user & password so special chars (@, #, %, etc.) are safe
        safe_user = quote_plus(mysql_user)
        safe_pass = quote_plus(mysql_pass)
        return f"mysql+pymysql://{safe_user}:{safe_pass}@{mysql_host}:{mysql_port}/{mysql_db}?charset=utf8mb4"

    # Fallback: SQLite (for zero-config local dev)
    return "sqlite:///price_scope.db"


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get("SECRET_KEY") or "professional-secret-key-change-in-production"

    # ── MySQL (primary) / SQLite (fallback) ───────────────────────────────
    SQLALCHEMY_DATABASE_URI = _build_db_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_recycle": 280,      # recycle connections before MySQL 8hr timeout
        "pool_pre_ping": True,    # check connection health before using it
        "connect_args": {},
    }

    # Session config
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # Email config
    MAIL_SERVER = os.environ.get("MAIL_SERVER") or "smtp.gmail.com"
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 587)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") or True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER") or "noreply@pricescope.com"

    # App settings
    ITEMS_PER_PAGE = 12
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
