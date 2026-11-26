#!/usr/bin/env python3


from .elements import create_earth
from .elements import create_air
import elements

def healing_potion() -> str:
    return f"'{create_earth()}' and '{create_air()}'"

def strength_potion() -> str:
    return f"'{elements.create_fire()}' and '{elements.create_water()}'"
