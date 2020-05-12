from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class move(commands.Cog):
    """[p]move [messageID] [channelID]"""

    @commands.command()
    async def move(self, ctx):
        """[p]move [messageID] [channelID]"""
        # Your code will go here
        await ctx.send("I like to move it , move it!")
