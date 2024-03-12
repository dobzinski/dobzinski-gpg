from main import *

def decrypt(path):
  directory = os.fsencode(path)
  for file in os.listdir(directory):
    d = os.fsdecode(directory)
    filename = os.fsdecode(file)
    dirFile = str(d) + str(filename)
    if os.path.isfile(dirFile):
      if (filename.lower().endswith('.gpg') == True):
        subprocess.run(["./script/control.sh", "out", iniPassphrase, dirFile])
    elif os.path.isdir(dirFile):
        if (recursive == True):
          decrypt(dirFile+"/")

for f in folders:
  f = f.strip()
  decrypt(f)
