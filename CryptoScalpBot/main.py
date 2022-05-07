import subprocess

files = ["Coin1SHORT.py", "Coin1LONG.py", "Coin2SHORT.py", "Coin2LONG.py", "Coin3SHORT.py", "Coin3LONG.py", "Coin4SHORT.py", "Coin4LONG.py", "Coin5SHORT.py", "Coin5LONG.py"]  # файлы, которые нужно запустить
for file in files:
    subprocess.Popen(args=["start", "python", file], shell=True, stdout=subprocess.PIPE)
