# Discord Bot Emoji IDs Reference

This file lists all emoji IDs currently used in your Discord bot.

## How to Update Emoji IDs

### Method 1: Interactive Mode (Recommended for beginners)
```bash
python3 update_emoji_ids.py
# Select option 1, then follow the prompts
```

### Method 2: Bulk Update (Recommended for multiple changes)
Create a Python script or edit `bulk_update_example.py`:

```python
from update_emoji_ids import bulk_update_emojis

emoji_mapping = {
    '<:asd:1408397481271627921>': 'YOUR_NEW_ID_HERE',
    '<:asdsw:1408397838857146470>': 'YOUR_NEW_ID_HERE',
    # Add more mappings as needed
}

bulk_update_emojis(emoji_mapping)
```

## All Emoji IDs in Your Bot

### Error/Alert Emojis
- `<:asd:1408397481271627921>` - Error emoji (used 137 times)
- `<:alert:1408398509882736651>` - Alert emoji (used 137 times)
- `<:asdsw:1408397838857146470>` - Success emoji (used extensively)

### Navigation/UI Emojis
- `<:arrow_left:1348340563610435594>` - Left arrow
- `<:arrow_right:1348340445708816494>` - Right arrow
- `<:arrow_left1:1368997542712574033>` - Left arrow variant
- `<:arrow_right1:1368997540334141562>` - Right arrow variant
- `<:arrow11:1348340609043398706>` - Arrow variant
- `<:delete:1348340540650950816>` - Delete button
- `<:delete_white:1377946250049228902>` - White delete button

### Server/Guild Emojis
- `<:boost:1348326410682372126>` - Server boost
- `<:booster:1274896054810312816>` - Server booster
- `<:crown:1404731688017330258>` - Crown
- `<a:crownn:1349244302802292787>` - Animated crown
- `<:Partnered:1219285024688443443>` - Discord Partner

### Member/User Emojis
- `<:member:1348326398929932388>` - Member
- `<:members:1348326443834146836>` - Members
- `<:members:1376167929481138196>` - Members variant
- `<:member_white_black:1417756145984209007>` - Member icon variant
- `<:robot:1348340531335270420>` - Bot/Robot
- `<:robot:894567890123456789>` - Bot variant

### Badge Emojis
- `<:Activedev:1219280536959189144>` - Active Developer
- `<:BadgeNitro:1274895915689443431>` - Nitro Badge
- `<:Balance:1219282289020637344>` - Balance Badge
- `<:Bravery:1219282462975201352>` - Bravery Badge
- `<:Brilliance:1219284165317361685>` - Brilliance Badge
- `<:Bugter:1219284193440436224>` - Bug Hunter
- `<:Early:1219284700292579328>` - Early Supporter
- `<:GoldenBugHunter:1274718350689304630>` - Golden Bug Hunter
- `<:HypeEvent:1219284814214205531>` - Hype Events
- `<:ModeratorProgamsAlumini:1274717806067187814>` - Moderator Alumni
- `<:Staff:1219285127444566056>` - Discord Staff
- `<:VERIFIED_BOT:1274718475583098982>` - Verified Bot
- `<:VerifiedBotDev:1219285243849080884>` - Verified Bot Developer
- `<:HTTP_INTERACTION_BOT:1274719023401013279>` - HTTP Interaction Bot
- `<:BarDiscord:1274718831352217620>` - Discord Bar

### Feature/Category Emojis
- `<:automod:1348326413912248432>` - Automod
- `<:automod2:1348340484241883206>` - Automod variant
- `<:automod2:1348889859632140298>` - Automod variant 2
- `<:fun:1407183872344719381>` - Fun category
- `<:game:1407183916149903373>` - Games category
- `<:games:1348326482241523742>` - Games
- `<:logg:1407184241866965062>` - Logging
- `<:mod:1348326431737909260>` - Moderation
- `<:utili:1408400343909269504>` - Utility
- `<a:gears:1261577892752789586>` - Settings/Gears (animated)

