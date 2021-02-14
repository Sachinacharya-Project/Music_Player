import tkinter as tk
from tkinter import filedialog
from vlc import MediaPlayer
import os
import time

# CREATING FILEDIALOGUE
root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)
musicFile = str(filedialog.askopenfilename())

itter = ''
if __name__ == '__main__':
    while True:
        data = MediaPlayer(musicFile)
        while True:
            if itter == 'play':
                ask = 'play'
                itter = ''
            else:
                ask = input('user@root:~ ').lower()
            if ask == 'play':
                if str(data.get_state()).split('.')[1] == 'Ended':
                    musicFile = filedialog.askopenfilename()
                    itter = 'play'
                    data.stop()
                    break
                else:
                    data.play()
                    print('Playing Audio')
                    time.sleep(1)
            elif ask == 'pause':
                print('Pausing Audio')
                time.sleep(0.5)
                data.pause()
            elif ask == 'stop':
                print('Stopping Audio')
                time.sleep(0.5)
                data.stop()
            elif ask == 'quit' or ask == 'exit':
                print('Exiting Music Player')
                time.sleep(1)
                exit()
            elif ask == 'clear' or ask == 'cls':
                print('Clearing Screen')
                time.sleep(0.5)
                os.system('cls')
            elif ask == 'change':
                musicFile = filedialog.askopenfilename()
                itter = 'play'
                data.stop()
                break
            elif ask == 'mute':
                if data.audio_get_mute() == 0:
                    print('Muting Audio')
                    time.sleep(0.5)
                    data.audio_toggle_mute()
                else:
                    print('Already Muted\nCurrent Volume Level: {}'.format(data.audio_get_volume()))
            elif ask == 'unmute':
                if data.audio_get_mute() == 1:
                    print('Unmuting Audio')
                    time.sleep(0.5)
                    data.audio_toggle_mute()
                else:
                    print('Already Unmuted\nCurrent Volue Level: {}'.format(data.audio_get_volume()))
            elif ask == 'status':
                print('Status-------------------------------------')
                print('State: {}'.format(str(data.get_state()).split('.')[1]))
                if data.audio_get_mute() == 0:
                    print('Muted/Unmuted: Unmuted')
                else:
                    print('Muted/Unmuted: muted')
                print('Length(MS): {}'.format(data.get_length()))
                print('Current Length: {}'.format(data.get_time()))
                print('Volume Level: {}'.format(data.audio_get_volume()))
            elif ask == 'volume':
                print('Current Level: {}'.format(data.audio_get_volume()))
                level = int(input('New Level (0 - 100): '))
                data.audio_set_volume(level)
            elif ask == 'set time':
                tm = int(input('Enter Time (0 - {}): '.format(data.get_length())))
                data.pause()
                data.set_time(tm)
                data.play()
            elif ask == 'test':
                print(data.get_time())
                data.set_time(3400)
            else:
                print(data.is_playing())