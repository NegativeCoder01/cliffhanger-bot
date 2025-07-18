# Cliffhanger Bot

The CliffHanger Discord Bot is a open source store/leveling sytem bot, it allows users to level up by typing more messages, getting tokens for each level, then spending those tokens in the shop. It also allows easy customization to add more products to the shop, to edit the cooldown, the exp per message, or the amount of exp needed to level up.

The default settings when you download it are set to:

Prefix: !

!shop: A command that shows all the avaliable products, their product number, and their price!
!buy <#>: A command that allows a user to buy a product by replacing <#> with the product number!
!xp: A command that allows users to see their level, their exp, and their tokens!
!help: A simple command that helps the user see what commands are avaliable!

Cooldown: 60
Exp per message: 10
Exp required to level up: 500
Tokens per level: 1


Since this project is open-source the owner of the server can edit the code anytime he wants, turn it into anything! And the way we set it up, the user can make the  bot however they want, custom profile picture, custom name, you name it (litteraly)!

# How to install

This should work on all operating systems. This requires a pc, OR you can use [termux](https://f-droid.org/packages/com.termux/) on mobile if you feel dangerous.

Step 1: Download the newest release [here](https://github.com/NegativeCoder01/cliffhanger-bot/releases/tag/0.1.0-rc.1) or choose from a list of releases [here](https://github.com/NegativeCoder01/cliffhanger-bot/tag/) any version should work unless said.

Step 2: Unzip the .Zip or .Tar.gz into any location you want

step 3: Add any products you want by editing the `products.json` file. You can copy and paste the entire field to make a new product.

Step 4: Customize the `bot.py` file anyway you want, there is comments in there that should guid you through what each customizable thing does.

Step 5: Setting up the bot.

First go to [Discord Developer Portal](https://discord.com/developers/applications) and log in.

In the top right you should see a `New Application` Button, click it.
What the button should look like:
![New Application Button](tutorial-assets/NewApp.png)

Choose any name you want, select a team (optional), then make sure to agree to [Developer ToS](https://support-dev.discord.com/hc/en-us/articles/8562894815383-Discord-Developer-Terms-of-Service) and [Developer Policy](https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy), Then press Create
![CreateApp](tutorial-assets/BobTheKing.png)

Customize how ever you want (optional)
![customize](tutorial-assets/bobthebroke.png)

Then press the bot button on the left to go to the bot section
It should look like this:
![fuggingbotssuck](tutorial-assets/lakebobpan.png)

Then look for the token, press reset token.
![kkk](tutorial-assets/kkk.png)
Verify it is you, and save your token somewhere where you won't lose it.

Once you have copied the token, go to the bottom of bot.py and replace `YOUR_BOTS_TOKEN` with Your Bots Actual Token
Save the file

After that open your terminal, then enter `pip install dicord.py`

Then go into your bot's folder, right click on `products.json` and click `copy path`
Then go into `bot.py` and look for `with open("/path/to/products.json") as f:`, and replace `/path/to/products.json` with the path you just copied.

After this right click the `bot.py` file and click `copy path`, then open terminal and enter `python /the/path/you/copied/`

Then once you run that it should say some thing like `Logged in as ExampleBot#1234` if so then its almost ready. Note: you must have this running for the bot to work, so if you stop the program it stops and has a potential loss of user data (exp, levels, tokens), so we recommend you run this on a device you can keep on constantly. We will hopefully come up with a solution in the future.

Then go back to the bot section in Discord Developer Portal and turn on the following:
`Presence Intent`, `Server Members Intent`, and `Message Content Intent`.

After this go back into Discord Developer Portal and go to the OAuth2 section
![REEEE](tutorial-assets/OFugginAuthentic69.png)

Under `OAuth2 URL Generator` click `bot` and `application.Commands`
Set the following permissions:
`Read Messages`, `manage messages`, `use slash commands`, `view channels`, `Use External Emojies`, `embed links`, `read message history`, and `mention everyone`.
Then set it as a guild install. Then copy the link and open the link, then add it to the server of your choosing.

After that, you are finished, time to test!
![FINALLY](tutorial-assets/fuuuuu.png)


Thank you for choose CliffHanger
![MOREIMAGES?!?!!?](CliffHanger.png)

<a href="https://account.venmo.com/u/MeIsNegative" target="_blank">
  <button>Want to support the creator? &#x2197;&#xfe0f;</button>
</a>

