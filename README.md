# hiven.py
📦 Opensource Python wrapper for Hiven's REST and WebSocket API

## Installation
```
pip install -U hiven.py
```

## Usage
hiven.py is currently under development (that's going pretty fast), we have the basic receive + send message functionality for (jank) commands though!

### Quickstart
```
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
- [openhiven.py](https://github.com/Luna-Klatzer/openhiven.py) - for great websocket api documentation
- [vhiven](https://github.com/insberr/vhiven) - for more great http api documentation

- [Iapetus-11](https://github.com/Iapetus-11) - for consistently providing great tips for efficiency and code quality, and helping out all the time
