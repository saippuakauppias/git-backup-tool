from utils import run_command


def git_init(directory):
    print run_command('git init', directory)


def git_add_all(directory):
    print run_command('git add .', directory)


def git_status(directory):
    return run_command('git status --short', directory)


def git_commit(directory, status):
    print run_command('git commit -am "{0}"'.format(status), directory)


def git_remote_add(directory, git_remote):
    remote_exists = run_command('git remote show', directory)
    if not remote_exists:
        print run_command('git remote add origin {0}'.format(git_remote))


def git_push(directory):
    print run_command('git push -u origin master', directory)
