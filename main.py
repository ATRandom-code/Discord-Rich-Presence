import discord, threading, time
from pypresence import Presence

rich-presence-id = "" #rich presence id to your application
large-image-name = "" #large image name of your application for your 'game'
large-text = "" #large text next to the image
details-text = "" #the smaller text under the large text
lowest-text = "" #the lowest text underneath everything
button-label = "" #the text on the button in your activity status
url-link = "" #the url that the button redirects to

def clear(): #clear console
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

selfbot = commands.Bot(command_prefix=prefix, self_bot=True)
selfbot.remove_command('help')

@selfbot.event
async def on_connect():
    clear()
    print(f"Logged in as: {selfbot.user.name}#{selfbot.user.discriminator}")
    try:
        def run_task_in_background():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            RPC = Presence(rich_presence_id)
            RPC.connect()
            while True:
                RPC.update(
                    large_image=large_image_name,
                    large_text = large-text,
                    details= details-text,
                    state= lowest-text,
                    start=int(time.time()),
                    buttons=[{"label":button-label,"url":url-link}]
                )
                time.sleep(999999) #probably not the best way to do it, but i was doing this quickly and this works well, you do not want it to refresh often cuz then the time elapsed will restart
        threading.Thread(target=run_task_in_background, daemon=True).start() #daemon thread the task so that it runs in the background while waiting for selfbot commands
    except:
        clear()
        print("Discord not found") #you need to have the discord app on (or minimized in background) for this to work
       
@aa.event
async def on_message(message):
    if message.content.lower() == "!help":
        await message.delete()
        await message.channel.send("") #your help command
      
selfbot.run("") #token
