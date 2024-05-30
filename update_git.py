import os
from git import Repo

def update_git():
    repo = Repo(os.path.dirname(__file__))

    pull = repo.git.pull('origin', 'main')
    print(pull)
    print('- -' * 30)

    status = repo.git.status()
    print(status)
    print('- -' * 30)

    if status.split('\n')[-1] != 'nothing to commit, working tree clean':
        print('add / commit / push')
        repo.git.add('.')
        repo.git.commit('-am', 'auto update')
        push = repo.git.push('origin', 'main')
        print(push)

if __name__ == '__main__':
    update_git()
