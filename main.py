import discord
import os
import time
import discord.ext
from discord_slash import SlashCommand
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check, MissingPermissions

#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = 'c?', help_command=None)

@client.event
async def on_ready():
  print("bot online")

  await client.change_presence(
  status = discord.Status.online, 
  activity = discord.Streaming(
    name = "Coffee", 
    url = "https://www.youtube.com/watch?v=Nid2HId9EVY"
    )
  ) 

@client.command(name="cool")
async def on_message(message):
  embedVar = discord.Embed(title="invite", description="The Invite For Coffee Shop Is https://discord.gg/tjtuafjNnf And A Other Very Smexy Server Is https://discord.gg/RwdXXSMxVx")

@client.command(name="bugreport", aliases=['br', 'bugr', 'breport'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def br(ctx, *, text=None):

  channel = client.get_channel(893485619869798420)
  await channel.send(f'({ctx.author.id}) {ctx.message.author} has reported a suspected bug: {text}')

  await ctx.reply("Thank you for Filing a Bug Report!")

@client.event
async def on_command_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This Command is in Cooldown! use it in {round(error.retry_after, 2)}')

@client.command(name="announcement", aliases=['ann'])
@commands.cooldown(1, 7, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def ann(ctx, *, message):

  await ctx.reply("Announcement has been sent in <#909270775117275159>!")
  channel = client.get_channel(909270775117275159)
  await channel.send(message)

@ann.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.event
async def on_command_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This Command is in Cooldown! use it in {round(error.retry_after, 2)}')

@client.command(name="dm", pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def dm(ctx, user: discord.User, *, message=None):
  message = message or "Hello!"
  try:
    await user.send(message)
    await ctx.reply(f"User has been DMed Successfully")
  except:
    await ctx.reply(f"User cannot be DMed")

@dm.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await message.delete()
      await ctx.reply("You do not have Permissions to use this Command!")

@client.command(name="suggest", aliases=['sug', 's'])
@commands.cooldown(1, 130, commands.BucketType.user)
async def suggest(ctx, *, text=None):

  channel = client.get_channel(937453991686701116)
  await channel.send(f'({ctx.author.id}) {ctx.message.author} has Suggested: {text}')

  await ctx.reply("Your Suggestion has been Sent!")

@client.event
async def on_command_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This Command is in Cooldown! use it in {round(error.retry_after, 2)}')

@client.command(name="repeat",aliases=['say'])
@commands.has_permissions(administrator=True)
async def speak(ctx, *, text):
    message = ctx.message
    await message.delete()

    await ctx.send(f"{text}")

@speak.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("You do not have Permissions to use this Command!")  

@client.command(name="purge", pass_context=True, aliases=['p'])
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        message = ctx.message
        await message.delete()

  
        await ctx.channel.purge(limit=limit)
        embedVar = discord.Embed(title="Purge Detected", description=f"Message(s) has been Purged by {ctx.message.author}", color=2552230)                                      
        await ctx.channel.send(embed=embedVar)

@client.event
async def on_command_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This Command is in Cooldown! use it in {round(error.retry_after, 2)}')

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.command(name="membercount", aliases=['mc'])
async def membercount(ctx):
  embedVar = discord.Embed(title=f"Hello! {ctx.author}, this is the Total Members in {ctx.guild.name}", description=f"{ctx.guild.member_count}", color=2552230)
  await ctx.reply(embed=embedVar)

@client.command(name="mute")
@commands.has_permissions(administrator=True)
async def mute(ctx, user : discord.Member,*, reason=None):
  
    guild = ctx.guild
    role = ctx.guild.get_role(931585327343226900)

    await user.add_roles(role)

    embedVar = discord.Embed(title="User has been Muted", description=f"{user.mention} has been muted by {ctx.author.mention} with the reason: {reason}", color=2552230)                                      
    await ctx.send(embed=embedVar)
    try:
      await user.send(f"you have been muted in {ctx.guild.name} with the Reason: {reason}")
  
    except:
      await ctx.send(f"cannot dm {user.mention}")

@mute.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.command(name="unmute")
@commands.has_permissions(administrator=True)
async def unmute(ctx, user : discord.Member):
  guild = ctx.guild
  role = ctx.guild.get_role(931581016815063132)

  await user.remove_roles(role)

  embedVar = discord.Embed(title="User has been Unmuted", description=f"{user.mention} has been unmuted by {ctx.author.mention}", color=2552230)                                      
  await ctx.send(embed=embedVar)

@unmute.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.command(name="approve-suggestion", aliases=['approve-s', 'a-suggestion', 'a-s'])
@commands.has_permissions(administrator=True)
async def approves(ctx, user : discord.User): 
  embedVar = discord.Embed(title="Suggestion Approval", description=f"Suggestion approved by {ctx.message.author}", color=2552230)
  try:
    await user.send(embed=embedVar)
    await ctx.send("Approval Sent!")
  except:
    await ctx.send(f"cannot dm {user.mention}")
 
@approves.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.command(name="deny-suggestion", aliases=['deny-s', 'd-suggestion', 'd-s'])
@commands.has_permissions(administrator=True)
async def denys(ctx, user : discord.User):
  embedVar = discord.Embed(title="Suggestion Denial", description=f"Suggestion denied by {ctx.message.author}", color=2552230)                                      
  try:
    await user.send(embed=embedVar)
    await ctx.send("Denial Sent!")
  except:
    await ctx.send(f"cannot dm {user.mention}")

@denys.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.command(name="embed-announcement", aliases=['e-ann', 'embed-ann', 'e-announcement'])
@commands.cooldown(1, 7, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def ann(ctx, *, message):

  await ctx.reply("Embedded Announcement has been sent in <#883671798456156170>!")
  channel = client.get_channel(883671798456156170)
  embedVar = discord.Embed(title=f"Brief Announcement by {ctx.message.author}", description=f"{message}", color=2552230)
  await channel.send("<@931578280392400936>")
  await channel.send(embed=embedVar)

@ann.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.event
async def on_command_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This Command is in Cooldown! use it in {round(error.retry_after, 2)}')

@client.command(name="help")
async def help(ctx):
  embedVar = discord.Embed(title="Commands", description="help - (shows this message)", color=2552230)
  embedVar.add_field(name="_ _", value="about - (shows a about the bot embed)")
  embedVar.add_field(name="_ _", value="announcement - c?announcement <your message here>")
  embedVar.add_field(name="_ _", value="embed-announcement - c?embed-announcement <your message here>")
  embedVar.add_field(name="_ _", value="approve-suggestion - c?aprove-suggestion <user>")
  embedVar.add_field(name="_ _", value="deny-suggestion - c?deny-suggestion <user>")
  embedVar.add_field(name="_ _", value="suggest - c?suggest <your suggestion>")
  embedVar.add_field(name="_ _", value="bugreport - c?bugreport <bug>")
  embedVar.add_field(name="_ _", value="dm - c?dm <user> <your message here>")
  embedVar.add_field(name="_ _", value="membercount - (sends a embedded membercount)")
  embedVar.add_field(name="_ _", value="mute - c?mute <user> <reason>")
  embedVar.add_field(name="_ _", value="unmute - c?unmute <user>")
  embedVar.add_field(name="_ _", value="ping - (sends the message pong)")
  embedVar.add_field(name="_ _", value="repeat - c?repeat <your message here>")
  embedVar.add_field(name="_ _", value="purge - c?purge <amount>")
  embedVar.add_field(name="_ _", value="qna - c?qna <question>")
  embedVar.add_field(name="_ _", value="ban - c?ban <user>")
  embedVar.add_field(name="_ _", value="unban - c?unban <user id>")
  embedVar.add_field(name="_ _", value="kick - c?kick <user> <reason>")
  embedVar.add_field(name="_ _", value="embed-repeat - c?embed-repeat <text>")
  embedVar.add_field(name="_ _", value="say - c?say <text>")

  await ctx.reply(embed=embedVar)

@client.command(name="qna")
@commands.cooldown(1, 30, commands.BucketType.user)
async def qna(ctx, *, message):

  await ctx.reply("Your Question has been Sent And Should Be Answerd As Soon As Posible.")
  channel = client.get_channel(894471254352990258)
  embedVar = discord.Embed(title=f"a Question by {ctx.message.author}", description=f"{message}", color=2552230)
  await channel.send(embed=embedVar)
  
@client.event
async def on_command_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This Command is in Cooldown! use it in {round(error.retry_after, 2)}')

@client.command(name="ban")
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *, reason=None):
  try:
    await user.ban(reason=reason)
    await ctx.reply("User has been Banned. L + Raito.")
  except:
    await ctx.reply("User cannot be Banned. Do They Have A Higher Role?")

@ban.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command! If You Think This Is A Error Please Report It With **c?bugreport**.")

@client.command(name="unban")
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member_id: int):
  try:
    await ctx.guild.unban(discord.Object(id=member_id))
    await ctx.reply("User has been Unbanned.")
  except:
    await ctx.reply("User cannot be Unbanned. Do You Have The Perms To Unban?")

@unban.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command!")

@client.command(name="kick")
@commands.has_permissions(administrator = True)
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *, reason=None):
  try:
    await user.kick(reason=reason)
    await ctx.reply("User has been Kicked.")
  except:
    await ctx.reply("User cannot be Kicked. do You Have The Perms?")

@kick.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command! If You Think This Is A Error Please Report It With **c?bugreport** And It Will Be Fixed.")

@client.command(name="embed-repeat",aliases=['e-repeat', 'embed-say', 'e-say'])
@commands.has_permissions(administrator = True)
async def embeddedsaycommand(ctx, *, text):
  message = ctx.message
  await message.delete()

  embedVar = discord.Embed(title=f"Embed by {ctx.message.author}", description=f"{text}", color=2552230)
  await ctx.send(embed=embedVar)

@embeddedsaycommand.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.message.author.mention} You do not have Permissions to use this Command! If You Think This Is A Error Please Report It With **c?bugreport** And It Will Be Fixed.")

client.sniped_messages = {}
  
@client.event
async def on_message_delete(message):
  client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
    
@client.command(name="snipe", aliases=['sn', 'deleted'])
async def snipe(ctx):
  try:
    contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
        
  except:
    await ctx.channel.send(f"{ctx.author.mention} No Messages to Snipe in <#{channel_id}>! ")
    return
  embed = discord.Embed(description=contents,
                        color=ctx.author.color,
                        timestamp=time)
  embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
  embed.set_footer(text=f"Message deleted in #{channel_name}")
    
  await ctx.send(embed=embed)

@client.command(name="whats-next")
async def wn(ctx):
  embedVar = discord.Embed(title="What's next for Us?", description="Coffee Shop Bot will be Actively Updated or Revamped.")
  await ctx.reply(embed=embedVar)

@client.event
async def on_messageo(message):
  if message.content == 'faggot':
    await message.reply("woah calm down buster brown")

@client.command()

@client.event
async def on_messaget(message):
  if message.content == 'Faggot':
    await message.reply("woah calm down buster brown.")

@client.command(name="test2")
async def test2(ctx):
  kill = [ ' ded  ', '  ded2 ' ]
  await ctx.reply(f"{random.choice(kill)}")

@client.event
async def on_messaget(message):
  if message.content == 'Faggot':
    await message.reply("woah calm down buster brown.")



#error and thedrcreeper were here.

client.run('OTQwMDQyMjk5OTczNDYwMDQ4.YgBonQ.32q2vYSOML3pyArFNbFmnvtu8Os')