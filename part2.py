import subprocess
import glob
import os
from youtube_search import YoutubeSearch
from time import sleep

while True:

    os.chdir("script\\dir\\here")
    file = open("output.txt", "r")
    term = file.readline()
    file.close()
    with open('output.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('output.txt', 'w') as fout:
        fout.writelines(data[1:])
    
    url = ""
    
    results = YoutubeSearch(term, max_results=1).to_dict()
    for result in results:
        url = f"https://youtube.com{result['url_suffix']}"
        
        
    if url != "":
        os.chdir("download\\dir\\here")
        cmd = "yt-dlp\\dir\\here\\yt-dlp.exe -x --audio-format vorbis".split()
        subprocess.run(cmd + [str(url)], shell=False)
        os.chdir("script\\dir\\here")
        list_of_files = glob.glob('download\\*')
        latest_file = max(list_of_files, key=os.path.getctime)
#        f = open("latest.txt", "a")
#        print(latest_file), file=f)
#        f.close()
        cmd = "\"part3.bat\""
        subprocess.Popen(cmd + ", \"" + latest_file + "\"")
    sleep(1)