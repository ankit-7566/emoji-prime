# Discord Bot - Setup & Emoji Update Instructions

## 📦 What's Included

This is a Discord bot with emoji ID update tools. The bot has been extracted and is ready to use.

### Main Files:
- **Discord Bot Files**: `main.py`, `cogs/`, `utils/`, etc.
- **Emoji Update Tools**: Tools to change all emoji IDs in your bot

## 🎯 Two Main Uses

### 1. Update Emoji IDs (Primary Purpose)

**Quick Start - Update Emojis:**

```bash
# Interactive mode (easiest)
python3 update_emoji_ids.py
# Select option 1, then follow prompts

# Or bulk mode (fastest for many emojis)
# Edit bulk_update_example.py first, then run:
python3 bulk_update_example.py
```

**Complete Emoji Guide:** See `EMOJI_UPDATE_GUIDE.md` for detailed instructions

**Emoji Reference:** See `emoji_reference.md` for all 115 emojis in your bot

### 2. Run the Discord Bot

To run the bot, you need:

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Discord Token:**
   The bot needs a `TOKEN` environment variable with your Discord bot token.
   
   You can set it in Replit Secrets or create a `.env` file:
   ```
   TOKEN=your_discord_bot_token_here
   ```

3. **Run the Bot:**
   ```bash
   python3 main.py
   ```

## 📋 Project Structure

```
.
├── main.py                    # Main bot file
├── cogs/                      # Bot command modules
│   ├── commands/             # Command cogs
│   ├── events/               # Event handlers
│   ├── moderation/           # Moderation commands
│   └── ...
├── utils/                     # Utility functions
├── db/                        # Database files
├── games/                     # Game modules
├── update_emoji_ids.py        # Interactive emoji updater
├── bulk_update_example.py     # Bulk emoji updater
├── emoji_reference.md         # Complete emoji list
└── EMOJI_UPDATE_GUIDE.md      # Detailed emoji update guide
```

## 🔧 Bot Configuration

The bot uses:
- **Discord.py** for Discord API
- **Flask** for keeping alive (webhook on port 8080)
- **Jishaku** for developer commands
- **MongoDB** for database (pymongo)
- **Wavelink** for music features

### Environment Variables Needed:
- `TOKEN` - Discord bot token (required)

## 📝 Emoji Update Features

### What the updater does:
- ✅ Finds all 115 emoji IDs across 88+ files
- ✅ Updates them automatically
- ✅ Shows you which files were changed
- ✅ Preserves emoji names and animation

### Most common emojis to update:
- Error emoji: `<:asd:1408397481271627921>` (used 137+ times)
- Success emoji: `<:asdsw:1408397838857146470>` (used extensively)
- Alert emoji: `<:alert:1408398509882736651>` (used 137+ times)

## 🚀 Quick Emoji Update Workflow

1. **See all emojis:**
   ```bash
   python3 update_emoji_ids.py
   # Select option 3
   ```

2. **Update interactively:**
   ```bash
   python3 update_emoji_ids.py
   # Select option 1
   # Copy emoji, paste new ID
   ```

3. **Update in bulk:**
   - Edit `bulk_update_example.py`
   - Add your emoji mappings
   - Run: `python3 bulk_update_example.py`

## ⚠️ Important Notes

- **Backup**: The updater modifies files directly (safely)
- **Format**: Emoji IDs must be 17-19 digits
- **Testing**: Test bot after updating emojis
- **Token**: Don't share your Discord bot token

## 📚 Documentation Files

- `EMOJI_UPDATE_GUIDE.md` - Complete guide for updating emojis
- `emoji_reference.md` - All 115 emojis with descriptions
- `README.md` - Original bot readme
- `config.yml` - Bot configuration

## 🎉 You're All Set!

Start by updating your emoji IDs using the tools provided, then run your bot with the new emojis!
