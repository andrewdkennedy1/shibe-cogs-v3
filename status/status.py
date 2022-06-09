import discord as B
from redbot.core import commands as A,Config,checks
import aiohttp
from redbot.core.utils.menus import menu,commands as A,DEFAULT_CONTROLS
C=getattr(A,'Cog',object)
class status(C):
	@A.command(pass_context=True)
	async def status(self,ctx,*,member=None):
		author=ctx.author;guild=ctx.guild
		if not member:member=author
		status_string='No Custom Status Dectected'
		for s in member.activities:
			if isinstance(s,B.CustomActivity):status_string=s
		name=str(member);name=member.nick if member.nick else name;embed=B.Embed();embed.title=name;embed.colour=member.colour;embed.add_field(name='Custom Status',value=status_string);embed.set_thumbnail(url=member.avatar_url_as(static_format='png'));await ctx.send(embed=embed)
