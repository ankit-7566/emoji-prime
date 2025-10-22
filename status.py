import discord
from discord.ext import commands, tasks
import asyncio

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 1385212481949012091
        self.message_id = None # Will store message ID after first send
        self.status_task.start()

    def cog_unload(self):
        self.status_task.cancel()

    @tasks.loop(seconds=30)
    async def status_task(self):
        channel = self.bot.get_channel(self.channel_id)
        if not channel:
            return

        uptime = discord.utils.utcnow() - self.bot.launch_time
        uptime_str = str(uptime).split('.')[0]  # Remove microseconds

        embed = discord.Embed(title="Code X Live Stats", color=0x2f3136)  # Default gray color

        # By default embed red & offline if bot not ready
        if not self.bot.is_ready():
            embed.color = 0xff0000  # Red
            embed.description = "**Status:** <a:status:1425819773278879775> Offline / Starting..."
        else:
            embed.color = 0x00ff00  # Green
            embed.description = "**Status:** <a:stats:1425819773278879775> Online"

            # Add stats only if online
            embed.add_field(name="Uptime <a:greencirclepa:1425823909223071795> ", value=uptime_str, inline=False)
            embed.add_field(name="Ping <:ping:1425822893761368096>", value=f"{round(self.bot.latency * 1000)} ms", inline=False)
            embed.add_field(name="Guilds <a:serverupdate:1425819773278879775>", value=str(len(self.bot.guilds)), inline=False)
            embed.add_field(name="Users <:members:1425822893761368096>", value=str(len(self.bot.users)), inline=False)
            embed.add_field(name="Commands <a:command:1425822893761368096>", value=str(len(self.bot.commands)), inline=False)  
            embed.add_field(name="Invite Link <:invite:1425823909223071795>", value="[Click Here](https://discord.com/api/oauth2/authorize?client_id=1362680985497636885&permissions=8&scope=bot)", inline=False)
            embed.add_field(name="Website <:website:1425822893761368096>", value="[Visit Code X](https://peacesecurity.netlify.app/)", inline=False)
            

        embed.set_footer(text="By Code X Team")
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.set_image(url="https://media.discordapp.net/attachments/1376132308419219486/1376453971170033787/a_0480347842c791592b4563ce7edc6030.gif?ex=68356228&is=683410a8&hm=fe5a65d43d13ec28c60949d244b4c0e6358d06461771af91fc44f01b35260bdf&=&width=287&height=161")

        # Send or edit message
        if self.message_id is None:
            msg = await channel.send(embed=embed)
            self.message_id = msg.id
        else:
            try:
                msg = await channel.fetch_message(self.message_id)
                await msg.edit(embed=embed)
            except discord.NotFound:
                # Message deleted, send new one
                msg = await channel.send(embed=embed)
                self.message_id = msg.id

    @status_task.before_loop
    async def before_status(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    # Store bot launch time for uptime calc
    bot.launch_time = discord.utils.utcnow()
    await bot.add_cog(StatusCog(bot))
