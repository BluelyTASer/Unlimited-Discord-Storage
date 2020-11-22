# Unlimited Discord Storage
Unlimited Discord Storage is a project that leverages Discord's 8 MB Limit for unlimited storage space.

## Recommended Python Version
Above or equal than Python 3.9

## How much does it take me to develop this?
4 Days.

## How it Works
Unlimited Discord Storage takes advantage of Discord's 8 MB Limit, which states that there's no limit between files uploaded per minute or hour. Unlimited Discord Storage splits files larger than 8 MB by 8 MB then uploads them to discord, when downloading files larger than 8 MB uploaded from discord to your computer, Unlimited Discord Storage stitches parts of files into one file then the single file will appear to your computer meaning that you can use Discord as unlimited storage!

## Setup

1 - Run `python -m pip install -U discord.py` then run `pip3 install nest_asyncio`

2 - Create a discord server.

3 - Create 2 channels on a created discord server.

4 - Create an application from https://discord.com/developers/applications

5 - Create a bot from created application.

6 - Copy Discord Bot Token then invite Discord bot to your discord server.

7 - Clone the Unlimited Discord Storage Git repository.

8 - Run unlimiteddiscordstorage.py

9 - Paste Discord Bot Token that you copied from earlier and press enter.

10 - Type Channel Name for viewing uploaded files and folders details and press enter.

11 - Use any commands on another channel.

# Commands
`!uploadfile "full path of file"` Uploads a file to your discord server, if it's larger than 8 MB then it will be splitted by 8 MB and uploaded each parts to your discord server!

`!uploadfolder "full path of folder"` Uploads all files from a folder to your discord server!

`!downloadfile "full path of file uploaded from your discord server"` Downloads a file uploaded from your discord server to your computer!

`!downloadfolder "full path of folder uploaded from your discord server"` Downloads all files from a folder uploaded from your discord server to your computer!

`!storage` Prints then Sends to your discord server the details about capacity, used and free storage!

# Screenshot of Downloaded File Larger Than 8 MB uploaded from Discord by Unlimited Discord Storage

It does have same bytes from original file compared to Downloaded File Larger Than 8 MB uploaded from Discord.
![Screenshot of Downloaded File Larger Than 8 MB uploaded from Discord by Unlimited Discord Storage](https://cdn.discordapp.com/attachments/352944118864805889/779860363234770994/182.PNG)
