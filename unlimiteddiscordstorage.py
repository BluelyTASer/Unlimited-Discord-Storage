from pathlib import Path
global reader
global count
global count1
global count2
global embeder
global timersr
global totalparts
global writersr
global oswalker
global namefile
global sizefile
global patherfile
global filecounter
global total_size
global readersize
global filerfound
global totalparts
global writerfiler
global pathercount
global pathercounter
global bannedchars
global currentlydirectory
global filetodownload
global downloadedpart
global currentertime
global movebackdir
global directorycounter
global directorywriter
global patherdir
global sizedir
global partcount
global directorytabler
global directoryname
global directoryfound
global currentdirsize
global directorynamersr
global downloadsnamersr
global count3
global currentfilesize
global aboveunder
global downloadedparter
global tablersizersr
global adddirectoriesr
global fileextensiontabler
global fileextender
global token
global channelnamersrr
token = input("Type Bot Token: ")
channelnamersrr = input("Type Channel Name For Viewing Uploaded Files And Folders Details: ")

class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))
import math
import discord
from discord import Embed
import os
from io import BytesIO
import nest_asyncio
from datetime import datetime
nest_asyncio.apply()

client = discord.Client()

@client.event
async def on_member_join(member):
    print("It looks like " + member + " just joined...")


@client.event
async def on_message(message):
  if message.guild is not None:
    if message.content.find("!uploadfile") == 0 and not message.author.bot:
      if os.path.exists(str(message.content[12:])): 
        if os.path.isfile(str(message.content[12:])):
          namefile = os.path.basename(str(message.content[12:]))
          sizefile = os.path.getsize(str(message.content[12:]))
          patherfile = os.path.abspath(str(message.content[12:]))
          embeder = Embed(title=namefile, description=patherfile, colour=0xFF0000, timestamp=datetime.utcnow())
          if sizefile > 8000000:
            fielder = [("Size in bytes", sizefile, True),
                       ("Last Access:", datetime.fromtimestamp(os.path.getatime(str(message.content[12:]))).strftime("%A, %B %d, %Y %H:%M:%S.%f"), True),
                       ("Last Modification:", datetime.fromtimestamp(os.path.getmtime(str(message.content[12:]))).strftime("%A, %B %d, %Y %H:%M:%S.%f"), True),
                       ("Last Creation:", datetime.fromtimestamp(os.path.getctime(str(message.content[12:]))).strftime("%A, %B %d, %Y %H:%M:%S.%f"), False),
                       ("Parts:", str(math.ceil(sizefile / 8000000)), False)]
          else:
            fielder = [("Size in bytes", sizefile, True),
                       ("Last Access:", datetime.fromtimestamp(os.path.getatime(str(message.content[12:]))).strftime("%A, %B %d, %Y %H:%M:%S.%f"), True),
                       ("Last Modification:", datetime.fromtimestamp(os.path.getmtime(str(message.content[12:]))).strftime("%A, %B %d, %Y %H:%M:%S.%f"), True),
                       ("Last Creation:", datetime.fromtimestamp(os.path.getctime(str(message.content[12:]))).strftime("%A, %B %d, %Y %H:%M:%S.%f"), False)]
          for namer, resulter, linersr in fielder:
            embeder.add_field(name=namer, value=resulter, inline=linersr)
          if sizefile > 8000000:
            print("Uploading file...")
            embeder.set_footer(text="File Above Than 8 MB")
            totalparts = math.ceil(sizefile / 8000000)
            for channel in message.guild.channels:
              if str(channel) == str(channelnamersrr):
                await channel.send(embed=embeder)
            await message.channel.send("File Starting of " + patherfile + " Parts: " + str(totalparts))
            filer = open(str(message.content[12:]), "rb")
            count = 1
            count1 = 0
            while True:
              timersr = datetime.now()
              reader = filer.read(8000000)
              if not reader:
                break
              await message.channel.send("File Above Than 8 MB - Part " + str(count) + ": " + patherfile, file=discord.File(BytesIO(reader), filename=namefile + "." + str(count)))
              count += 1
              count1 += len(reader)
              if math.floor((count1 / sizefile) * 100) < 100:
                print(str(math.floor((count1 / sizefile) * 100)) + "% Uploaded  Time Estimated: " + str((datetime.now() - timersr) * ((sizefile - count1) / 8000000)))
              else:
                print("100% Uploaded")
            await message.channel.send("File Ending of " + patherfile + " Parts: " + str(totalparts))  
          else:
            print("Uploading file...")
            embeder.set_footer(text="File Under Than 8 MB")
            for channel in message.guild.channels:
              if str(channel) == str(channelnamersrr):
                await channel.send(embed=embeder)
            await message.channel.send("File Under Than 8 MB: " + patherfile, file=discord.File(str(message.content[12:]), filename=namefile))
            print("100% Uploaded")
        else:
          await message.channel.send(str(message.content[12:]) + " Isn't File. To Upload A Folder use !uploadfolder")
      else:
        await message.channel.send(str(message.content[12:]) + " Doesn't Exist.")
    elif message.content.find("!uploadfolder") == 0 and not message.author.bot:
      if os.path.exists(str(message.content[14:])):
        if os.path.isdir(str(message.content[14:])):
          fileextensiontabler = []
          filecounter = 0
          writersr = ""
          oswalker = os.walk(str(os.path.abspath(message.content[14:])))
          writersr += (str(os.path.abspath(str(message.content[14:]))))
          for path in DisplayablePath.make_tree(Path(str(message.content[14:]))):
            writersr += ("\n" + str(path.displayable()))
          total_size = 0
          for dirrrr, dirsrr, filesrr in oswalker:
            for f in filesrr:
              ersr = os.path.join(dirrrr, f)
              total_size += os.path.getsize(ersr)
              if "." in str(f) and (not str(f)[0] == "."):  
                if not str(str(f)[int(int(str(f).rfind(".")) + 1):]) in fileextensiontabler:
                  fileextensiontabler.append(str(str(f)[int(int(str(f).rfind(".")) + 1):]))
              elif str(f)[0] == ".":
                if str(f).rfind(".") > 0:
                  if not str(f).rfind(".") == int(len(str(f)) - 1):
                    if not str(str(f)[int(int(str(f).rfind(".")) + 1):]) in fileextensiontabler:
                      fileextensiontabler.append(str(str(f)[int(int(str(f).rfind(".")) + 1):]))
                  else:
                    if not "unknown" in fileextensiontabler:
                      fileextensiontabler.append("unknown")
                else:
                  if not "hidden" in fileextensiontabler:
                    fileextensiontabler.append("hidden")
              else:
                if not "unknown" in fileextensiontabler:
                  fileextensiontabler.append("unknown")
          fileextender = ""
          if len(fileextensiontabler) > 0:
            for extender in fileextensiontabler:
              fileextender += extender + " "
          fileextensiontabler = ""
          writersr += (str("\nTotal Size in bytes: " + str(total_size)))
          writersr += ("\nLast Access of main folder: " + str(datetime.fromtimestamp(os.path.getatime(str(os.path.abspath(message.content[14:])))).strftime("%A, %B %d, %Y %H:%M:%S.%f")))
          writersr += ("\nLast Modification of main folder: " + str(datetime.fromtimestamp(os.path.getmtime(str(os.path.abspath(message.content[14:])))).strftime("%A, %B %d, %Y %H:%M:%S.%f")))
          writersr += ("\nLast Creation of main folder: " + str(datetime.fromtimestamp(os.path.getctime(str(os.path.abspath(message.content[14:])))).strftime("%A, %B %d, %Y %H:%M:%S.%f")))
          writersr += ("\n-----------------------------------------------------------------------------")
          oswalker = os.walk(str(os.path.abspath(message.content[14:])))
          for root, dirs, files in oswalker:
            for x in files:
              namefile = os.path.basename(os.path.join(root, x))
              sizefile = os.path.getsize(os.path.join(root, x))
              patherfile = os.path.abspath(os.path.join(root, x))
              if sizefile < 8000000:  
                writersr += (str("\nName of file: " + namefile + "\nSize in bytes: " + str(sizefile) + "\nLast Access: " + str(datetime.fromtimestamp(os.path.getatime(os.path.join(root, x))).strftime("%A, %B %d, %Y %H:%M:%S.%f")) + "\nLast Modification: " + str(datetime.fromtimestamp(os.path.getmtime(os.path.join(root, x))).strftime("%A, %B %d, %Y %H:%M:%S.%f")) + "\nLast Creation: " + str(datetime.fromtimestamp(os.path.getctime(os.path.join(root, x))).strftime("%A, %B %d, %Y %H:%M:%S.%f")) + "\n-----------------------------------------------------------------------------"))
              else:
                writersr += (str("\nName of file: " + namefile + "\nSize in bytes: " + str(sizefile) + "\nLast Access: " + str(datetime.fromtimestamp(os.path.getatime(os.path.join(root, x))).strftime("%A, %B %d, %Y %H:%M:%S.%f")) + "\nLast Modification: " + str(datetime.fromtimestamp(os.path.getmtime(os.path.join(root, x))).strftime("%A, %B %d, %Y %H:%M:%S.%f")) + "\nLast Creation: " + str(datetime.fromtimestamp(os.path.getctime(os.path.join(root, x))).strftime("%A, %B %d, %Y %H:%M:%S.%f")) + "\nParts: " + str(math.ceil(sizefile / 8000000)) + "\n-----------------------------------------------------------------------------"))
              filecounter += 1
          oswalker = os.walk(str(os.path.abspath(message.content[14:])))
          directorywriter = ""
          directorycounter = 0
          for cat, tas, pen in oswalker:
            for x in tas:
              sizedir = 0
              for dirrrrr, dirsrrr, filesrrr in os.walk(os.path.join(cat, x)):
                for f in filesrrr:
                  ersr = os.path.join(dirrrrr, f)
                  sizedir += os.path.getsize(ersr)
              patherdir = os.path.abspath(os.path.join(cat, x))
              directorywriter += (str("\nPath of the folder: " + patherdir + "\nSize in bytes: " + str(sizedir) + "\nLast Access: " + str(datetime.fromtimestamp(os.path.getatime(os.path.join(cat, x))).strftime("%A, %B %d, %Y %H:%M:%S.%f")) + "\nLast Modification: " + str(datetime.fromtimestamp(os.path.getmtime(os.path.join(cat, x))).strftime("%A, %B %d, %Y %H:%M:%S.%f")) + "\nLast Creation: " + str(datetime.fromtimestamp(os.path.getctime(os.path.join(cat, x))).strftime("%A, %B %d, %Y %H:%M:%S.%f")) + "\n-----------------------------------------------------------------------------"))
              filecounter += 1
          for channel in message.guild.channels:
            if str(channel) == str(channelnamersrr):
              writersr = BytesIO(str(writersr).encode())
              if len(str(fileextender)) > 0:
                await channel.send(str(os.path.abspath(str(message.content[14:])) + str("  Total Size in bytes: " + str(total_size)) + " All File Extensions: " + fileextender), file=discord.File(writersr, filename="All Files of a directory.txt"))
              else:
                await channel.send(str(os.path.abspath(str(message.content[14:])) + str("  Total Size in bytes: " + str(total_size)) + " No File Extensions "), file=discord.File(writersr, filename="All Files of a directory.txt"))
              directorywriter = BytesIO(str(directorywriter).encode())
              await channel.send(file=discord.File(directorywriter, filename="All Folders of a directory.txt"))
          fileextender = ""
          writersr = ""
          directorywriter = ""
          count1 = 0
          count2 = 0
          print("Uploading Folder...")
          oswalker = os.walk(str(os.path.abspath(message.content[14:])))
          await message.channel.send("Folder Starting of " + str(os.path.abspath(str(message.content[14:]))))
          for rooter, dirsr, fileser in oswalker:
            for x in fileser:
              namefile = os.path.basename(str(os.path.join(rooter, x)))
              sizefile = os.path.getsize(str(os.path.join(rooter, x)))
              patherfile = os.path.abspath(str(os.path.join(rooter, x)))
              if namefile[0] == "." or namefile[0] == "_":
                if "\\" in str(patherfile):
                  patherfile = patherfile.replace(namefile, str("\\" + namefile))
                elif "/" in str(patherfile):
                  patherfile = patherfile.replace(namefile, str("/" + namefile))
              if sizefile > 8000000:
                totalparts = math.ceil(sizefile / 8000000)
                await message.channel.send("File Starting of " + patherfile + " Parts: " + str(totalparts))
                filer = open(patherfile, "rb")
                count = 0
                count1 = 0
                while True:
                  timersr = datetime.now()
                  count += 1
                  reader = filer.read(8000000)
                  if not reader:
                    break
                  await message.channel.send("File Above Than 8 MB - Part " + str(count) + ": " + patherfile, file=discord.File(BytesIO(reader), filename=namefile + "." + str(count)))
                  readersize = len(reader)
                  count1 += readersize
                  count2 += readersize
                  if count2 < total_size:
                    print(str(namefile) + " " + str(math.floor((count1 / sizefile) * 100)) + "% File Uploaded " + str(math.floor((count2 / total_size) * 100)) + "% Uploaded  Time Estimated: " + str((datetime.now() - timersr) * ((total_size - count2) / 8000)))
                  else:
                    print(str(namefile) + " " + str(math.floor((count1 / sizefile) * 100)) + "% File Uploaded " + str(math.floor((count2 / total_size) * 100)) + "% Uploaded")  
                await message.channel.send("File Ending of " + patherfile + " Parts: " + str(totalparts))
              else:
                timersr = datetime.now()
                await message.channel.send("File Under Than 8 MB: " + patherfile, file=discord.File(os.path.abspath(str(os.path.join(rooter, x))), filename=namefile))
                count1 += sizefile
                count2 += sizefile
                if count2 < total_size:
                  print(str(namefile) + " 100% File Uploaded " + str(math.ceil((count2 / total_size) * 100)) + "% Uploaded  Time Estimated: " + str((datetime.now() - timersr) * ((total_size - count2) / 8000)))
                else:
                  print(str(namefile) + " 100% File Uploaded " + str(math.floor((count2 / total_size) * 100)) + "% Uploaded")  
          await message.channel.send("Folder Ending of " + str(os.path.abspath(str(message.content[14:]))))      
        else:
          await message.channel.send(str(message.content[14:]) + " Isn't Folder. To Upload A File use !uploadfile")
      else:
        await message.channel.send(str(message.content[14:]) + " Doesn't Exist.")
    elif message.content.find("!downloadfile") == 0 and not message.author.bot:
      filerfound = "Pathersr"
      bannedchars = '*?:"<>|'
      print("Finding File...")
      async for messagersr in message.channel.history(oldest_first=True, limit=1999999999):
        if "File Starting of" in str(messagersr.content) and str(message.content)[14:] in str(messagersr.content) and messagersr.author.bot and filerfound == "Pathersr":
          print("File Found! Downloading it...")
          pathercount = 0
          while not str(messagersr.content)[pathercount - 17:pathercount] == "File Starting of ":
            pathercount += 1
          pathercounter = pathercount
          while not str(messagersr.content)[pathercounter:pathercounter + 8] == " Parts: ":
            pathercounter += 1
          filerfound = str(str(messagersr.content)[pathercount:pathercounter])
          for car in bannedchars:
            filerfound = filerfound.replace(car, "")
          filerfound = filerfound.replace("\\", "!").replace("/", "!")
          while not str(messagersr.content)[pathercounter - 8:pathercounter] == " Parts: ":
            pathercounter += 1
          if (pathercounter + 1) == len(str(messagersr.content)):
            totalparts = int(str(messagersr.content)[pathercounter])
          else:
            totalparts = int(str(messagersr.content)[pathercounter:])
          partcounter = 0
        if "File Above Than 8 MB" in str(messagersr.content) and str(message.content)[14:] in str(messagersr.content) and filerfound != "Pathersr" and messagersr.author.bot:
          if not "writerfiler" in locals():
            currentlydirectory = str(os.getcwd())
            if not os.path.exists(os.path.join(os.getcwd(), "downloads")):
              os.mkdir(os.path.join(os.getcwd(), "downloads"))
            os.chdir(os.path.join(os.getcwd(), "downloads"))
            datenower = str(datetime.now()).replace("-", "").replace(" ", "").replace(":", "").replace(".", "")
            if not os.path.exists(os.path.join(os.getcwd(), datenower)):
              os.mkdir(os.path.join(os.getcwd(), datenower))
            os.chdir(os.path.join(os.getcwd(), datenower))
            if not os.path.exists(os.path.join(os.getcwd(), filerfound)):
              os.mkdir(os.path.join(os.getcwd(), filerfound))
            filetodownload = str(os.path.join(os.getcwd(), filerfound))
            os.chdir(currentlydirectory)
            writerfiler = open(str(os.path.join(str(filetodownload), str(str(messagersr.attachments[0].filename)[:int(str(messagersr.attachments[0].filename).rfind("."))]))), "wb")
            downloadedparter = 0
          currentertime = datetime.now()
          writerfiler.write(await messagersr.attachments[0].read())
          writerfiler.flush()
          downloadedparter += 1
          if downloadedparter < totalparts:
            print(str(math.ceil((downloadedparter / totalparts) * 100)) + "% File Downloaded  Time Estimate: " + str((datetime.now() - currentertime) * (totalparts - downloadedparter)))
          else:
            print("100% File Downloaded  They're Located at: " + str(filetodownload))
        if "File Under Than 8 MB" in str(messagersr.content) and str(message.content)[14:] in str(messagersr.content) and messagersr.author.bot:
          currentlydirectory = str(os.getcwd())
          pathercount = 0
          while not str(messagersr.content)[pathercount - 22:pathercount] == "File Under Than 8 MB: ":
            pathercount += 1
          filerfound = str(str(messagersr.content)[pathercount:])
          for car in bannedchars:
            filerfound = filerfound.replace(car, "")
          filerfound = filerfound.replace("\\", "!").replace("/", "!")
          if not os.path.exists(os.path.join(os.getcwd(), "downloads")):
            os.mkdir(os.path.join(os.getcwd(), "downloads"))
          os.chdir(os.path.join(os.getcwd(), "downloads"))
          datenower = str(datetime.now()).replace("-", "").replace(" ", "").replace(":", "").replace(".", "")
          if not os.path.exists(os.path.join(os.getcwd(), datenower)):
            os.mkdir(os.path.join(os.getcwd(), datenower))
          os.chdir(os.path.join(os.getcwd(), datenower))
          if not os.path.exists(os.path.join(os.getcwd(), filerfound)):
            os.mkdir(os.path.join(os.getcwd(), filerfound))
          filetodownload = str(os.path.join(os.getcwd(), filerfound))
          os.chdir(currentlydirectory)
          writerfiler = open(str(os.path.join(str(filetodownload), str(str(messagersr.attachments[0].filename)))), "wb")
          downloadedparter = 0
          writerfiler.write(await messagersr.attachments[0].read())
          print("100% File Downloaded  They're Located at: " + filetodownload)
          writerfiler.close()
          break
        if "File Ending of" in str(messagersr.content) and str(message.content)[14:] in str(messagersr.content) and messagersr.author.bot and filerfound != "Pathersr":
          writerfiler.close()
          break
      if filerfound == "Pathersr":
        print("File Not Found")
    elif message.content.find("!downloadfolder") == 0 and not message.author.bot:
      filerfound = "Pathersr"
      bannedchars = '*?:"<>|'
      directorytabler = []
      directoryfound = 0
      sizedir = 0
      print("Finding Folder...")
      async for messagersr in message.channel.history(oldest_first=True, limit=1999999999):
        if "Folder Starting of" in str(messagersr.content) and str(message.content)[16:] in str(messagersr.content) and messagersr.author.bot and filerfound == "Pathersr":
          print("Folder Found!")
          filerfound = 1
          directoryfound = 1
        if filerfound == 1:
          if (not "Folder Ending of" in str(messagersr.content)) and (str(message.content)[16:] in str(messagersr.content)):
            if messagersr.author.bot and ("File Under Than 8 MB" in str(messagersr.content) or "File Above Than 8 MB" in str(messagersr.content)):
              sizedir += int(messagersr.attachments[0].size)
              count = 0
              count1 = 0
              if "File Under Than 8 MB: " in str(messagersr.content):
                while not str(messagersr.content)[count - 22:count] == "File Under Than 8 MB: ":
                  count += 1
                aboveunder = 0
              elif "File Above Than 8 MB" in str(messagersr.content):
                count = int(str(messagersr.content).find(":"))
                count += 2
                aboveunder = 1
              directoryname = ""
              if aboveunder == 0:  
                directoryname = str(str(messagersr.content)[count:]).replace(str(messagersr.attachments[0].filename), "")
              else:
                directoryname = str(str(messagersr.content)[count:]).replace(str(messagersr.attachments[0].filename)[:int(str(messagersr.attachments[0].filename).rfind("."))], "")
              directoryname = str(directoryname).replace(str(message.content)[16:], "")
              for x in bannedchars:
                directoryname = str(directoryname).replace(x, "")
              if directoryname[0] == "/" or directoryname[0] == "\\":
                directoryname = str(directoryname)[1:]
              if "\\" in directoryname:
                if "." in directoryname[int(str(directoryname).rfind("\\")):]:
                  directoryname = str(directoryname)[:int(str(directoryname).rfind("\\"))]
              if "/" in directoryname:
                if "." in directoryname[int(str(directoryname).rfind("/")):]:
                  directoryname = str(directoryname)[:int(str(directoryname).rfind("/"))]
              if (not str(directoryname) in directorytabler) and len(str(directoryname)) > 0:
                directorytabler.append(str(directoryname))
          if "Folder Ending of" in str(messagersr.content) and str(message.content)[16:] in str(messagersr.content):
            break
      if directoryfound > 0:  
        directorytabler.sort(key=len)
        currentlydirectory = str(os.getcwd())
        filerfound = str(message.content)[16:]
        for fly in bannedchars:
          filerfound = str(filerfound).replace(fly, "")
        filerfound = filerfound.replace("\\", "!").replace("/", "!")
        if not os.path.exists(os.path.join(os.getcwd(), "downloads")):
          os.mkdir(os.path.join(os.getcwd(), "downloads"))
        os.chdir(os.path.join(os.getcwd(), "downloads"))
        datenower = str(datetime.now()).replace("-", "").replace(" ", "").replace(":", "").replace(".", "")
        if not os.path.exists(os.path.join(os.getcwd(), datenower)):
          os.mkdir(os.path.join(os.getcwd(), datenower))
        os.chdir(os.path.join(os.getcwd(), datenower))
        if not os.path.exists(os.path.join(os.getcwd(), filerfound)):
          os.mkdir(os.path.join(os.getcwd(), filerfound))
        os.chdir(os.path.join(os.getcwd(), filerfound))
        downloadsnamersr = str(os.getcwd())
        filetodownload = downloadsnamersr
        for x in directorytabler:
          adddirectoriesr = os.path.join(os.getcwd(), x)
          if "." in str(adddirectoriesr):
            if "\\" in str(adddirectoriesr):
              adddirectoriesr = str(adddirectoriesr)[:int(str(adddirectoriesr).rfind("\\"))]
              if adddirectoriesr[-1] == "\\":
                adddirectoriesr = str(adddirectoriesr)[:-1]
            if "/" in str(adddirectoriesr):
              adddirectoriesr = str(adddirectoriesr)[:int(str(adddirectoriesr).rfind("/"))]
          if not os.path.exists(adddirectoriesr):
            os.mkdir(adddirectoriesr)
        os.chdir(currentlydirectory)
        filerfound = "Pathersr"
        async for messagersr in message.channel.history(oldest_first=True, limit=1999999999):
          if "Folder Starting of" in str(messagersr.content) and str(message.content)[16:] in str(messagersr.content) and messagersr.author.bot and directoryfound < 2:
            print("Downloading These...  Folder's Total Size in bytes: " + str(sizedir))
            directoryfound = 2
            currentdirsize = 0
            writerfiler = 0
          if directoryfound == 2:
            if "File Starting of" in str(messagersr.content) and str(message.content)[16:] in str(messagersr.content) and messagersr.author.bot and filerfound == "Pathersr":
              pathercount = 0
              pathercounter = pathercount
              while not str(messagersr.content)[pathercounter - 8:pathercounter] == " Parts: ":
                pathercounter += 1
              if (pathercounter + 1) == len(str(messagersr.content)):
                totalparts = int(str(messagersr.content)[pathercounter])
              else:
                totalparts = int(str(messagersr.content)[pathercounter:])
              partcounter = 0
              filerfound = 0
            if "File Above Than 8 MB" in str(messagersr.content) and str(message.content)[16:] in str(messagersr.content) and filerfound == 0 and messagersr.author.bot:
              if writerfiler == 0:
                count3 = 0
                count3 = int(str(messagersr.content).find(":"))
                count3 += 2
                directorynamersr = str(str(messagersr.content)[count3:]).replace(str(message.content)[16:], "")
                for x in bannedchars:
                  directorynamersr = str(directorynamersr).replace(x, "")
                if directorynamersr[0] == "/" or directorynamersr[0] == "\\":
                  directorynamersr = str(directorynamersr)[1:]
                if not os.path.exists(directorynamersr):
                  directorynamersr = os.path.dirname(directorynamersr)
                directorynamersr = os.path.join(downloadsnamersr, directorynamersr)
                if (not "." in str(directorynamersr)) or (not str(messagersr.attachments[0].filename) in str(directorynamersr)):
                  directorynamersr = os.path.join(directorynamersr, str(str(messagersr.attachments[0].filename)[:int(str(messagersr.attachments[0].filename).rfind("."))]))
                writerfiler = open(str(directorynamersr), "wb")
                downloadedparter = 0
              currentertime = datetime.now()
              writerfiler.write(await messagersr.attachments[0].read())
              writerfiler.flush()
              currentdirsize += int(messagersr.attachments[0].size)
              downloadedparter += 1
              if currentdirsize < sizedir:
                print(str(messagersr.attachments[0].filename) + " " + str(math.ceil((downloadedparter / totalparts) * 100)) + "% File Downloaded  " + str(math.ceil((currentdirsize / sizedir) * 100)) + "% Downloaded  Time Estimate: " + str((datetime.now() - currentertime) * (sizedir / currentdirsize)))
              else:
                print(str(messagersr.attachments[0].filename) + " 100% File Downloaded  100% Downloaded  They're Located at: " + str(filetodownload))
            if "File Under Than 8 MB" in str(messagersr.content) and str(message.content)[16:] in str(messagersr.content) and messagersr.author.bot:
              count3 = 0
              count3 = int(str(messagersr.content).find(":"))
              count3 += 2
              directorynamersr = str(str(messagersr.content)[count3:]).replace(str(message.content)[16:], "")
              for x in bannedchars:
                directorynamersr = str(directorynamersr).replace(x, "")
              if directorynamersr[0] == "/" or directorynamersr[0] == "\\":
                directorynamersr = str(directorynamersr)[1:]  
              if not os.path.exists(directorynamersr):
                directorynamersr = os.path.dirname(directorynamersr)
              directorynamersr = os.path.join(downloadsnamersr, directorynamersr)
              if (not "." in str(directorynamersr)) or (not str(messagersr.attachments[0].filename) in str(directorynamersr)):
                directorynamersr = os.path.join(directorynamersr, str(messagersr.attachments[0].filename))
              writerfiler = open(str(directorynamersr), "wb")
              downloadedparter = 0
              currentertime = datetime.now()
              writerfiler.write(await messagersr.attachments[0].read())
              currentdirsize += int(messagersr.attachments[0].size)
              if currentdirsize < sizedir:
                print(str(messagersr.attachments[0].filename) + " 100% File Downloaded  " + str(math.ceil((currentdirsize / sizedir) * 100)) + "% Downloaded  Time Estimate: " + str((datetime.now() - currentertime) * (sizedir / currentdirsize)))
              else:
                print(str(messagersr.attachments[0].filename) + " " + "100% File Downloaded  100% Downloaded  They're Located at: " + str(filetodownload))
              writerfiler.close()
              writerfiler = 0
              filerfound = "Pathersr"
            if "File Ending of" in str(messagersr.content) and str(message.content)[16:] in str(messagersr.content) and messagersr.author.bot and filerfound != "Pathersr":
              writerfiler.close()
              writerfiler = 0
              filerfound = "Pathersr"
            if "Folder Ending of" in str(messagersr.content) and str(message.content)[16:] in str(messagersr.content) and messagersr.author.bot:
              directoryfound = 3
              break
      else:
        print("Folder Not Found")
    elif message.content.find("!storage") == 0 and not message.author.bot:
      total_size = 0
      async for messagersr in message.channel.history(oldest_first=True, limit=1999999999):
        if ("File Above Than 8 MB" in str(messagersr.content) or "File Under Than 8 MB" in str(messagersr.content)) and (len(messagersr.attachments) > 0 and messagersr.author.bot):
          total_size += int(messagersr.attachments[0].size)
      embeder = Embed(title="Storage", description="", colour=0xFF0000, timestamp=datetime.utcnow())
      fielder = [("Capacity:", "∞", True),
                 ("Used:", str(total_size), True),
                 ("Free:", "∞", True)]
      for namer, resulter, linersr in fielder:
        embeder.add_field(name=namer, value=resulter, inline=linersr)
      fielder = [("Capacity:", "Used:", "Free:"),
                 ("∞", str(total_size), "∞")]
      tablersizersr = max(len(x) for l in fielder for x in l)
      for row in fielder:
        print(''.join(x.ljust(tablersizersr + 2) for x in row))
      await message.channel.send(embed=embeder)
client.run(token)