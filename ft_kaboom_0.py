#!/usr/bin/env python3

import alchemy.grimoire.light_spellbook


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    light_spells: str = "earth, aire, fire, jorge"
    not_valid: str = "mirtha, caca, maybe"
    print(f"Testing record light spell: Spell recorded: "
          f"{alchemy.grimoire.light_spellbook.light_spell_record('Fantasy', light_spells)}\n")
