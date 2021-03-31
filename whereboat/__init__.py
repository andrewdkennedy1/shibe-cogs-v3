from redbot.core.bot import Red

from .whereboat import whereboat


def setup(bot: Red):
    bot.add_cog(whereboat())
