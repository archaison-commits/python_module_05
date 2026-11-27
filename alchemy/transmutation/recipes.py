#!/usr/bin/env python3

from ..potions import strength_potion, create_air
import elements


def lead_to_gold() -> str:

    return (f"Testing lead to Gold: Recipe transmuting "
            f"Lead to Gold: brew '{create_air()}' and '{strength_potion()}'"
            f" mixed with '{elements.create_fire()}'")
