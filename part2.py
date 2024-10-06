import subprocess
import glob
import os
from youtube_search import YoutubeSearch
from time import sleep

while True:

    os.chdir("script\\dir\\here")
    #read first line of output.txt and store it in term variable
    file = open("output.txt", "r")
    term = file.readline()
    file.close()
    
    #delete first line of output.txt
    with open('output.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('output.txt', 'w') as fout:
        fout.writelines(data[1:])
    
    url = ""

    #youtube search shenanigans 
    results = YoutubeSearch(term, max_results=1).to_dict()
    for result in results:
        url = f"https://youtube.com{result['url_suffix']}"
        
        
    if url != "":
        
        os.chdir("download\\dir\\here")
        
        cmd = "yt-dlp\\dir\\here\\yt-dlp.exe -x --audio-format vorbis".split() #change format and quality settings however you like 
        subprocess.run(cmd + [str(url)], shell=False)
        
        os.chdir("script\\dir\\here")

        #get latest file to send to vlc (i think this is gonna break)
        list_of_files = glob.glob('download\\*')
        latest_file = max(list_of_files, key=os.path.getctime)

        #i couldn't get this to work in python so i put it in a batch file :  )
        cmd = "\"part3.bat\""
        subprocess.Popen(cmd + ", \"" + latest_file + "\"")
        
    sleep(1)
