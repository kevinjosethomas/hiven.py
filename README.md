# hiven.py
📦 Opensource Python wrapper for Hiven's REST and WebSocket API

## Installation
```
pip install -U hiven.py
```

## Usage
hiven.py is currently under development (that's going pretty fast), we have the basic receive + send message functionality for (jank) commands though!

### Token
Hiven currently only supports selfbots so you'll need to get your Hiven token from the web application or the desktop client.
1. Open the web app or desktop client
2. Hit ``Ctrl+Shift+I`` to open Developer Tools
3. Navigate to the Console tab
4. Type in ``localStorage["hiven-auth"]``
5. Copy & paste the token in your code

![image](https://user-images.githubusercontent.com/46242684/131377552-1faefc2e-9f1b-4b66-913a-37c29bb7246a.png)

**Do not share this token with anybody**

### Quickstart
```py
import hiven
from hiven import Client

bot = Client(bot=False)  # set bot = True if you're controlling a bot account


@bot.event
async def on_ready():
    """Triggered when the bot is ready """
    
    print("hello world!")


@bot.event
async def on_message(message: hiven.Message):
    """Triggered when a message (that the bot can see) is sent"""

    if message.content.startswith("!hello"):
        await message.room.send("hey there!")  # respond to the message if it starts with !hello


bot.run(token="YOUR_TOKEN_HERE")
```

## Credits

- [hiven](https://hiven.io) - for providing such a great service for free
- [discord.py](https://github.com/Rapptz/discord.py) - for providing a easy-to-use structure that we continued in hiven.py
- [openhiven.py](https://github.com/Luna-Klatzer/openhiven.py) & [vhiven](https://github.com/insberr/vhiven) - for great http & websocket api documentation

- [Iapetus-11](https://github.com/Iapetus-11) - for consistently providing great tips for efficiency and code quality, and helping out all the time
