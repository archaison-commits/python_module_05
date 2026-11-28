#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(dark_ingredients: str) -> str:
    dark_ingredients_list = dark_ingredients.lower().split(",")
    allowed = dark_spell_allowed_ingredients()
    result = any(dark_ingredient.strip() in allowed for dark_ingredient in dark_ingredients_list)
    if result:
        return f"{dark_ingredients} - VALID"
    else:
        return f"{dark_ingredients} - INVALID"
