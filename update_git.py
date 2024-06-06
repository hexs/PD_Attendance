import json
import os
import psutil
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
    print('status', status, '- -' * 30, sep='\n')
    if status.split('\n')[-1] != 'nothing to commit, working tree clean':
        add = repo.git.add('.')
        print('add', add, '- -' * 30, sep='\n')
        for v in status.split('\n'):
            if '	modified:   ' in v:
                print(v.split('	modified:   ')[-1])
                break
        else:
            v = ''
        commit = repo.git.commit('-am', f'auto update {v.strip()}')
        print('commit', commit, '- -' * 30, sep='\n')

        try:
            push = repo.git.push('origin', 'main')
            print('push', push, '- -' * 30, sep='\n')
        except Exception as e:
            if 'fatal: Authentication failed for' in str(e):
                repo.git.remote('remove', 'origin')

                users = psutil.users()
                user_name = (users[0].name)
                with open(rf'C:\Users\{user_name}\Documents\remote_origin_url.txt') as f:
                    new_url = f.read().replace('<project_name>', 'PD_Attendance')
                repo.git.remote('add', 'origin', new_url)

                push = repo.git.push('origin', 'main')
                print('push', push, '- -' * 30, sep='\n')


if __name__ == '__main__':
    if_status_change_add_commit_push()
