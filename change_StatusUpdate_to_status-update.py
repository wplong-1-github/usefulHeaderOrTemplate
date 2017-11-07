import os

for filename in os.listdir("/cnfs/data1/users/chekanov/Dijet2016lepton/data_Apr_2017/data/"):
    if filename.startswith("StatusUpdate"):
        os.rename(filename, "status-update_" + filename[12:])

