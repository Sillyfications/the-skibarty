#HUMAN SKIBIDI TOILET SKIBARTY BACKEND source code
#made by Sillyfications! 2023-2025
#check oute my pther stuff too! like project sillyfied!
#SMASH THAT LIKE BUTTON IF THIS WAS A FRICKIN' EPIC BOT!!!!11


import os
import random
from random import choice
import discord #discord.py
from discord.ext import commands 
from discord.interactions import Interaction
# from replit import db
from discord.ext.commands import cooldown, BucketType
import datetime
import time
from discord import app_commands
import math

# define a function to read the database file
def read_database(filename):
  print("Initalizing database file...")
  data = {}
  if os.path.exists(filename): # look for the database.txt file that is on the same dir as this script
    with open(filename, "r",encoding='latin-1') as file: #changed encoding to latin-1 due to an error
      print("Reading database file...")
      for line in file:
        key, value = line.strip().split("=", 1)#1
        data[key] = value
        print("Successfully read database file!")
  return data

# define a function to write the database file
def write_database(filename, data):
  with open(filename, "w", encoding='latin-1') as file:
    for key, value in data.items():
      file.write(f"{key}={value}\n")

# initialize the database
database_filename = "database.txt"
database = read_database(database_filename)



IgnoreImport = [] #isnt used anymore

intents = discord.Intents.all() #some fuckass update discord rolled out, i dont know what this actually does, i am like norm from the new norm FR!
client = commands.Bot(command_prefix="]", case_insensitive=True, intents=intents) #hey peter remember when this bot used PREFIXES???
client.remove_command("help")
allowed_server_ids = [ #lock servers from accessing the add command, these servers are allowed to execute the add command. future bot hosters can delete this to make the bot more public
    824410304103448618,
    1011318717939986492,
    1058111743601168394,
    1172262897662042266,
]
allowed_ids = [1011318717939986492] #i genuinely forgot what allowed ids did lol...

#command cooldown when adding. which is kind of useless since there is no way to copy a link and run the command in 2 seconds
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"You can't post just yet... {round(error.retry_after, 2)} seconds remaining")

        

@client.event
async def on_ready():
    print("its peanut butter jelly time")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="Skibidi Toilet"
        )
    )

@client.tree.command(name="skibidi", description="Posts Skibidi Toilet, what did you expect?")
async def skibidi(interaction: discord.Interaction):
    await interaction.response.send_message("https://media.discordapp.net/attachments/1011324879649394698/1165194116263591986/bot.resource.001.jpg")

@client.tree.command(name="hdtf", description="Posts a Hunt Down the Freeman quote.")
async def hdtf(interaction: discord.Interaction):
    quotes = [
        "You have my permission to die.",
        "Hero? Huh. You're talking to a villain, my dear. The hero inside of me died...many, many years ago when I was young.",
        "You fucked up my face.",
        "Ooh colonel, we are SO fucked.",
        "Stop touching me!",
        "game SUCKS i go to BED",
        "Black Messa",
        "I ain't nEVUH voted for this guy",
        "That's where you're wrong kiddo",
        "Spiders with vaginas",
        "Mitch, please... I-I can explain.",
        "Larry, for god's sake, shut the fuck up!",
        "He's cursed!",
        "No. God will stay away from this one.",
        "Where is our money, Berkan?",
        "#HL2_GameOver_Ally",
        "The aliens are coming! We have been compromised!",
        "Node graph is out of date. Rebuilding...",
        "We uploaded the wrong version",
    ]
    await interaction.response.send_message(choice(quotes))

@client.tree.command(name="home", description="The Human Skibidi Toilet Party homepage")
async def home(interaction: discord.Interaction):
    msg = len(database["skibarty"].split(",")) if "skibarty" in database else 0
    em = discord.Embed(
        title="The Human Skibidi Toilet Party",
        description=f"Currently serving {msg} posts!",
    )
    em.add_field(
        name="The Human Skibidi Toilet Party (also known as The Skibarty or just The Party) is a database where users can submit and request posts. Named after the most ~~shittiest~~ PEAK Youtube Shorts series of all time.",
        value="To start with browsing, use the random command `/random`. If you decide to submit something use the `/add` command. After you have submitted something. You will get a Post ID. With that ID you can use the `/search` command. The code is now open source! Check it oute here! https://github.com/Sillyfications/the-skibarty",
    )

    await interaction.response.send_message(embed=em)

def databaseUpdate(messageDatabase):
  if "skibarty" in database:
    database["skibarty"] = f"{database['skibarty']},{messageDatabase}"
  else:
    database["skibarty"] = messageDatabase
  write_database(database_filename, database)

@client.tree.command(name="random", description="Posts a random entry from the Skibarty")
async def random(interaction: discord.Interaction):
  if "skibarty" in database:
    messageDB = database["skibarty"].split(",")
    chunk = choice(messageDB)
    message = chunk.split("(-)")
    number = messageDB.index(chunk)
    
  print(f"Requested random post, sending postID {number} to user")
  await interaction.response.send_message(f"{message[0]}\nTag: {message[1]} - Posted on {message[3]} - {message[2]} hexadecimal - Takes {message[4]} bytes in storage - PostID: {number}")

@client.tree.command(
  name="old", description="Posts an old entry from the Beta Skibarty")

async def old(interaction: discord.Interaction):
  if "messageDB" in database:
    messageDB = database["messageDB"].split(",")
    awaitingMessage = choice(messageDB)
  await interaction.response.send_message(awaitingMessage)

