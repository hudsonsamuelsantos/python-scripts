from pygame import mixer

mixer.init()
mixer.music.load('music.mp3')

mixer.music.play()

x = input('Digite algo para parar a musica...')