import pygame
import time
import keyboard

pygame.mixer.init()
playlist = ["Denis_Ten_-_She_wont_be_mine.mp3",
            "Lil_Nas_X_-_HOLIDAY.mp3",
            "Eminem_-_Houdini_.mp3"
]
ind = 0
def play_s():
    pygame.mixer.music.load(playlist[i])
    pygame.mixer.music.play()
    print(f"Playing: {playlist[ind]}")

def stop():
    pygame.mixer.music.stop()
    print("Music stopped")

def nexxt():
    global ind
    ind = (ind + 1) % len(playlist)
    play_s()

def prev():
    global ind
    ind  = (ind - 1 + len(playlist)) % len(playlist)
    play_s()

keyboard.add_hotkey("space", play_s)
keyboard.add_hotkey("s", stop)
keyboard.add_hotkey("n", nexxt)
keyboard.add_hotkey("p", prev)

while True:
    time.sleep(0.01)