@client.tree.command(name="search", description="Searches for a post in the Skibarty using the post ID")
@app_commands.describe(id="The ID of the post you are searching for.")
async def search(interaction: discord.Interaction, id: int):
  if id != None:
    number = int(id)
    chunk = database["skibarty"].split(",")[number]
    message = chunk.split("(-)")
    
   
    print(f"Requested search of postID {number}, sending post with tag {message[1]} to user")
    await interaction.response.send_message(f"{message[0]}\nTag: {message[1]} - Posted on {message[3]} - {message[2]} hexadecimal - Takes {message[4]} bytes in storage - PostID: {number}")
  else:
    await interaction.response.send_message("No ID provided")


@client.tree.command(name="list", description="Lists 10 entries with description")
@app_commands.describe(id="PostID to start listing")
async def search(interaction: discord.Interaction, id: int):
    if id is not None:
        # convert to int and calculate end index
        start_id = int(id)
        end_id = start_id + 9

        # placeholder for entries to be listed
        titlelist = []

        # get the size of the database
        dbsize = len(database["skibarty"])

        # check if the end_id exceeds the size of the database (this is bugged, oops too lazy to fix)
        if end_id > dbsize:
            await interaction.response.send_message("List exceeds available entries. Please try again with a lower ID value.")
            return

        # loop over the range of IDs 
        for number in range(start_id, end_id):
            chunk = database["skibarty"].split(",")[number]
            message = chunk.split("(-)")
            titlelist.append(f"PostID {number} - {message[1]}")

        # Ffrmat the output message 
        result_message = "\n".join(titlelist) #joohn FREEMAN??? from the hit series full life consequences???

        # Send the formatted result message
        await interaction.response.send_message(f"Listing PostIDs {start_id} to {end_id}:\n{result_message}")
    else:
        await interaction.response.send_message("Invalid ID. Please provide a valid PostID to start listing.")

    
    
  
@client.tree.command(name="add", description="Add a post to the Skibarty")
@app_commands.describe(text="String of text or image link you want to add.", tag="A small description.")
async def add(interaction: discord.Interaction, text: str, tag: str):
  if interaction.guild.id in allowed_server_ids:
    text = text.replace(",", ";")
    tag = tag.replace(",", ";")
    current_time = int(time.time())
    vote = hex(len(database["skibarty"].split(",")) +1)
    views = len(text) + len(tag)

    if text != None:
        databaseUpdate(text + "(-)" + tag + "(-)" + str(vote) + "(-)" +  "<t:" + str(current_time) + ":F>" + "(-)" + str(views))
        cmdtime = (
            str(datetime.datetime.today())
            .replace("-", "/")
            .split(".")[0]
            + " (UTC)"
        )
        num = len(database["skibarty"].split(","))
        idis = num - 1
        print(f"Adding post number to database.")
        await interaction.response.send_message(
            f"<:TF2_votekick_OK:1166483033596100719> Quote added to database. Your post ID is {idis} with the description of: {tag}."
        )
            
            #this is basically useless since this uses slash comms now... if there are people who want to use prefixes again. there you go! very cool easter eggs!
    else:
        notext = [
            "<:TF2_votekick_F2:1166789537159188551> You forgot to add your text, epic fail! (Forgot to add arguments)",
            "<:TF2_votekick_F2:1166789537159188551> Ooooo... you have to put text or image links, if you don't want to...  Cry about it! (Forgot to add arguments)",
            "<:TF2_votekick_F2:1166789537159188551> #HST_NoArguments_Database_03 (Forgot to add arguments)",
            "<:TF2_votekick_F2:1166789537159188551> void CDatabase::NoArgumentsErrorMessage() (Forgot to add arguments)",
            "<:TF2_votekick_F2:1166789537159188551> Cope, seethe, cry about it. You are not as cool as me. (Forgot to add arguments)",
            "<:TF2_votekick_F2:1166789537159188551> Half-Life 1 Announcer: PLEASE TRY AGAIN WITH TEXT OR IMAGE LINK. (Forgot to add arguments)",
            "<:TF2_votekick_F2:1166789537159188551> this bot SUCKS, i go to BED (Forgot to add arguments)",
            "<:TF2_votekick_F2:1166789537159188551> average_among_life_player.mp4 (Forgot to add arguments)",
            "<:TF2_votekick_F2:1166789537159188551> Let me get straight to the point. You do NOT have that skibidi ohio sigma rizz added after the command. (Forgot to add arguments)",
            "<:TF2_votekick_F2:1166789537159188551> You have my permission to die. (Forgot to add arguments)",
        ]
        await interaction.response.send_message(choice(notext))
  else:
    await interaction.response.send_message("This command is not allowed in this server.")

@client.tree.command(name="ping", description="Posts latency in ms.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Latency {round(client.latency * 1000)}ms")

@client.tree.command(name="wiki", description="Searches for a Wikipedia article")
@app_commands.describe(wiki="Search query (Case sensitive!)")
async def search(interaction: discord.Interaction, wiki: str):
  wiki = wiki.replace(" ", "_")
  wiki = wiki.replace("&", "%26")
  await interaction.response.send_message(content=f"https://en.wikipedia.org/wiki/{wiki}")
  

client.run("veryvcooltokeneen!getyourownatwww.discord.com/developers/applications") #put your own bot token here
keys = database.keys()