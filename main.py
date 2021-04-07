import discord
from discord.ext import commands
client = commands.Bot(command_prefix="%")

f = open('rules.txt', 'r')


@client.event
async def on_ready():
    print('All systems tested, operational and online')
#This is for anti swear#
@client.event
async def on_message(ctx, message):
    msg = message.content
    with open('badWords.txt') as BadWords:
        if msg in BadWords.read():
            await message.delete()
            await ctx.send("Dont use that word!")
        else:
            await ctx.process_commands(message)
#This clears messages#
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)
#This kicks members#
@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason = 'No reason provided'):
    await member.send('You have been kicked from the guild, because:'+reason)
    await ctx.channel.kick(reason=reason)
#This bans members#
@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason = 'No reason provided'):
    await member.send('You have been banned from the guild, because:'+reason)
    await ctx.channel.ban(reason=reason)

client.run('ODI1NzA4MTE2MDQwNDgyODc2.YGB2mw.D0GdV8sc7xYPt_ZmXHQpHNrcfT8')
