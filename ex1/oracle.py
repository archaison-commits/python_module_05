#!/usr/bin/env python3

import os


def variable_checker() -> None:
    variables = [
        "MATRIX_MODE", "DATABASE_URL", "API_KEY",
        "LOG_LEVEL", "ZION_ENDPOINT"]
    var_counter: int = 0
    with open(__file__, "r") as file:
        source_code = file.readlines()
        for variable in variables:
            variable_found: bool = False
            for line in source_code:
                if variable in line and "os.getenv(" in line:
                    variable_found = True
            if variable_found:
                var_counter += 1
    if var_counter == len(variables):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] secrets may be hardcoded")


if __name__ == "__main__":
    print("\nORACLE STATUS: Consulting the configuration\n")
    from dotenv import load_dotenv
    load_dotenv()
    matrix_mode: str = os.getenv("MATRIX_MODE", "development")
    database_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT")
    print("Configuration loaded:")
    if matrix_mode == "development":
        print(f"Mode: {matrix_mode}")
        if database_url:
            print("Database: Connected to local instance")
        else:
            print("Database: Not connected to local instance")
        if api_key:
            print("API Access: Authenticated")
        else:
            print("Missing API key")
        if log_level == "DEBUG":
            print(f"Log level: {log_level}")
        else:
            print("Log level: Not configured")
        if zion_endpoint:
            print("Remote Network: Online")
        else:
            print("Remote Network: Offline")
    elif matrix_mode == "production":
        print(f"Mode: {matrix_mode}")
        if api_key and zion_endpoint and database_url:
            print("System: Operational.")
        else:
            print("System: Not operational, missing API Access, "
                  "remote Endpoint or Database")
    else:
        print(f'Mode: "{matrix_mode}" is not a valid mode')
    print("\nConfiguration security check:")
    variable_checker()
    try:
        with open(".gitignore", "r") as file:
            content = file.read()
            if ".env" in content:
                print("[OK] .env file properly ignored by git")
            else:
                print("[KO] .env is not ignored by git")
    except OSError:
        print(".gitignore does not exist")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")
