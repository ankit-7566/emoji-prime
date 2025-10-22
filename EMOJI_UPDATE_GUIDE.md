# 🎯 Discord Bot Emoji ID Update Guide

This guide will help you update all emoji IDs in your Discord bot quickly and easily.

## 📋 Quick Start

### Option 1: Interactive Mode (Easiest)
Perfect for updating emojis one at a time.

```bash
python3 update_emoji_ids.py
```

1. Select option `1` for Interactive Mode
2. You'll see a list of all emojis currently in your bot
3. Copy and paste the emoji you want to update (e.g., `<:asd:1408397481271627921>`)
4. Enter the new ID (just the numbers, e.g., `1234567890123456789`)
5. Done! The script will update all occurrences automatically

### Option 2: Bulk Update (Fastest)
Perfect for updating many emojis at once.

1. Open `bulk_update_example.py` in an editor
2. Add your emoji mappings:
   ```python
   emoji_mapping = {
       '<:asd:1408397481271627921>': '1234567890123456789',
       '<:asdsw:1408397838857146470>': '9876543210987654321',
       '<:alert:1408398509882736651>': '1111111111111111111',
   }
   ```
3. Run the script:
   ```bash
   python3 bulk_update_example.py
   ```

### Option 3: List Only
Just want to see all your emojis?

```bash
python3 update_emoji_ids.py
```
Select option `3` to view all emojis and exit.

## 📚 Understanding Emoji IDs

Discord emojis have this format:
- **Static emoji**: `<:emoji_name:1234567890123456789>`
- **Animated emoji**: `<a:emoji_name:1234567890123456789>`

### Parts of an emoji:
- `<:` or `<a:` - Indicates static or animated
- `emoji_name` - The name (for readability only)
- `1234567890123456789` - The actual ID (17-19 digits)
- `>` - Closing bracket

**Important**: Only the ID number changes. The emoji name and animation prefix stay the same!

## 🔍 Finding Your Emoji IDs

### Most Common Emojis in Your Bot:

1. **Error/Success Emojis** (used most frequently):
   - `<:asd:1408397481271627921>` - Error emoji
   - `<:asdsw:1408397838857146470>` - Success emoji
   - `<:alert:1408398509882736651>` - Alert emoji

2. **Navigation Arrows**:
   - `<:arrow_left:1348340563610435594>` - Left arrow
   - `<:arrow_right:1348340445708816494>` - Right arrow
   - `<:delete:1348340540650950816>` - Delete button

3. **Status Indicators**:
   - `<:tick:1408402912585056327>` - Checkmark
   - `<a:enabled:1349283415962157056>` - Enabled (animated)
   - `<a:disabled:1349283526465421325>` - Disabled (animated)

See `emoji_reference.md` for the complete list of 115 emojis!

## 🎨 Getting New Emoji IDs from Discord

### Method 1: From Discord Desktop/Web
1. Go to your Discord server
2. Right-click on the emoji you want to use
3. Click "Copy Link" or "Copy ID"
4. The ID is the long number in the URL or the copied value

### Method 2: From Discord Developer Mode
1. Enable Developer Mode in Discord Settings → Advanced → Developer Mode
2. Right-click the emoji in chat or emoji picker
3. Click "Copy ID"
4. Use this ID in the updater

### Method 3: From Emoji Picker
1. Type the emoji in Discord chat with a backslash: `\:emoji_name:`
2. Send the message
3. Discord will display: `<:emoji_name:1234567890123456789>`
4. Copy the ID from the displayed format

## 📝 Files in This Project

- `update_emoji_ids.py` - Main updater script (interactive and bulk modes)
- `bulk_update_example.py` - Example template for bulk updates
- `emoji_reference.md` - Complete list of all 115 emojis in your bot
- `EMOJI_UPDATE_GUIDE.md` - This guide

## ⚠️ Important Notes

1. **Backup First**: While the updater is safe, consider backing up your bot before making changes
2. **Test After Update**: Test your bot after updating emojis to ensure they display correctly
3. **ID Format**: Emoji IDs must be 17-19 digits long
4. **Name Preservation**: The emoji name stays the same, only the ID changes
5. **Animation Prefix**: `<:` for static, `<a:` for animated - keep this the same

## 🐛 Troubleshooting

### "Invalid ID format" error
- Make sure the ID is only numbers (no < : > symbols)
- ID must be 17-19 digits long

### Emoji not displaying in Discord
- Check if the emoji exists in your server
- Verify the bot has access to the emoji
- Make sure you copied the correct ID

### Script says "Emoji not found"
- Double-check you typed the emoji exactly as shown
- Include the `<:` or `<a:` prefix and the closing `>`
- Use option 3 to list all emojis and copy from there

## 📊 Statistics

Your bot currently uses:
- **115 unique emojis**
- **Across 88+ Python files**
- **Most used**: Alert/Error emojis (used 137+ times)

## 🚀 After Updating

After updating your emoji IDs:
1. The script automatically saves all changes
2. Restart your Discord bot
3. Test the commands that use emojis
4. Verify emojis display correctly in Discord

## 💡 Pro Tips

1. **Update common emojis first**: Start with error, success, and alert emojis as they're used most
2. **Group similar emojis**: Update all navigation arrows together, all status icons together, etc.
3. **Use bulk mode**: If you have many emojis to update, bulk mode is much faster
4. **Keep a backup**: Save your emoji mappings in case you need to revert

## 📞 Need Help?

If you encounter issues:
1. Check that Python 3 is installed: `python3 --version`
2. Verify the emoji format in `emoji_reference.md`
3. Try the interactive mode first (it's more forgiving)
4. Use option 3 to verify the emoji exists in your bot

---

Happy emoji updating! 🎉
