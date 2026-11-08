from imports import Lyric, SongLyric, Color

lyrics = [
    Lyric("L'ansia ti frega, ", 0.08, 0.4, False, Color.WHITE),
    Lyric("chi vuoi che creda", 0.08, 0.8, color=Color.WHITE),
    Lyric("Se anche tu non credi in te", 0.09, 1.8, color=Color.WHITE),
    Lyric("Però ricorda ", 0.08, 0.4, False, color=Color.WHITE),
    Lyric("che chi sopporta", 0.08, 0.8, color=Color.WHITE),
    Lyric("Tutto il sudore e lo stress", 0.08, 1.6, color=Color.WHITE),
    Lyric("Arriva al top", 0.06, 0.6, color=Color.CYAN),
    Lyric("Fra, fatica un tot", 0.08, 0.6, color=Color.CYAN),
    Lyric("Fino alla cima G.O.A.T", 0.06, 0.8, color=Color.CYAN),
    Lyric("Fra, don't give a fuck ", 0.06, 0.4, False, color=Color.CYAN),
    Lyric("degli altri", 0.06, 0.6, color=Color.CYAN),
    Lyric("Arriva al top", 0.06, 0.6, color=Color.CYAN),
]

canzone = SongLyric(lyrics)
canzone.play()