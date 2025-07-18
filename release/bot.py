import discord
from discord.ext import commands
import json
import os
import time

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents) #the prefix for before the commands

# Load products from JSON
with open("/path/to/products.json") as f:
    products = json.load(f)

# User data file
USER_DATA_FILE = "user_data.json"

# Load or create user data
if os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE) as f:
        user_data = json.load(f)
else:
    user_data = {}

COOLDOWN_SECONDS = 60 #The cooldown for getting exp from a message
EXP_PER_MESSAGE = 10 #The amount of exp per message
EXP_PER_LEVEL = 500 #The required amount of exp to level up

cooldowns = {}

def save_user_data():
    with open(USER_DATA_FILE, "w") as f:
        json.dump(user_data, f, indent=4)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}") #Message when you log in

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    user_id = str(message.author.id)
    now = time.time()

    # Cooldown check so users don't spam EXP
    if user_id in cooldowns and now - cooldowns[user_id] < COOLDOWN_SECONDS:
        await bot.process_commands(message)
        return

    cooldowns[user_id] = now

    # Init user data if not present
    if user_id not in user_data:
        user_data[user_id] = {"exp": 0, "level": 0, "tokens": 0}

    user = user_data[user_id]
    user["exp"] += EXP_PER_MESSAGE

    # Level up check
    required_exp = (user["level"] + 1) * EXP_PER_LEVEL
    if user["exp"] >= required_exp:
        user["level"] += 1 #the amount you level up when you reach required exp (recommended to not change)
        user["tokens"] += 1 #amount of tokens for leveling up
        user["exp"] -= required_exp
        await message.channel.send(
            f"🎉 Congrats {message.author.mention}, you leveled up to level {user['level']}! You earned 1 token." #custom message when someone levels up
        )

    save_user_data()

    await bot.process_commands(message)

@bot.command() #The entire embed when you run !xp
async def xp(ctx):
    user_id = str(ctx.author.id)
    if user_id not in user_data:
        await ctx.send("You have no data yet. Start chatting to gain EXP!") #custom message when user has no data
        return
    user = user_data[user_id]
    embed = discord.Embed(title=f"{ctx.author.display_name}'s Profile", color=0x00ffcc)
    embed.set_thumbnail(url=ctx.author.display_avatar.url)
    embed.add_field(name="Level", value=user["level"])
    embed.add_field(name="EXP", value=user["exp"])
    embed.add_field(name="Tokens", value=user["tokens"])
    await ctx.send(embed=embed)

@bot.command()
async def shop(ctx):
    embed = discord.Embed(
        title="🛒 Shop",
        description="Use !buy <number> to purchase!",
        color=0xffa500
    )

    for idx, product in enumerate(products, start=1):
        embed.add_field(
            name=f"{idx}. {product['name']} - {product['cost']} tokens",
            value=product["description"],
            inline=False
        )

    # Add clickable form link at the bottom
    embed.add_field(
        name="\u200b",  # invisible spacer
        value="You can also request to add your own product [here!](https://forms.gle/#)", #Feel free to replace to anything, this is just a extra
        inline=False
    )

    await ctx.send(embed=embed)


@bot.command()
async def buy(ctx, item_number: int):
    user_id = str(ctx.author.id)

    if user_id not in user_data:
        await ctx.send("You have no tokens! Chat to earn some first.") #Custom message when user has no tokens
        return

    if item_number < 1 or item_number > len(products):
        await ctx.send("Invalid product number!") #Custom message when user inputs invalid number in the !buy command
        return

    user = user_data[user_id]
    product = products[item_number - 1]

    if user["tokens"] < product["cost"]:
        await ctx.send(f"You don't have enough tokens to buy **{product['name']}**.") #Custom message when the user is to broke to buy a product (HAHA L. im broke too :sad:)
        return

    user["tokens"] -= product["cost"]
    save_user_data()

    await ctx.send(f"✅ You bought **{product['name']}** for {product['cost']} tokens!") #Custom message when user buys a product

    # Notify specific user about purchase if notify_user_id exists
    notify_user_id = product.get("notify_user_id")
    notify_message = product.get("notify_message")

    if notify_user_id and notify_message:
        user_to_notify = bot.get_user(int(notify_user_id))
        if user_to_notify:
            try:
                await user_to_notify.send(notify_message.replace("{buyer}", ctx.author.name))
            except Exception as e:
                print(f"Failed to send notification DM: {e}")

bot.run("YOUR_BOTS_SECRET") #Replace YOUR_BOTS_SECRET with your bots actual secret
