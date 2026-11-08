from imports import Lyric, SongLyric, Color

lyrics = [
    Lyric("Ricordo che ho pensato", 0.04, 0.04, color=Color.WHITE),
    Lyric("\"Finalmente riesco a sentirla\"", 0.06, 0.09, color=Color.WHITE),
    
    Lyric("Vali molto di più di quello che DO", 0.06, 0.4, color=Color.CYAN),
    Lyric("Suona ancora per me e da RE morirò", 0.06, 0.4, color=Color.CYAN),
    Lyric("MI FA tremare il pensiero che ti perderò", 0.06, 0.4, color=Color.CYAN),
    
    Lyric("(Sei la mia musica)", 0.1, 0.4, color=Color.MAGENTA),
    
    Lyric("SOLtanto tu riesci a darmi quello che non ho", 0.04, 0.6, color=Color.CYAN),
    Lyric("LA risposta a tutte le cose che non so", 0.06, 0.4, color=Color.CYAN),
    Lyric("SI infrangeranno 'ste promesse quando me ne andrò", 0.04, 0.6, color=Color.CYAN),
    
    Lyric("(Sei la mia musica)", 0.1, 0.4, color=Color.MAGENTA),
    Lyric("Sei molto più di quel che ho", 0.08, 0.4, color=Color.WHITE),
    Lyric("Suona per me, non me ne andrò", 0.08, 0.4, color=Color.WHITE),
    Lyric("Se fai silenzio, sparirò", 0.08, 0.4, color=Color.WHITE),
    Lyric("Sei la mia musica", 0.1, 0.4, color=Color.MAGENTA),
]

canzone = SongLyric(lyrics)
canzone.play()