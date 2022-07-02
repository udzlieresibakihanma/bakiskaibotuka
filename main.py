import discord
from discord.ext import commands


client = commands.Bot(command_prefix = 'b.')



@client.event
async def on_ready():
	print("Bot Is Online")
 





@client.command()
async def ping(ctx):
	await ctx.send("Pong! ***51ms***")


@client.command()
async def clear(ctx, amount=100):
	await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await ctx.send("თქვენს მიერ მოპინგული ადამიანი გაიკიკა სერვერიდან ")
	await member.kick(reason=reason)



@client.command()
async def ban (ctx, member : discord.Member, *, reason=None):
	await ctx.send("თქვენს მიერ მონიშნულ ადამიანს დაედო ბანი")
	await member.ban(reason=reason)





@client.command(aliases=["prefixs"])
async def prefix (ctx): 
	await ctx.send("```Bot Prefix : b. ```")





















	

client.run('OTkxNzcxNzgxOTUyMTkyNjIz.GPA4ry.hjuZJDJdBbjAQjadvxh5OSAmYblyVu0qAcDzhw')






