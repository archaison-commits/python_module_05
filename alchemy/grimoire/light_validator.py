#!/usr/bin/env python3


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    ingredients_list = ingredients.lower().split(",")
    allowed = light_spell_allowed_ingredients()
    result = any(ingredient.strip() in allowed for ingredient in ingredients_list)
    if result:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
