#!/usr/bin/env python3
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(dark_spell_name: str, dark_ingredients: str) -> str:
    check_dark_validation: str = validate_ingredients(dark_ingredients)
    if "INVALID" in check_dark_validation:
        return f"Spell rejected: {dark_spell_name.capitalize()} ({check_dark_validation})"
    return f"Spell recorded: {dark_spell_name.capitalize()} ({check_dark_validation})"

