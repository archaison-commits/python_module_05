#!/usr/bin/env python3

from alchemy.potions import healing_potion, strength_potion

if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: Strength potion brewed with "
          f"{strength_potion()}")
    print(f"Testing healing_potion: Healing potion brewed with "
          f"{healing_potion()}")
