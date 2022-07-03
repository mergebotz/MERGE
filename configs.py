# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID", '7651392')
    API_HASH = os.environ.get("API_HASH", 'db62aa57ef8162bb4c95d0cf81e1c09b')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '1907000957:AAFT2UzNd7i8gNZYnpsUjQX1PG_edWgs738')
    SESSION_NAME = os.environ.get("SESSION_NAME", "DKMERGEBOT")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", '-1001287353197')
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", '-1001514043208')
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", '5'))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", '5'))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", '31545dfcad86132fd47b')
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", '2drxdW7FZJ8M')
    MONGODB_URI = os.environ.get("MONGODB_URI", 'mongodb+srv://Watermarks:786@cluster0.v1ah9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", 'False'))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", '1805398747'))

    START_TEXT = """
**Hello {}, I'm a Simple Video Merger Bot!
I can Merge Multiple Videos into One Video, Generate ScreenShots, Generate Sample Video and many extra features....!

Configure The Settings Before using meh...!
Check Below Buttons for more..! 

🤖 Developer : [Anonymous](https://t.me/DKBOTZHELP)**
"""
    ABOUT_TEXT = """
**● Developed By : [This Person](https://t.me/DKBOTZHELP)
● Updates Channel : [DK BOTZ](https://t.me/DKBOTZ)
● Support : [DK BOTZ Support](https://t.me/DK_BOTZ)
● Language : [Python 3](https://www.python.org)
● Library : [Pyrogram](https://docs.pyrogram.org)
● Server : [Heroku](https://heroku.com)

©️ Made By @DKBOTZ ❤️**
"""

    HELP_TEXT = """**Hello {}, It's too easy to use me..**
 
**● Configure the Settings before using me... 
● Send a photo to set it as your custom thumbnail...
● Send videos to merge accordingly...**
  __- Atleast 2 Videos to be sent to merge
  - The video formats should be mp4, mkv or WebM
  - The videos should have proper file name__
  
**● If you are done with sending medias, Click "🔀 Merge Now" to merge
● That's it, and rest is mine work...

© By @DKBOTZ ❤️**
"""
    
    CAPTION = "**__© Merged By @DKBOTZ ❤️__**"
    PROGRESS = """
**● Percentage : {0}%**
**● Done: {1}**
**● Total: {2}**
**● Speed: {3}/s**
**● ETA: {4}**
"""
