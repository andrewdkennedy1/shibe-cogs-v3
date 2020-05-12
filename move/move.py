import asyncio
import re
import io
import discord
from datetime import datetime
from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class move(commands.Cog):
    """Take your message here and move it over there"""

    @commands.command()
    async def move(self, ctx):
        """[p]move [messageID] [channelID]"""
        message_id = int(content.group(1))
        message_channel = int(content.group(2))

        target_channel = bot.get_channel(message_channel)
        target_message = await ctx.fetch_message(message_id)
        if target_message == None:
            await ctx.send(f'{ctx.message.author.mention}: The message specified does not exist.', delete_after=5)
            return

        if target_channel == None:
            await ctx.send(f'{ctx.message.author.mention}: The channel specified does not exist.', delete_after=5)
            return
        files = []
        for attachment in target_message.attachments:
            files.append(discord.File(fp=io.BytesIO(requests.get(attachment.url).content), filename=attachment.filename, spoiler=attachment.is_spoiler()))

        embed = discord.Embed(title='The message was originally sent at: %s' % (target_message.created_at.strftime('%Y/%m/%d %I:%M:%S %p')), description='', color=0x00ff00)
        embed.set_author(name=target_message.author.name, url=target_message.author.avatar_url, icon_url=target_message.author.avatar_url)
        embed.add_field(name='Message', value=target_message.content)
        await target_channel.send('', embed=embed, files=files)
        await target_message.delete()
        await ctx.send(f'{ctx.message.author.mention}: The message was successfully pushed down into {target_channel.mention}', delete_after=5)
        await ctx.message.delete()
