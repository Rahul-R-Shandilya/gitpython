import git
import os
import string
import git_status
from subprocess import *

repo = git.Repo()

def clone():
    url = input("Enter the url to clone from\t")
    dirname = input("Enter the name to be given for cloned repo\t")
    git.Repo.clone_from(url, dirname)



# Git status implementation
""" 
repoDir = 'G:\git automate'

def command(x):
    return str(Popen(x.split(' '), stdout=PIPE).communicate()[0])

def rm_empty(L): return [l for l in L if (l and l!="")]

def getUntracked():
    os.chdir(repoDir)
    status = command("git status")
    if "# Untracked files:" in status:
        untf = status.split("# Untracked files:")[1][1:].split("\n")
        return rm_empty([x[2:] for x in untf if string.strip(x) != "#" and x.startswith("#\t")])
    else:
        return []

def getNew():
    os.chdir(repoDir)
    status = command("git status").split("\n")
    return [x[14:] for x in status if x.startswith("#\tnew file:   ")]

def getModified():
    os.chdir(repoDir)
    status = command("git status").split("\n")
    return [x[14:] for x in status if x.startswith("#\tmodified:   ")]

"""
def stat():
    status = git_status.Status(".")
    print("Added file:")
    print(status.A)
    print("Modified:")
    print(status.M)
    print("Deleted:")
    print(status.D)
    print('Renamed:')
    print(status.R)
    print("Untracked: ")
    print(status.untracked)

    print("Printing using git python\n")
    print(repo.is_dirty())
    print(repo.untracked_files)
    


for remote in repo.remotes:
    print(f'- {remote.name} {remote.url}')


try:
   # url= '' #url='https://github.com/Rahul-R-Shandilya/test.git'
    remote = repo.create_remote('origin', 'https://github.com/Rahul-R-Shandilya/gitpython.git')
    

except git.exc.GitCommandError as error:
    print(f'Error creating remote: {error}') 


# Reference a remote by its name as part of the object
print(f'Remote name: {repo.remotes.origin.name}')
print(f'Remote URL: {repo.remotes.origin.url}')



# List all branches
for branch in repo.branches:
    print(branch)

for item in repo.untracked_files:
    print(item)
    repo.index.add([item])
#repo.remotes.origin.pull(refspec="main:origin")


def rem():
    orig = repo.remotes.origin
    orig.refs
    orig.fetch()
    """ 
    orig.rename('new_origin')
    print(orig.pull())
    print(orig.push())
    """
def com(commitMsg = "initial commit"):
    #master = repo.heads.main                        # right-hand side is ahead of us, in the future
    #merge_base = repo.merge_base(new_branch, main)   # allows for a three-way merge
    #repo.index.merge_tree(master) 
    

    for branch in repo.branches:
        print(branch)


    for item in repo.untracked_files:
        print(item)
        repo.index.add([item])
    """ 
    status = git_status.Status(".")
    for item in status.M:
        print(item)
        repo.index.add([item]) 
    
    """
    #repo.branch('-M', 'main')
    #Providing a commit
    repo.index.commit(commitmsg)

def push(commitmsg:str):
    com(commitmsg)
    #repo.heads.main.set_tracking_branch(repo.remotes.origin.refs.main)
    print(repo.remotes.origin.push(refspec="main:{repo.remotes}").raise_if_error())
    #print(repo.remotes.origin.push(refspec="main:origin"))


def pull(): 
    com()
    

    #print("${repo.active_branch}:${repo.remotes}")
    print(repo.remotes.origin.pull(refspec="main:{repo.remotes}"))


 
print("Enter number\n 1. Clone \n 2. Push \n 3. Pull\n 4. Status\n 5.Remote Repo changes")

num = int(input("Waiting for the input\t"))

if num == 1:
    clone()

elif num == 2:
    push()

if num == 3:
    pull()


if num == 4:
    stat()

if num == 5:
    rem()
#print(repo.remotes)

    
""" 
print(repo.branches)
if repo.branches == 'refs/heads/main':
# Pull from remote repo

"""