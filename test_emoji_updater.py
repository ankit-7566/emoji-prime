#!/usr/bin/env python3
"""
Test script to verify emoji updater is working
"""

from update_emoji_ids import find_all_emojis

print("=" * 80)
print("DISCORD BOT EMOJI UPDATER - TEST")
print("=" * 80)

print("\nSearching for emojis in bot files...")
emoji_locations = find_all_emojis()

if emoji_locations:
    print(f"\n✅ Success! Found {len(emoji_locations)} unique emojis in your Discord bot.")
    print(f"\nTop 5 most used emojis:")
    
    sorted_emojis = sorted(emoji_locations.items(), key=lambda x: len(x[1]), reverse=True)[:5]
    for emoji, locations in sorted_emojis:
        print(f"  • {emoji} - used {len(locations)} times")
    
    print(f"\n📝 Total emojis: {len(emoji_locations)}")
    print(f"📂 Run 'python3 update_emoji_ids.py' to start updating emojis")
    print(f"📚 See EMOJI_UPDATE_GUIDE.md for detailed instructions")
else:
    print("\n❌ No emojis found")

print("\n" + "=" * 80)
