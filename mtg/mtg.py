from redbot.core import commands as A
import asyncio,aiohttp as D,json,discord as B,re,time
class mtg(A.Cog):
	@A.command(pass_context=True)
	async def mtg(self,ctx,*,cardname):
		E=D.ClientSession();F=await E.get(url='http://api.scryfall.com/cards/named?',params={'fuzzy':cardname});A=await F.json()
		if A['object']=='error':await ctx.send(re.sub("\\(|\\'|,|\\)+",'',A['details']));return
		C=B.Embed(title='**{}**'.format(A['name']),url=A['scryfall_uri']);C.set_image(url=A['image_uris']['normal']);await ctx.send(embed=C)
	async def mtgrandom(self,ctx,*):
		E=D.ClientSession();F=await E.get(url='http://api.scryfall.com/cards/random');A=await F.json()
		if A['object']=='error':await ctx.send(re.sub("\\(|\\'|,|\\)+",'',A['details']));return
		C=B.Embed(title='**{}**'.format(A['name']),url=A['scryfall_uri']);C.set_image(url=A['image_uris']['normal']);await ctx.send(embed=C)