import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,10):
    if(not os.path.exists(f"data/day{i}")):
        os.mkdir(f"data/day{i}") # create 10 folder namely day0,day1, day2

for i in range(0,10):
    if(not os.path.exists(f"data/tutorial{i}")):
        os.rename(f"data/day{i}", f"data/tutorial{i}")

folders = os.listdir("data")
for folder in folders:
    print(folder)

print(os.getcwd())
os.chdir("/users")
print(os.getcwd())

print(dir(os))   # dir() print all methods in a particualar module 

# rmdir
# os.path.join