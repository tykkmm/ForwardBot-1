import asyncio
from os import environ
from pyrogram import Client 

class Bot(Client):
    def __init__(self):
        super().__init__
            name=SESSION,
            api_id=API_ID,
            bot_token=BOT_TOKEN, 
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        ) 
    async def start(self): 
        await super().start()
        me = await self.get_me() 
        self.mention = me.mention 
        self.username = '@' + me.username  
        logging.info(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️") 
        
    async def stop(self, *args): 
        await super().stop()
        logging.info("Bot stopped. Bye.")
        
app = Bot()
app.run()
        
        
