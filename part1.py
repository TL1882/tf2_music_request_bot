import os
import re
from time import sleep

# Given a TF2 console log, this will extract chat messages recorded.
def parse_console(filename):
    
    ##### Private helper function. #####
    def clean_list(string_list):
        sl_2 = [item.replace("*DEAD* ", "").replace('*DEAD*', "").replace("\n", "").replace("(TEAM)", "").replace("(PARTY)", "") for item in string_list]
        ping_reg = re.compile("^\s+\d{1,4} ms")
        error_reg = re.compile("^Error:")
        bind_reg = re.compile("^\"\w+\"")
        mdl_reg = re.compile("\.mdl : ")
        return [item for item in sl_2 if not (ping_reg.search(item) or error_reg.search(item) or bind_reg.search(item) or mdl_reg.search(item))]
    #####################################
    
    assert isinstance(filename, str)
    assert ('.txt' in filename or '.log' in filename)
    
    string_list = []
    regexp = re.compile('.+( : ).+')
    no_ff = re.compile('(freak_fortress_2)')
    f = open(filename, 'r', encoding="utf-8")
    while True:
        try:
            line = f.readline()
            if not line:
                break
            if (regexp.search(line) and not no_ff.search(line)) or (") Connected" in line):
                string_list.append(line)
        except:
            pass
    return clean_list(string_list)
    
# Function to restrict searches to a certain phrase.
def contains(text, all_chat):
    text = text.lower()
    text_reg = re.compile(rf" : .*{text}.*")
    chat_list = []
    for chat in all_chat:
        if text_reg.search(chat.lower()):
            chat_list.append(chat)
    return chat_list
    
#above code is from tf2 console log parser
#below code is regex stuff to get only the request (needs updating to prevent messages that have the command in the middle of the message messing things up)
while True:
    txt = str(contains(";play ", parse_console("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Team Fortress 2\\tf\\console.log")))
    txt = str(re.sub("', '", "']\n['", txt))
    f = open("log.txt", "a")
    print(txt, file=f)
    f.close()
    txt = str(re.sub("^\[", "", txt))
    txt = str(re.sub("\]\n", "\n", txt))
    txt = str(re.sub("\]$", "", txt))
    txt = str(re.sub("'(.*?) :  ;play ", "", txt))
    txt = str(re.sub("^$\n", "", txt))
    txt = str(re.sub("\n\[", "\n", txt))
    txt = str(re.sub("'\n", "\n", txt))
    if txt != "":
        f = open("output.txt", "a")
        print(re.sub("'$", "", txt), file=f)
        f.close()
        print(re.sub("'$", "", txt))
    open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Team Fortress 2\\tf\\console.log", "w").close()
    sleep(2)
