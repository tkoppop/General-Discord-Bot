import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('Invalid command used.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error,commands.MissingRequiredArguments):
        await ctx.send('Please specify an amount of message to delete.')

@client.command()
async def kick(ctx,member : discord.Member, *, reason=None):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx,member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')    

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

            


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt',
                'Yes - definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'The outlook is good',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now',
                'Cannot predict now.', 
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run('')