# Discord Bot - Emoji ID Updater Project

## Overview
This project contains a Discord bot with a comprehensive emoji ID update system. The primary purpose is to help you easily update all emoji IDs throughout your Discord bot files.

## Current State
- ✅ Discord bot files extracted and organized
- ✅ Emoji updater tools created and tested
- ✅ 115 unique emojis identified across 97 files
- ✅ Interactive and bulk update modes available
- ✅ Web interface running successfully on port 5000
- ✅ Complete documentation created
- ⚠️ Discord bot requires TOKEN environment variable to run

## Recent Changes (October 9, 2025)
- Extracted Discord bot from zip file
- Created `update_emoji_ids.py` - Interactive emoji ID updater
- Created `bulk_update_example.py` - Bulk emoji ID updater template
- Created `emoji_reference.md` - Complete list of all 115 emojis
- Created `EMOJI_UPDATE_GUIDE.md` - Comprehensive update guide
- Created `README_SETUP.md` - Project setup instructions
- Tested emoji updater successfully

## Project Architecture

### Main Components
1. **Discord Bot** (`main.py`)
   - Discord.py based bot
   - Multiple cog modules for commands
   - Flask keep-alive server on port 8080
   - Requires Discord TOKEN to run

2. **Emoji Updater System**
   - `update_emoji_ids.py` - Main updater with interactive/bulk modes
   - `bulk_update_example.py` - Template for bulk updates
   - `test_emoji_updater.py` - Test script
   - `emoji_reference.md` - Complete emoji reference
   - `EMOJI_UPDATE_GUIDE.md` - User guide

3. **Bot Modules**
   - `cogs/commands/` - Command modules
   - `cogs/events/` - Event handlers
   - `cogs/moderation/` - Moderation tools
   - `utils/` - Utility functions
   - `db/` - Database files
   - `games/` - Game modules

### Key Files
- `main.py` - Bot entry point
- `requirements.txt` - Python dependencies
- `config.yml` - Bot configuration
- `status.py` - Status monitoring

## Emoji Statistics
- **Total Emojis**: 115 unique emojis
- **Files with Emojis**: 88+ Python files
- **Most Used Emojis**:
  - `<:asdsw:1408397838857146470>` - Success emoji (182 uses)
  - `<:asd:1408397481271627921>` - Error emoji (153 uses)
  - `<:alert:1408398509882736651>` - Alert emoji (138 uses)

## How to Use

### Update Emoji IDs (Primary Function)

#### Interactive Mode (Recommended for beginners):
```bash
python3 update_emoji_ids.py
# Select option 1, then follow prompts
```

#### Bulk Mode (For multiple emojis):
1. Edit `bulk_update_example.py`
2. Add your emoji mappings
3. Run: `python3 bulk_update_example.py`

#### List Only (View all emojis):
```bash
python3 update_emoji_ids.py
# Select option 3
```

### Run Discord Bot

**Prerequisites:**
- Discord bot TOKEN (set in Replit Secrets)

**Steps:**
1. Set TOKEN in Secrets
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python3 main.py`

## Environment Variables
- `TOKEN` - Discord bot token (required for bot to run)
- `SESSION_SECRET` - Available but not used by bot

## Dependencies
- discord.py - Discord API
- Flask - Keep-alive server
- Jishaku - Developer tools
- PyMongo - Database
- Wavelink - Music features
- See `requirements.txt` for complete list

## User Preferences
- None recorded yet

## Documentation
- `EMOJI_UPDATE_GUIDE.md` - Complete emoji update guide
- `emoji_reference.md` - All 115 emojis with descriptions
- `README_SETUP.md` - Setup and usage instructions
- `README.md` - Original bot documentation

## Notes
- The emoji updater is fully functional and tested
- Discord bot requires TOKEN to run
- Bot uses port 8080 for Flask keep-alive server
- Database uses MongoDB (connection string needed if using DB features)
