"""
Debug script to verify .env variables are being loaded correctly
"""
from app.config import settings

print("=" * 60)
print("Configuration Verification")
print("=" * 60)
print(f"DB_HOST: {settings.db_host}")
print(f"DB_PORT: {settings.db_port}")
print(f"DB_USER: {settings.db_user}")
print(f"DB_PASSWORD: {'*' * len(settings.db_password) if settings.db_password else 'NOT SET'}")
print(f"DB_NAME: {settings.db_name}")
print(f"API_HOST: {settings.api_host}")
print(f"API_PORT: {settings.api_port}")
print(f"DEBUG: {settings.debug}")
print("=" * 60)
print(f"Database URL: {settings.database_url}")
print("=" * 60)
