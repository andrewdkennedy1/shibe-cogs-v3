import discord as E
from redbot.core import commands as A,Config,checks
import aiohttp
from redbot.core.utils.menus import menu,commands as A,DEFAULT_CONTROLS
B=getattr(A,'Cog',object)
class status(B):
	@A.command(pass_context=True)
	async def status(self,ctx,*,member=None):
		C=ctx;A=member;H=C.author;I=C.guild
		if not A:A=H
		F='None'
		for G in A.activities:
			if isinstance(G,E.CustomActivity):F=G
		D=str(A);D=A.nick if A.nick else D;B=E.Embed();B.title=D;B.colour=A.colour;B.add_field(name='Custom Status',value=F);B.set_thumbnail(url=A.avatar_url_as(static_format='png'));await C.send(embed=B)
