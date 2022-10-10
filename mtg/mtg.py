from redbot.core import commands
import asyncio, aiohttp, json
import discord, re, time


# Classname should be CamelCase and the same spelling as the folder
class mtg(commands.Cog):
    """Take your message here and move it over there"""

    @commands.command(pass_context=True)
    async def mtg(self, ctx, *, cardname : str):
        """
        Fetches for a card.
        """

        startTimer = time.monotonic()
        card = await self.getRequest(url='http://api.scryfall.com/cards/named?', params={'fuzzy':cardname})
        endTimer = time.monotonic()
        f = endTimer - startTimer

        if card['object'] == "error":
            await self.bot.say(re.sub(r'\(|\'|,|\)+', '', card['details']))
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
                await self.bot.say(embed=message)
            return

        message = discord.Embed(
            title="**{}**".format(card['name']),
            url=card['scryfall_uri'],
            color=discord.Color(0x1b6f9),
            description=""
        )

        message.set_footer(text="Fetch took: {} seconds.".format('%.3f' % f))
        message.set_image(url=card['image_uris']['normal'])
        await self.bot.say(embed=message)