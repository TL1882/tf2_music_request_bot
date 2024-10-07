# tf2_music_request_bot

## **(WINDOWS ONLY)**
scripts to play audio from youtube through vlc when someone sends a message starting with ;play in tf2 chat

# requires:
## python libraries:
  subprocess
  
  glob
  
  youtube_search
## applications:
  yt-dlp
  
  vlc

# downloading and running:
  download all 3 parts

  **edit paths in part2 and part3**

  **set vlc to only allow 1 instance at a time**

  make sure to set vlc to output to something like vb virtual cable or voicemod line in so you can hook it up to tf2
  
  run part1 and part2 in 2 separate cmd windows

# credits 'n' stuff
https://github.com/BreezyInterwebs/TF2-Console-Parser

# support
i'm gonna be honest i have no clue how this works so you're gonna have to figure it out yourself if you have unexpected problems

# known issues
if someone puts ;play outside of the start of their message it will cause the whole message including their name and ;play to be searched

if the youtube searcher chooses a live stream part2 will hang
