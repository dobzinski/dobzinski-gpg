from main import *

def crypto(path):
  directory = os.fsencode(path)
  for file in os.listdir(directory):
    d = os.fsdecode(directory)
    filename = os.fsdecode(file)
    dirFile = str(d) + str(filename)
    if os.path.isfile(dirFile):
      if (filename.lower().endswith('.gpg') == False):
        subprocess.run(["./script/control.sh", "in", iniPassphrase, dirFile])
    elif os.path.isdir(dirFile):
        if (recursive == True):
          crypto(dirFile+"/")

for f in folders:
  f = f.strip()
  crypto(f)
