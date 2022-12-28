import os
#get current working directory
cur_path = os.getcwd()
os.environ["PATH"] = "cur_path\\{}".format("geckodriver.exe")+ os.pathsep + os.environ["PATH"]