import os
import shutil

os.system("git clone https://github.com/bricktrooper/Logs repo")
os.system("pip install repo/python/")
shutil.rmtree("repo/", ignore_errors = True)
shutil.rmtree("build", ignore_errors = True)
shutil.rmtree("dist/", ignore_errors = True)
shutil.rmtree("log.egg-info", ignore_errors = True)
