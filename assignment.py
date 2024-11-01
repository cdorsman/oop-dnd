#!/usr/bin/env python3

from dnd import DNDAPI



def display_spell(spell_data):
    print(f"Name: {spell_data['name']}")
    print(f"Level: {spell_data['level']}")
    print(f"Index: {spell_data['index']}")
    print(f"URL: {spell_data['url']}")
    print()

def menu():
    print("Welcome to the D&D Spellbook!")

    while True:
        print("Commands:")
        print("1 - List all spells")
        print("2 - Search for a spell by name")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nList of Spells:")
            for spell in spells:
                display_spell(spell)
        elif choice == '2':
            spell_name = input("Enter the spell name: ").lower()
            matching_spells = [spell for spell in spells if spell_name in spell['name'].lower()]
            print("\nMatching Spells:")
            for spell in matching_spells:
                display_spell(spell)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
