from redbot.core.bot import Red

from .randomfact import randomfact


def setup(bot: Red):
    bot.add_cog(randomfact())
