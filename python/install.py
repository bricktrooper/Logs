import os
import shutil

os.system("git clone https://github.com/bricktrooper/Logs")
os.system("pip install Logs/python/")
shutil.rmtree("Logs/", ignore_errors = True)
shutil.rmtree("build", ignore_errors = True)
shutil.rmtree("dist/", ignore_errors = True)
shutil.rmtree("log.egg-info", ignore_errors = True)
