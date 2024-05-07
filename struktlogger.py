import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
badwords = ['fuck', 'hure', 'hurensohn', 'arschloch', 'fick', 'nigger', 'nigga', 'niga']
ipTrigger = ['ip', 'adresse', 'join', 'beitreten']


@client.event
async def on_ready():
    print(f'StruktLoggerv1 has been logged in as {client.user.name}.')
    print('----------------------------------------')
    embed = discord.Embed(title="StruktLoggerv1", description="Successfully logged in and started logging!",
                          color=0x00ff00)
    channel = client.get_channel(1182802909918924851)
    await channel.send(embed=embed)
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="mit den Logs"))


@client.command()
async def logs(ctx):
    embed = discord.Embed(title="StruktLoggerv1 Logs", description="All logged events are listed below.",
                          color=0x00ff00)
    embed.add_field(name="Message Delete", value="Sends an embed everytime a message has been deleted and the message "
                                                 "content.", inline=False)
    embed.add_field(name="Member Joined", value="Sends an embed with the name and ID of the User", inline=False)
    embed.add_field(name="Member Leave", value="Sends an embed with the name and ID of the User", inline=False)
    embed.set_footer(text="Mehr kommt bald...", icon_url="https://imgur.com/a/yuNiIDP")
    await ctx.send(embed=embed)


@client.event
async def on_message_delete(message):
    channel = client.get_channel(1182802909918924851)
    embed = discord.Embed(title="Message deleted", description=f"{message.author.name}'s Nachricht wurde gelöscht.",
                          color=0xfc0303)
    embed.add_field(name="Nachricht:", value=message.content, inline=False)
    await channel.send(embed=embed)


@client.event
async def on_member_join(member):
    channel = client.get_channel(1182802909918924851)
    embed = discord.Embed(title="Member joined", description=f"**Name: {member.name}**", color=0x00ff00)
    embed.add_field(name="ID", value=member.id, inline=False)
    await channel.send(embed=embed)


@client.event
async def on_member_remove(member):
    channel = client.get_channel(1182802909918924851)
    embed = discord.Embed(title="Member left", description=f"**Name: {member.name}**", color=0x00ff00)
    embed.add_field(name="ID", value=member.id, inline=False)
    await channel.send(embed=embed)


@client.event
async def on_message(message):
    content = message.content
    if message.author == client.user:
        return
    for word in badwords:
        if word in content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention} no badwords", delete_after=5)
            channel = client.get_channel(1182802909918924851)
            embed = discord.Embed(title="Bad Word detected",
                                  description=f"Autor: {message.author.name} ({message.author.id})", color=0xfc0303)
            embed.add_field(name="Kontext: ", value=content)
            await channel.send(embed=embed)
            return


@client.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    contentBefore = before.content
    contentAfter = after.content
    embed = discord.Embed(title="Message edited", color=0x05fab0)
    embed.add_field(name="Content Before", value=contentBefore, inline=True)
    embed.add_field(name="Content After", value=contentAfter, inline=True)
    channel = client.get_channel(1182802909918924851)
    await channel.send(embed=embed)


@client.event
async def on_reaction_add(reaction):
    embed = discord.Embed(title="Reaction added", color=0x05fab0)
    embed.add_field(name="Reaction", value=reaction, inline=False)
    channel = client.get_channel(1182802909918924851)
    await channel.send(embed=embed)


@client.event
async def on_reaction_remove(reaction):
    embed = discord.Embed(title="Reaction removed", color=0x05fab0)
    embed.add_field(name="Reaction", value=reaction, inline=False)
    channel = client.get_channel(1182802909918924851)
    await channel.send(embed=embed)


client.run('TOKEN')