### Status/Info Emojis
- `<a:status:1376168960231215196>` - Status (animated)
- `<a:stats:1376168473406869645>` - Stats (animated)
- `<a:greencirclepa:1376167246321287249>` - Green circle (animated)
- `<:info:1348326490793840640>` - Info
- `<:tick:1408402912585056327>` - Tick/Check
- `<:Ztick:1222750301233090600>` - Z tick
- `<:ml_cross:1204106928675102770>` - Cross/X
- `<a:enabled:1349283415962157056>` - Enabled (animated)
- `<a:disabled:1349283526465421325>` - Disabled (animated)
- `<:enabled:1204107832232775730>` - Enabled

### Music Emojis
- `<:music:1348340499647430777>` - Music
- `<a:musica:1376420282478100511>` - Music (animated)
- `<a:MusicNotes:1412346391082041374>` - Music notes (animated)
- `<:Voice:1279464563150032991>` - Voice
- `<:mic:1348326446216515604>` - Microphone
- `<:spotify:1348326517507362917>` - Spotify

### Communication Emojis
- `<:mail:1348340617935065240>` - Mail
- `<:mail:1408396074544271422>` - Mail variant
- `<:mail1:1348340613636165712>` - Mail variant 2
- `<:msg:1348326387873873960>` - Message
- `<:channel:1306576564229767239>` - Channel

### Location/Server Info Emojis
- `<:earth:1348327194342199409>` - Earth
- `<:web_earth1:1348326509907017768>` - Web/Earth
- `<:location:1348326401505361920>` - Location
- `<:mapa:1257656719639707689>` - Map
- `<:home:1348326486511325256>` - Home
- `<:website:1378788763429244968>` - Website
- `<:invite:1378788896967491666>` - Invite

### Bot/System Emojis
- `<:ping:1376167777068650589>` - Ping
- `<:bot_latency:1417757705627504702>` - Bot latency
- `<:harmonia_cpu:1417757405298823168>` - CPU
- `<:ram:1417757183436656651>` - RAM
- `<:db:1408401496256680037>` - Database
- `<:python:1417756707790131260>` - Python
- `<:dev:1417756878863339602>` - Developer
- `<:system_user:1274718577185787954>` - System user

### Settings/Tools Emojis
- `<:setting:1348340711862571069>` - Settings
- `<:setting_tool:1348340497403613325>` - Settings tool
- `<:icons_settings:1099577554991583292>` - Settings icon
- `<:Tools:1417757956287496194>` - Tools
- `<:SageTrash:1417377638166827029>` - Trash

### Misc Emojis
- `<:gift:1348326523043840120>` - Gift
- `<:star:1408399782225117256>` - Star
- `<:ticket:1348340622154793041>` - Ticket
- `<:timer:1348340572586377326>` - Timer
- `<:circle2:1348326520581521469>` - Circle
- `<:snow1:1348326529129517067>` - Snow
- `<:hallow:1348340599803351080>` - Halloween
- `<:e_lesbian:1257104534300266577>` - Pride flag
- `<:atom:1348326466210889821>` - Atom
- `<:proton:1348340511303270461>` - Proton
- `<:medi:1408400624084586646>` - Medical
- `<:mem:1407184439976661187>` - Memory
- `<:x_folder2:1377946489296388147>` - Folder
- `<:ignore:1407184135595757642>` - Ignore
- `<:gw:1407183965605068922>` - Giveaway
- `<:3742:1363545422752383240>` - Custom emoji
- `<:660:1372187014446710835>` - Custom emoji
- `<:am:1407183418089017356>` - AM
- `<:New:1376453470596366419>` - New indicator
- `<:icons_stagemoderator:1099577483923292260>` - Stage moderator

### Animated Emojis
- `<a:dot:1407183814312202280>` - Dot (animated)
- `<a:loading:1205135543071940639>` - Loading (animated)
- `<a:maruloader:1407271356277456907>` - Loader (animated)
- `<a:command:1376168021234560000>` - Command (animated)
- `<a:diamond:1348872355031683084>` - Diamond (animated)
- `<a:serverupdate:1376167871008477294>` - Server update (animated)
- `<a:MATHS:1204235249916317697>` - Math (animated)

## Notes
- Emoji IDs are 17-19 digit numbers
- Format: `<:name:id>` for static, `<a:name:id>` for animated
- The name is just for readability, the ID is what Discord uses
- When updating, only change the ID number, keep the emoji name and animation prefix the same
