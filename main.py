from playsound import playsound
from pynput.mouse import Listener
sound = 'thud.mp3'
def on_click(a,b,c,pressed):
    if pressed:
        playsound(sound)
while True:
    try:        
        with Listener(on_click = on_click) as listener:
            listener.join()
    except:
        pass
