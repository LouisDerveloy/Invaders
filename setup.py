from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "main.py",icon = "icone.ico", base = "Win32GUI" )
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.
  
buildOptions = dict( 
        includes = ["threading","time","random","pygame"],
        include_files = ["icone.ico"]
)#"script/player.py", "icone.ico", "script/text.py", "script/image.py", "script/IA.py", "image/background.jpg", "image/battleship_IA.png.png", "image/battleship_player.png", "image/bouton_play.png", "image/game_over.png", "image/heart.png", "image/icone.png", "image/laser.png", "image/STAR_INVADER.png"
  
setup(
    name = "STAR_INVADER",
    version = "1.0",
    description = "Programme cré par un enfant de 12ans Discord: infinity-loulou#6437",
    author = "Infinity-loulou",
    options = dict(build_exe = buildOptions),
    executables = executables)