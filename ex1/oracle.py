#!/usr/bin/env python3

import os

if __name__ == "__main__":
    from dotenv import load_dotenv  
    load_dotenv()
    try:
        matrix_mode: str = os.getenv("MATRIX_MODE", "development")
        database_url: str = os.getenv("DATABASE_URL", "DEBUG")
        api_key: str = os.getenv("API_KEY")
        log_level = os.getenv("LOG_LEVEL")
        zion_endpoint = os.getenv("ZION_ENDPOINT")
    except OSError as e:
        print(e)
    if matrix_mode == "development":
        print(f"Mode: {matrix_mode}")
    elif matrix_mode == "production":
        print(f"Mode: {matrix_mode}")
    else:
        print(f'Mode: "{matrix_mode}" is not a valid mode')    
    if database_url:
        print("Database: Connected to local instance")
    else:
        print("Databese: Not connected to local instance")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("Missing API key")
    print(f"Log level: {log_level}")
    if zion_endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline")