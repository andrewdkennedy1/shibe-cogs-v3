from redbot.core.bot import Red

from .villager import villager


def setup(bot: Red):
    bot.add_cog(villager())
