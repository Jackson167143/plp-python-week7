# PLP Python Week 7 - Lists

This project demonstrates how to use Python lists, including indexing, adding, removing, looping, checking membership, and finding the length of a list.

## Files

- `list_warmup.py` - Demonstrates list indexing, append, remove, and len.
- `shopping_list.py` - A menu-based shopping list manager using add, remove, show, and done commands.
- `list_report.py` - Prints a numbered shopping list, counts items with more than four letters, and finds the longest item.
- `screenshots/` - Contains screenshots showing the programs running successfully.

## Why check `in` before using `.remove()`?

Checking `in` before calling `.remove()` is safer because `.remove()` causes an error if the item does not exist in the list. Using `in` first allows the program to handle a missing item without crashing and display a helpful message to the user.

## Assignment

PLP Python Week 7 - Lists