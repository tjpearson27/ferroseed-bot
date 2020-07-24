import discord
from discord.ext import tasks, commands
from Person import *
from discord.utils import get
from random import *
import argparse
import asyncio
import sys
import time

TOKEN = open("token.txt","r").readline()

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

extensions = ['RaidCommands']

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	channel = message.channel
	if message.guild is None:
		await message.channel.send("Hey there!")
	else:
	    await client.process_commands(message)

#Command used for bot admin to turn their bot off
#Please put the admin's discord ID where indicated
@client.command()
async def logout(ctx):
	if ctx.message.author.id in [138411165075243008]:
		await ctx.send('```Shutting down...```')
		await client.logout()
	else:
		await ctx.send('Nice try jackass!')
		
#Sends greet command
@client.command()
async def greet(ctx):
        await ctx.send("Hello everyone! I am Ferroseed and I'm here to assist you :)")

# Den commands
@client.command()
async def denlist(ctx):
        await ctx.send("<https://www.serebii.net/swordshield/maxraidbattledens.shtml>")

@client.command(pass_context=True)
async def den(ctx, number : int):
        id = ctx.message.author.id
        p = Person(id, ctx.message.channel, ctx.message.author)
        user = ctx.message.author.name
        if number >=1 and number <158:
                await ctx.send("<https://www.serebii.net/swordshield/maxraidbattles/den"+str(number)+".shtml>")
        else:
                await ctx.send("That's not a den, "+str(user)+"! <a:rowBop:734983435348869180>. Only from 1 to 157 <a:RowHype:734731466629578873>")
        
#@client.command(pass_context=True)
#async def newden(ctx):
#        i = randrange(157) + 1
#        newden = str(i)
#        await ctx.send("<https://www.serebii.net/swordshield/maxraidbattles/den"+newden+".shtml>")

@client.command()
async def newden(ctx, *args):
        if args:
                loc = args[0]
                if loc == "ioa":
                        i = randint(94, 157)
                elif loc == "swsh":
                        i = randint(1, 93)
        else:
                i = randrange(157)
        newden = str(i)
        await ctx.send("<https://www.serebii.net/swordshield/maxraidbattles/den"+newden+".shtml>")

# Caught, naught, pet
@client.command(pass_context=True)
async def caught(ctx):
        id = ctx.message.author.id
        p = Person(id, ctx.message.channel, ctx.message.author)
        embed = discord.Embed(
        colour = discord.Colour.green())
        embed.add_field(name=':tada: Caught!', value="<@"+str(id)+"> caught the pokemon!", inline=False)
        await ctx.send(embed=embed)
        await ctx.send("<a:RowHype:734731466629578873>")


@client.command(pass_context=True)
async def naught(ctx):
        id = ctx.message.author.id
        p = Person(id, ctx.message.channel, ctx.message.author)
        embed = discord.Embed(
        colour = discord.Colour.red())
        embed.add_field(name='<:sherbSad:732994987683217518> escaped', value="<@"+str(id)+"> did not catch the pokemon.", inline=False)
        await ctx.send(embed=embed)
        await ctx.send("<a:RWalkAway:734747213040975873>")

@client.command(pass_context=True)
async def pet(ctx):
        id = ctx.message.author.id
        p = Person(id, ctx.message.channel, ctx.message.author) 
        petpet = randrange(10)
        if petpet >= 6:
                embed = discord.Embed(
                colour = discord.Colour.green())
                embed.add_field(name='Ferroseed anticipated this', value="<@"+str(id)+"> pet Ferroseed! <:ferroHappy:734285644817367050>")
                await ctx.send(embed=embed)
        else:
                embed = discord.Embed(
                colour = discord.Colour.red())
                embed.set_author(name='Ouch!')
                embed.add_field(name='*Sorry!*', value="<@"+str(id)+"> got hurt by Iron Barbs <:sherbSad:732994987683217518>")
                await ctx.send(embed=embed)

# Go to sleep commands
@client.command()
async def absleep(ctx):
	if ctx.message.author.id in [138411165075243008]:
                embed = discord.Embed(
                colour = discord.Colour.green())
                embed.add_field(name='*Abdur is going to sleep*', value=":zzz: :zzz: :zzz:")
                await ctx.send(embed=embed)
	else:
                embed = discord.Embed(
                colour = discord.Colour.green())
                embed.add_field(name='ABDUR!!', value="Go to sleep! :zzz:")
                await ctx.send(embed=embed)



# Add custom commands over this
@client.command()
async def sleep(ctx, str):
        await ctx.send("Go to sleep, "+str+" <a:rowBop:734983435348869180>")

@client.command()
async def test(ctx):
	while True:
		print("Hello!")
		await asyncio.sleep(1)
		return
	
@client.command()
async def load(extension):
	try:
		client.load_extension(extension)
		print('Loaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be loaded. [{}]'.format(extension, error))

@client.command()
async def unload(extension):
	try:
		client.unload_extension(extension)
		print('Unloaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be unloaded. [{}]'.format(extension, error))

if __name__ == '__main__':
	for extension in extensions:
		try:
			client.load_extension(extension)
		except Exception as error:
			print('{} cannot be loaded. [{}]'.format(extension, error))

	#client.loop.create_task(test())
	client.run(TOKEN)
