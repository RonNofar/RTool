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
    t=check_output("git add *", stderr=subprocess.STDOUT)
    print(t)
    t = check_output(
        "git commit -a -m \"Auto Push\" -m \"Tag %s\""%tag,
        stderr=subprocess.STDOUT)
    print(t)
    t=check_output("git tag %s"%tag, shell=True).decode()
    print(t)
    check_output("git push --tags origin master", shell=True).decode()
    check_output("python setup.py sdist upload -r pypi", shell=True).decode()

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc

if __name__=="__main__":
    main()


