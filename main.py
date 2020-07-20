from moviepy.editor import *
from PIL import Image
import os, youtube_dl, eyed3, requests, shutil, json

os.system("cls")

def specialCh(string):
    string = string.replace("?","").replace(":","").replace("*","").replace('"', "'")
    return string
def removeTags(string):
    string = string.replace(" (Official Video)", "").replace(" (Lyrics)", "").replace(" [Official Video]", "").replace(" (Official Music Video)", "").replace(" (Official Video)", "").replace(" (Audio)", "")
    return string

def convert(src, path):
    videoclip = VideoFileClip(src)
    audioclip = videoclip.audio
    audioclip.write_audiofile(path)
    audioclip.close()
    videoclip.close()
    os.remove(src)

def resize(file, w, h):
    tl = w/2 - h/2
    br = h + tl
    img = Image.open(file)
    img = img.crop((tl, 0, br, h))
    img.save(file)

def meta(file, info, path, uploader):

    if " - " in info["title"]:
        ttl = specialCh(info["title"]).split(" - ")
        ttl.pop(0)
        print(ttl)
        title = removeTags(" - ".join(ttl))
    else:
        title = specialCh(removeTags(info["title"]))

    audiofile = eyed3.load(file)
    audiofile.tag.artist = uploader
    audiofile.tag.title = title
    audiofile.tag.album = title
    audiofile.tag.track_num = n + 1
    audiofile.tag.images.set(3, open(albumart,'rb').read(), 'image/jpeg')
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
    try:
        os.rename(file, path + specialCh(title + ".mp3"))
    except:
        os.remove(file)

url = input("Enter the url of a song. \n>")
try:
    with youtube_dl.YoutubeDL({}) as ydl:
        data = ydl.download([url])[1]
        #Right click on "download" and click "Go to Definition". On line 2029 after "return self._download_retcode" add ", res"
        #(Only works in Visual Studio)
except:
    if data == null:
        
    print("Make sure you have followed all the instructions correctly and that the URL is correct")
    exit()

try:
    tn = data["entries"][0]["thumbnails"][len(data["entries"][0]["thumbnails"])-1]["url"]
except:
    tn = data["thumbnails"][len(data["thumbnails"])-1]["url"]

albumart = tn.split("/")[-1].split("?")[0]

with open(albumart,'wb') as f:
    shutil.copyfileobj(requests.get(tn, stream = True).raw, f)

width, height = Image.open(albumart).size
resize(albumart, width, height)

if ".jpg" not in albumart:
    fformat = albumart.split(".")[1]
    im = Image.open(albumart).convert("RGB")
    albumart = albumart.split(".")[0] + ".jpg"
    im.save(albumart, "jpeg")
    os.remove(albumart.split(".")[0] + "." + fformat)

titles = []

try:
    for i in data["entries"]:
        titles.append(specialCh(i['title']) + "-" + i["id"] + ".mp4")
    os.mkdir(data["entries"][0]["playlist_title"])
except:
    titles.append(data["title"] + "-" + data["id"] + ".mp4")


for n, i in enumerate(titles):
    mp3 = i.replace("mp4", "mp3")
    try:
        convert(i, mp3)
    except:
        print("The file", i, "could not be found. Please copy the file name of the mp4 and enter it manually")
        failf = input("> ")
        if ".mp4" not in failf:
            failf += ".mp4"
        convert(failf, mp3)
    try:
        info_ = data["entries"][n]
        meta(mp3, info_, info_["playlist_title"] + "/", info_["playlist_uploader"])
    except:
        meta(mp3, data, "", data["uploader"])

os.remove(albumart)
os.system("cls")
print("Done.")