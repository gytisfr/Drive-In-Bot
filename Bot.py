#Drive-In Assistant ~ by ~ Gytis5089

#Imports
import discord
import asyncio
from discord.ext import commands
from discord.utils import get

#Vars
client = commands.Bot(command_prefix = ['+'], intents=discord.Intents.all())
client.remove_command('help')

#Def
def admin(ctx):
    return ctx.author.id in [301014178703998987, 667029055727599627, 476115454730043393, 299912060551299073]
    #Me

#Events
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Drive-In"))
    print('Drive-In Assistant now online!')
    print(f'Running with {round(client.latency * 100)}ms ping.')

@client.event
async def on_member_join(member):
    general = client.get_channel(960145661737721958)
    embed = discord.Embed(
        title="Welcome!",
        colour=0xffffff,
        description=f"{member.mention} has joined!"
    )
    embed.set_thumbnail(url="https://i.ibb.co/Ry3KLrx/Image.png")
    await general.send(embed=embed)

@client.event
async def on_message(msg):
    if msg.channel.id == 960210480595628062:
        await msg.delete()
    await client.process_commands(msg)

#Commands
@client.command()
async def verify(ctx):
    memberrole = ctx.guild.get_role(960209790066393099)
    if memberrole not in ctx.author.roles:
        await ctx.author.add_roles(memberrole)
        embed = discord.Embed(
            title="Verify",
            colour=0xffffff,
            description=f"{ctx.author.mention} has verified"
        )
        embed.set_thumbnail(url="https://i.ibb.co/Ry3KLrx/Image.png")
        logs = client.get_channel(960182173703479346)
        await logs.send(embed=embed)

@client.command()
@commands.check(admin)
async def grant(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(
        title="Grant",
        colour=0xffffff,
        description=f"{ctx.author.mention} has given {member.mention} the {role.mention} role"
    )
    embed.set_thumbnail(url="https://i.ibb.co/Ry3KLrx/Image.png")
    logs = client.get_channel(960182173703479346)
    await logs.send(embed=embed)

@client.command()
@commands.check(admin)
async def remove(ctx, member : discord.Member, role : discord.Role):
    await member.remove_roles(role)
    embed = discord.Embed(
        title="Remove",
        colour=0xffffff,
        description=f"{ctx.author.mention} has taken away the {role.mention} role from {member.mention}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/Ry3KLrx/Image.png")
    logs = client.get_channel(960182173703479346)
    await logs.send(embed=embed)

@client.command()
@commands.check(admin)
async def kick(ctx, member : discord.Member, *, reason):
    await member.kick(reason=reason)
    embed = discord.Embed(
        title="Kick",
        colour=0xffffff,
        description=f"{ctx.author.mention} has kicked {member.mention} for {reason}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/Ry3KLrx/Image.png")
    logs = client.get_channel(960182173703479346)
    await logs.send(embed=embed)

@client.command()
@commands.check(admin)
async def ban(ctx, member : discord.Member, *, reason):
    await member.ban(reason=reason)
    embed = discord.Embed(
        title="Ban",
        colour=0xffffff,
        description=f"{ctx.author.mention} has banned {member.mention} for {reason}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/Ry3KLrx/Image.png")
    logs = client.get_channel(960182173703479346)
    await logs.send(embed=embed)

@client.command()
@commands.check(admin)
async def say(ctx, channel : discord.TextChannel, *, message):
    await channel.send(message)

@client.command()
async def serverinfo(ctx):
    embed = discord.Embed(
        title="Server Info",
        colour=0xffffff,
        description=f"**Member Count:**{ctx.guild.member_count}\n**Server Creation:**{ctx.guild.created_at:%d/%m/%Y %H:%M:%S}"
    )
    embed.set_thumbnail(url="https://i.ibb.co/Ry3KLrx/Image.png")
    await ctx.send(embed=embed)

@client.command()
@commands.check(admin)
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        colour=0xffffff,
        description="`+grant {person} {role}`\n`+remove {person} {role}`\n`+kick {person} {reason}`\n`+ban {person} {reason}`\n`+say {channel} {message}`\n`+serverinfo`"
    )
    embed.set_thumbnail(url="https://i.ibb.co/Ry3KLrx/Image.png")
    await ctx.send(embed=embed)

@client.command()
@commands.check(admin)
async def rules(ctx):
    embed = discord.Embed(
        title="Rules",
        colour=0xffffff,
        description=""
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Text Channels",
        colour=0xffffff,
        description="1.Do not spam, this includes but is not limited to:\n> a)Words/characters/phrases\n> b)Emojis\n> c)Mentions\n2.Only speak in English\n3.No advertising\n4.While cursing is permitted, don't be excessive\n5.Respect all members and staff\n6.Do not impersonate famous influencers or staff members or anything else"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Voice Channels",
        colour=0xffffff,
        description="1.Don't earrape (your problem if you have a bad mic)\n2.Don't use a voice changer\n3.Don't play any music or anything else through your mic"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="General",
        colour=0xffffff,
        description="In general, use your brain, don't be over the top\nPlease refrain from offensive names/nicks and profile pics aswell"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Overall",
        colour=0xffffff,
        description="Please, just have a good time\nIf you couldn't tell, this server has the theme of a drive-in movie theatre\nRemember, mods have final say and can take any action if deemed necessary\nPerm invite link:https://discord.gg/Vx94dftpVa"
    )
    await ctx.send(embed=embed)

@client.command()
@commands.check(admin)
async def roles(ctx):
    embed = discord.Embed(
        title="Roles",
        colour=0xffffff,
        description=""
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Owner",
        colour=0x000000,
        description="<@&960184868585750638> - The creator and owner of the server"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Manager",
        colour=0xffffff,
        description="<@&960184895777423411> - All of the server's featured bots (all by Gytis!)"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Manager",
        colour=0x1F8B4C,
        description="<@&960185800362958939> - Leader of staff team"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Head Admin",
        colour=0xFF0000,
        description="<@&960184930304946286> - Highest ranked non-server-leading staff member"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Administrator",
        colour=0xE67E22,
        description="<@&960184912579805274> - High ranked, experienced staff member"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Junior Admin",
        colour=0xF1C40F,
        description="<@&960184992191905822> - New member within the highest set of staff members"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Head Mod",
        colour=0x71368A,
        description="<@&960185129609887805> - Staff member who has proven capable of leading"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Moderator",
        colour=0x206694,
        description="<@&960185107652681748> - Fairly well acquainted within the server and staff team"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Trial Mod",
        colour=0x11806A,
        description="<@&960185246530285709> - New member on the staff team"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Helper",
        colour=0xE67E22,
        description="<@&960532736345505912> - Server member who has volunteered to help other server members around (starting point for joining staff team) (has no adminstrative power)"
    )
    await ctx.send(embed=embed)
    embed = discord.Embed(
        title="Member",
        colour=0x6E97E6,
        description="<@&960209790066393099> - All members!"
    )
    await ctx.send(embed=embed)

#Run Token
client.run('OTYwMTgxMjg0NDQ4MTM3MzA3.YkmsgQ.w2smpRBWcuMI3pmYYdkIRcG0in8')