from redbot.core import commands
import asyncio, aiohttp, json
import discord, re, time


# Classname should be CamelCase and the same spelling as the folder
class mtg(commands.Cog):
    """Take your message here and move it over there"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    async def getRequest(self, url, **kwargs):
        async with self.aiohttp_session.get(url, **kwargs) as response:
            return await response.json()
            
    @commands.command(pass_context=True)
    async def mtg(self, ctx, *, cardname : str):
        """
        Fetches for a card.
        """
        card = await self.getRequest(url='http://api.scryfall.com/cards/named?', params={'fuzzy':cardname})

        if card['object'] == "error":
            await ctx.send(re.sub(r'\(|\'|,|\)+', '', card['details']))
            return

        if 'card_faces' in card:
            for entry in card['card_faces']:
                message = discord.Embed(
                    title="**{}**".format(entry['name']),
                    url=card['scryfall_uri'],
                    color=discord.Color(0x1b6f9)
                )
                message.set_image(url=entry['image_uris']['normal'])
                message.set_footer(text="Fetch took: {} seconds.".format('%.3f' % f))
                await ctx.send(embed=message)
            return

        message = discord.Embed(
            title="**{}**".format(card['name']),
            url=card['scryfall_uri'],
            color=discord.Color(0x1b6f9),
            description=""
        )

        message.set_footer(text="Fetch took: {} seconds.".format('%.3f' % f))
        message.set_image(url=card['image_uris']['normal'])
        await ctx.send(embed=message)