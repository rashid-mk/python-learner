import os

name_file=open("name.txt","r+")
# open("name.txt","w")  write
# open("name.txt","a")  append to last
# open("name.txt","r+") read and
name_file.write("gjhgskcc\nvgdhd\ndbjwb\ndwggwy")
print(name_file.readable())    #check wheather a file readable
print()

print(name_file.read(4))   #read whole fil

print(name_file.readlines())
os.rename("name.txt","name.txt")

name_file.close()   # closing is necessary
print(os.getcwd())
os.chdir("game")
