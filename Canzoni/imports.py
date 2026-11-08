from pathlib import Path
import sys

cartella_lyrics = Path(__file__).resolve().parent.parent
sys.path.append(str(cartella_lyrics))

from main import Lyric, SongLyric, Color