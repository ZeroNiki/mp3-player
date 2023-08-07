from pydub import AudioSegment
from pydub.playback import play

from pyfzf.pyfzf import FzfPrompt

import os

fzf = FzfPrompt()

def mp_player(music):
    try:
        output = fzf.prompt(music)

        output_str = ' '.join(output)

        song = AudioSegment.from_mp3(f"{path}{output_str}")
        print(f"Song: {output_str}")

        song = song - 28 # Регулировка звука | Sound adjustment

        play(song)

    except KeyboardInterrupt:
        print("\nВы вышли из программы || You have exited the program")

     
def music():
    global path
    path = 'full/path/to/playlist' #Путь к плейлисту | Path to playlist 

    files = os.listdir(path)
    
    mp_player(files)


def main():
    music()

if __name__ == '__main__':
    main()

