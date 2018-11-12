import os

print(1)
print(os.system('git add .'))
print(2)
print(os.system('git pull origin  master'))
print(3)
print(os.system('git commit -m "test script"'))
print(4)
print(os.system('git remote -v '))
print(os.system('git push -u origin master'))