import aiohttp
import asyncio
import logging

from redbot.core import commands

class randomfact(commands.Cog):
    """Gets a random fact."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__url: str = "https://uselessfacts.jsph.pl/random.json?language=en"
        self.__session = aiohttp.ClientSession()

    def cog_unload(self) -> None:
        if self.__session:
            asyncio.get_event_loop().create_task(self.__session.close())

    @commands.command()
    async def randomfact(self, ctx: commands.Context) -> None:
        """Gets a useless fact."""

        await ctx.trigger_typing()

        try:
            async with self.__session.get(self.__url) as response:
                fact = (await response.json())["text"]
                await ctx.send(fact)
        except aiohttp.ClientError:
            await ctx.send("I was unable to get a fact.")
