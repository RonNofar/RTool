'''

Todo:
    * Create prompts for version, description, keywords
'''

import subprocess, shlex, sys
from subprocess import check_output, Popen, PIPE

def main():
    with open('setup.py', 'r') as file:
        data = file.readlines()
    print("Current",data[0])

    print("Tag:")
    tag = None
    if sys.version_info[0] >= 3:
        tag = input(">>> ")
    elif sys.version_info[0] < 3:
        tag = raw_input(">>> ")
    else:
        print("Invalid Python version.")

    data[0] = "tag = \'%s\'\n"%tag
    with open('setup.py', 'w') as file:
        file.writelines(data)

    try:
        run_command("git tag %s"%tag)
    except:
        print("FATAL ERROR: git tag might already exist")
        
    run_command("git add *")
    run_command("git commit -a -m \"Auto Push\" -m \"Tag %s\""%tag)
    run_command("git push --tags origin master")
    run_command("python setup.py sdist upload -r pypi")

def run_command(command):
    print(subprocess.call(command, shell=True))
    '''
    command_args = shlex.split(command)
    with Popen(command_args, stdout=PIPE) as proc:
        print(proc.stdout.read())
    '''

if __name__=="__main__":
    main()


