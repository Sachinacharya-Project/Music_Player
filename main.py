import tkinter as tk
from tkinter import filedialog
from vlc import MediaPlayer
import os
import time

# CREATING FILEDIALOGUE
root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)
musicFile = list(filedialog.askopenfilenames())

itter = ''
options = [
    ('Play', 'Play Music/Unpause Music'),
    ('Pause', 'Pause Music'),
    ('Stop', 'Stop Music'),
    ('Quit / exit', 'Close Player'),
    ('Status', 'Show Current Status of Music'),
    ('Volume', 'Set Volume Level'),
    ('mute/unmute', 'Mute/Unmute Audio'),
    ('Change', 'Change Current music'),
    ('set time', 'Set Current Time'),
    ('Clear', 'Clear Screen'),
    ('Next', 'Change to Next Song'),
    ('prev', 'Change to Previous Song'),
    ('ls', 'View List of Song'),
    ('update repo', 'Update to GitHub'),
    ('add', 'Add More Files')
]
constant = 0
if __name__ == '__main__':
    while True:
        data = MediaPlayer(str(musicFile[constant]))
        while True:
            if itter == 'play':
                ask = 'play'
                itter = ''
            else:
                ask = input('user@root:~ ').lower()
            if ask == 'play':
                if str(data.get_state()).split('.')[1] == 'Ended':
                    musicFile = list(filedialog.askopenfilenames())
                    itter = 'play'
                    data.stop()
                    break
                else:
                    print('Playing Audio')
                    data.play()
                    time.sleep(1)
            elif ask == 'pause':
                print('Pausing Audio')
                time.sleep(0.5)
                data.pause()
            elif ask == 'next':
                constant = len(musicFile)-1 if (constant+1) >= len(musicFile) else constant+1
                print('No More Files are there!Play Last File' if (constant+1) >= len(musicFile) else constant+1)
                itter = 'play'
                data.stop()
                break
            elif ask == 'prev':
                constant = constant - 1
                itter = 'play'
                data.stop()
                break
            elif ask == 'choose':
                innerAsk = input('Enter Number (ls for list): ').lower()
                if innerAsk == 'ls':
                    cnt = 0
                    for item in musicFile:
                        print('0'+str(cnt) if cnt < 10 else cnt, ') ', str(item).split('/')[-1])
                        cnt += 1
                    innerAsk = input('Enter Number: ')
                else:
                    innerAsk = int(innerAsk)
                if innerAsk == 'exit':
                    print('Exiting Music Player')
                    time.sleep(1)
                    exit()
                else:
                    try:
                        constant = int(innerAsk)
                    except Exception:
                        pass
                itter = 'play'
                data.stop()
                break
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
                musicFile = filedialog.askopenfilenames()
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
                level = input('New Level (0 - 100): ')
                if level == '':
                    pass
                else:
                    data.audio_set_volume(int(level))
            elif ask == 'set time':
                tm = int(input('Enter Time (0 - {}): '.format(data.get_length())))
                data.pause()
                data.set_time(tm)
                data.play()
            elif ask == 'options' or ask == 'opt':
                print('Options',' '*(15-len('Options')), ':','Functions')
                print('\n')
                for item in options:
                    print(item[0],' '*(15-len(item[0])),':',item[1])
            elif ask == 'test':
                print(data.get_time())
                data.set_time(3400)
            elif ask == 'update repo':
                os.system('git pull&&git push')
            elif ask == 'add':
                getItem = list(filedialog.askopenfilenames())
                musicFile.append(getItem)
                time.sleep(0.2)
                print('{} Files added to Current List'.format(len(getItem)))
            elif ask == 'ls':
                cnt = 0
                for item in musicFile:
                    print('0'+str(cnt) if cnt < 10 else cnt, ') ', str(item).split('/')[-1])
                    cnt += 1
            else:
                print(data.is_playing())