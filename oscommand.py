import os

print(1)
print(os.system('git add .'))
print(2)
print(os.system('git pull origin  master'))
print(3)
print(os.system('git commit -m "test script"'))
print(4)
# print(os.system('git remote -v '))
print(os.system('git remote rm origin'))
print(os.system('git remote add origin git@github.com:busizshen/busizshen.github.io.git'))
print(os.system('git push -u origin master'))