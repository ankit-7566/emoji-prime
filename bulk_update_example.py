#!/usr/bin/env python3
"""
Bulk Emoji ID Update Example

Edit the emoji_mapping dictionary below with your old emoji IDs and new emoji IDs,
then run this script to update all emojis at once.
"""

from update_emoji_ids import bulk_update_emojis

# ADD YOUR EMOJI MAPPINGS HERE
# Format: 'old_emoji_with_id': 'new_id_only'
emoji_mapping = {
    # Example mappings - replace these with your actual emoji IDs
    # '<:asd:1425818447094218793>': '1234567890123456789',
    # '<:asdsw:1425817350967398523>': '9876543210987654321',
    # '<:alert:1425819342511276083>': '1111111111111111111',
    
    # Add your mappings below (one per line):
    
}

if __name__ == "__main__":
    if not emoji_mapping:
        print("⚠️  No emoji mappings defined!")
        print("\nPlease edit this file and add your emoji mappings to the 'emoji_mapping' dictionary.")
        print("\nExample:")
        print("emoji_mapping = {")
        print("    '<:asd:1425818447094218793>': '1234567890123456789',")
        print("    '<:asdsw:1425817350967398523>': '9876543210987654321',")
        print("}")
        print("\nSee emoji_reference.md for a complete list of all emojis in your bot.")
    else:
        print("Starting bulk emoji update...")
        bulk_update_emojis(emoji_mapping)
        print("\n✅ All done! Your emoji IDs have been updated.")
