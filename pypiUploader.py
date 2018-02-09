import subprocess, shlex
from subprocess import check_output

def main():
    with open('setup.py', 'r') as file:
        data = file.readlines()
    print("Current",data[0])

    print("Tag:")
    tag = input(">>> ")

    data[0] = "tag = \'%s\'\n"%tag
    with open('setup.py', 'w') as file:
        file.writelines(data)

    # stage all files
    run_command("git add *")
    run_command("git commit -a -m \"Auto Push\" -m \"Tag %s\""%tag)
    run_command("git tag %s"%tag)
    run_command("git push --tags origin master")
    run_command("python setup.py sdist upload -r pypi")

def run_command(command):
    print(check_output(
        command,
        stderr=subprocess.STDOUT).decode())

if __name__=="__main__":
    main()


