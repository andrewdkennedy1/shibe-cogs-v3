from redbot.core import commands
import asyncio, aiohttp, json
import discord, re, time


# Classname should be CamelCase and the same spelling as the folder
class mtg(commands.Cog):
    """mtg"""

    @commands.command(pass_context=True)
    async def mtg(self, ctx, *, cardname : str):
        """
        Fetches for a card.
        """
        session = aiohttp.ClientSession()

        resp = await session.get(url='http://api.scryfall.com/cards/named?', params={'fuzzy':cardname})
        card = resp.json()
        await ctx.send(card)