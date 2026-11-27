#!/usr/bin/env python3

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) -> str:
    ingredients_list = ingredients.lower().split(",")
    result = any(ingredient.strip() in light_spell_allowed_ingredients() for ingredient in ingredients_list)
    if result:
        return (f"{spell_name.capitalize()} {ingredients} - VALID")
    else:
        return (f"{spell_name.capitalize()} {ingredients} - INVALID")
