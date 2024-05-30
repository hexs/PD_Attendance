import json
import os
from git import Repo

with open('config.json') as f:
    config = json.loads(f.read())
def update_git():
    repo = Repo(config['Directory'])

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


def if_status_change_add_commit_push():
    repo = Repo(config['Directory'])
    status = repo.git.status()

    if status.split('\n')[-1] != 'nothing to commit, working tree clean':
        add = repo.git.add('.')
        print('add', add, '- -' * 30, sep='\n')
        commit = repo.git.commit('-am', 'auto update')
        print('commit', commit, '- -' * 30, sep='\n')
        push = repo.git.push('origin', 'main')
        print('push', push, '- -' * 30, sep='\n')


if __name__ == '__main__':
    update_git()
