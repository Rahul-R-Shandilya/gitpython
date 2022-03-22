import git

repo = git.Repo()

def clone():
    url = input("Enter the url to clone from\t")
    dirname = input("Enter the name to be given for cloned repo\t")
    git.Repo.clone_from(url, dirname)

#clone()

print('Remotes:')
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

def com():
    master = repo.heads.main                         # right-hand side is ahead of us, in the future
    #merge_base = repo.merge_base(new_branch, main)   # allows for a three-way merge
    repo.index.merge_tree(master) 
    for branch in repo.branches:
        print(branch)

    for item in repo.untracked_files:
        print(item)
        repo.index.add([item])
    
    #repo.branch('-M', 'main')
    #Providing a commit
    repo.index.commit("initial commit")

def push():
    com()
    #repo.heads.main.set_tracking_branch(repo.remotes.origin.refs.main)
    print(repo.remotes.origin.push(refspec="main:origin").raise_if_error())
    #print(repo.remotes.origin.push(refspec="main:origin"))


def pull():
    
    com()    
    # Pull from remote repo
    print(repo.remotes.origin.pull(refspec="main:{repo.remote}"))


print("Enter number\n 1. Clone \n 2. Push \n 3. Pull\n")

num = int(input("Waiting for the input\t"))

if num == 1:
    clone()

elif num == 2:
    push()

if num == 3:
    pull()

