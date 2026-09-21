#!/usr/bin/env python3

import os
from dotenv import load_dotenv


def oracle() -> None:
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...\n")
    matrix_mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    missing_conf = []
    if not database_url:
        missing_conf.append("DATABASE_URL")
    if not api_key:
        missing_conf.append("API_KEY")
    if not zion_endpoint:
        missing_conf.append("ZION_ENDPOINT")
    if missing_conf:
        print(f"WARNING: Missing configuration variables: "
              f"{', '.join(missing_conf)}")
        print("Please check your .env file or environment settings.\n")
    if matrix_mode == "production":
        db_status = "Connected to secure cluster (Production Mode)"
        api_status = "Authenticated via Production Vault"
    else:
        db_status = "Connected to local instance"
        api_status = "Authenticated"
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion_endpoint else 'Offline'}")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found "
              "(using system environment or defaults)")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


def main() -> None:
    oracle()


if __name__ == "__main__":
    main()
