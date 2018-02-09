from subprocess import check_output

with open('setup.py', 'r') as file:
    data = file.readlines()
print("Current",data[0])

print("Tag:")
tag = input(">>> ")

data[0] = "tag = \'%s\'\n"%tag
with open('setup.py', 'w') as file:
    file.writelines(data)

# stage all files
t=check_output("git add *", shell=True).decode()
print(t)
check_output(
    "git commit -a -m \"Auto Push\" -m \"Tag %s\""%tag,
    shell=True).decode()
t=check_output("git tag %s"%tag, shell=True).decode()
print(t)
check_output("git push --tags origin master", shell=True).decode()
check_output("python setup.py sdist upload -r pypi", shell=True).decode()


