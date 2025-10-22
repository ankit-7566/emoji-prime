#!/usr/bin/env python3
"""
Discord Bot Emoji ID Updater
This script helps you update emoji IDs throughout your Discord bot files.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

def find_all_emojis() -> Dict[str, List[Tuple[str, int]]]:
    """Find all emoji IDs in the bot files and their locations."""
    emoji_pattern = re.compile(r'<(a?):([a-zA-Z0-9_]+):(\d{17,19})>')
    emoji_locations = {}
    
    for py_file in Path('.').rglob('*.py'):
        if 'update_emoji_ids.py' in str(py_file):
            continue
            
        with open(py_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines, 1):
                matches = emoji_pattern.finditer(line)
                for match in matches:
                    emoji_full = match.group(0)
                    if emoji_full not in emoji_locations:
                        emoji_locations[emoji_full] = []
                    emoji_locations[emoji_full].append((str(py_file), line_num))
    
    return emoji_locations

def display_emojis(emoji_locations: Dict[str, List[Tuple[str, int]]]):
    """Display all found emojis with their locations."""
    print("\n" + "="*80)
    print("FOUND EMOJI IDs IN YOUR DISCORD BOT")
    print("="*80 + "\n")
    
    sorted_emojis = sorted(emoji_locations.keys())
    for idx, emoji in enumerate(sorted_emojis, 1):
        locations = emoji_locations[emoji]
        print(f"{idx}. {emoji}")
        print(f"   Found in {len(locations)} location(s)")
        if len(locations) <= 3:
            for file_path, line_num in locations:
                print(f"   - {file_path}:{line_num}")
        print()

def update_emoji_id(old_emoji: str, new_id: str) -> int:
    """Update an emoji ID throughout all bot files."""
    # Parse the old emoji to get its structure
    match = re.match(r'<(a?):([a-zA-Z0-9_]+):(\d{17,19})>', old_emoji)
    if not match:
        print(f"Error: Invalid emoji format: {old_emoji}")
        return 0
    
    animated, name, old_id = match.groups()
    new_emoji = f"<{animated}:{name}:{new_id}>"
    
    files_updated = 0
    
    for py_file in Path('.').rglob('*.py'):
        if 'update_emoji_ids.py' in str(py_file):
            continue
            
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_emoji in content:
            new_content = content.replace(old_emoji, new_emoji)
            with open(py_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_updated += 1
    
    return files_updated

def bulk_update_emojis(emoji_mapping: Dict[str, str]):
    """Update multiple emoji IDs at once."""
    print("\n" + "="*80)
    print("BULK EMOJI UPDATE")
    print("="*80 + "\n")
    
    for old_emoji, new_id in emoji_mapping.items():
        files_updated = update_emoji_id(old_emoji, new_id)
        print(f"✓ Updated {old_emoji} → ID: {new_id} ({files_updated} files)")
    
    print(f"\n✓ Bulk update complete! Updated {len(emoji_mapping)} emoji(s)")

def interactive_mode():
    """Interactive mode for updating emojis one by one."""
    emoji_locations = find_all_emojis()
    
    if not emoji_locations:
        print("No emojis found in the bot files!")
        return
    
    display_emojis(emoji_locations)
    
    print("\n" + "="*80)
    print("INTERACTIVE EMOJI UPDATE MODE")
    print("="*80)
    print("\nOptions:")
    print("1. Update a specific emoji by entering its full text (e.g., <:asd:1408397481271627921>)")
    print("2. Type 'list' to see all emojis again")
    print("3. Type 'quit' to exit")
    
    while True:
        print("\n" + "-"*80)
        choice = input("\nEnter emoji to update (or 'list'/'quit'): ").strip()
        
        if choice.lower() == 'quit':
            print("\nExiting emoji updater...")
            break
        elif choice.lower() == 'list':
            display_emojis(emoji_locations)
            continue
        elif choice in emoji_locations:
            new_id = input(f"Enter new ID for {choice}: ").strip()
            if new_id.isdigit() and len(new_id) >= 17:
                files_updated = update_emoji_id(choice, new_id)
                print(f"\n✓ Updated {choice} in {files_updated} file(s)")
                # Refresh emoji locations
                emoji_locations = find_all_emojis()
            else:
                print("Error: Invalid ID format. Must be 17-19 digits.")
        else:
            print("Error: Emoji not found. Type 'list' to see all emojis.")

def main():
    print("\n" + "="*80)
    print("DISCORD BOT EMOJI ID UPDATER")
    print("="*80)
    print("\nThis tool helps you update emoji IDs in your Discord bot.")
    print("\nModes:")
    print("1. Interactive Mode - Update emojis one by one")
    print("2. Bulk Mode - Update multiple emojis using a mapping")
    print("3. List Only - Just show all emojis and exit")
    
    mode = input("\nSelect mode (1/2/3): ").strip()
    
    if mode == '1':
        interactive_mode()
    elif mode == '2':
        print("\nBulk mode example:")
        print("Edit this script and add your mappings to the 'emoji_mapping' dictionary")
        print("\nExample:")
        print("emoji_mapping = {")
        print("    '<:asd:1408397481271627921>': '1234567890123456789',")
        print("    '<:asdsw:1408397838857146470>': '9876543210987654321',")
        print("}")
        print("\nThen run: bulk_update_emojis(emoji_mapping)")
    elif mode == '3':
        emoji_locations = find_all_emojis()
        display_emojis(emoji_locations)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
