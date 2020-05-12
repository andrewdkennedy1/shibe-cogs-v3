import asyncio

import discord

from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class move(commands.Cog):
    """Take your message here and move it over there"""

    @commands.command()
    async def move(self, ctx):
        """[p]move [messageID] [channelID]"""
        msg = "**Message from** {} ({})\n".format(
            message.channel.mention, message.channel.id
        )
        msg = "**Message sent by**: {} ({})\n".format(
            message.author.name, message.author.id
        )
        msg += "**Message content**:\n{}".format(message.content)
        await message_channel.send(msg)
        await message.delete()
