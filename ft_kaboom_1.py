#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access tp alchemy/grimoire/dark_spellbook.py direclty")
    dark_spells: str = "bats, aire, fire, jorge"
    print("Test import now - THIS WILL RAISE AN UNCOUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(f"Testing record light spell: Spell recorded: "
        f"{dark_spell_record("Caca", dark_spells)}")
