import asyncio
import re
import io
import discord
import requests
from datetime import datetime
from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class move(commands.Cog):
    """Take your message here and move it over there"""

    @commands.command(pass_context=True)
    async def move(self, ctx, message_id: int,message_channel: discord.TextChannel):
        """Notifies the sender. `[p]move [messageID] #Channel-Name`"""
        target_channel = ctx.bot.get_channel(message_channel.id)
        target_message = await ctx.fetch_message(message_id)
        if target_message is None:
            await ctx.send(f'{ctx.message.author.mention}: The message specified does not exist.', delete_after=5)
            return

        if target_channel is None:
            await ctx.send(f'{ctx.message.author.mention}: The channel specified does not exist.', delete_after=5)
            return
        files = [
            discord.File(
                fp=io.BytesIO(requests.get(attachment.url).content),
                filename=attachment.filename,
                spoiler=attachment.is_spoiler(),
            )
            for attachment in target_message.attachments
        ]
        embed = discord.Embed(
            title=f'Message moved from: {target_message.channel}',
            description='',
            color=0x00FF00,
        )
        embed.set_author(name=target_message.author.name, url=target_message.author.avatar_url, icon_url=target_message.author.avatar_url)
        embed.add_field(name='Message', value=target_message.content)
        await target_channel.send('', embed=embed, files=files)
        await target_message.delete()
        await ctx.send(f'{target_message.author.mention}: Your message was moved to {target_channel.mention}', delete_after=30)
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def silentmove(self, ctx, message_id: int,message_channel: discord.TextChannel):
        """Moves a message without any notifications `[p]silentmove [messageID] #Channel-Name`"""
        target_channel = ctx.bot.get_channel(message_channel.id)
        target_message = await ctx.fetch_message(message_id)
        if target_message is None:
            await ctx.send(f'{ctx.message.author.mention}: The message specified does not exist.', delete_after=5)
            return

        if target_channel is None:
            await ctx.send(f'{ctx.message.author.mention}: The channel specified does not exist.', delete_after=5)
            return
        files = [
            discord.File(
                fp=io.BytesIO(requests.get(attachment.url).content),
                filename=attachment.filename,
                spoiler=attachment.is_spoiler(),
            )
            for attachment in target_message.attachments
        ]
        embed = discord.Embed(
            title=f'Message moved from: {target_message.channel}',
            description='',
            color=0x00FF00,
        )
        embed.set_author(name=target_message.author.name, url=target_message.author.avatar_url, icon_url=target_message.author.avatar_url)
        embed.add_field(name='Message', value=target_message.content)
        await target_channel.send('', embed=embed, files=files)
        await target_message.delete()
        await ctx.message.delete()
