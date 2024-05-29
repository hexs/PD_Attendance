from git import Repo

repo = Repo()

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
