import os

from optparse import OptionParser

from utils import config_from_file, run_command, construct_mysql_command
from git import (git_init, git_add_all, git_status, git_commit,
                 git_remote_add, git_push)


def main(config_file):
    config = config_from_file(config_file)
    for database in config.values():
        # create directory for backup
        if 'backup_dir' in database and \
           not os.path.exists(database['backup_dir']):
            os.makedirs(database['backup_dir'])

        # create empty git repo
        if not os.path.exists(os.path.join(database['backup_dir'], '.git')):
            git_init(database['backup_dir'])

        # backup database
        print run_command(construct_mysql_command(database))

        # add changes in repo
        git_add_all(database['backup_dir'])

        # get status message for commit
        status_message = git_status(database['backup_dir'])
        print status_message

        # commit changes
        git_commit(database['backup_dir'], status_message)

        # add remote for pushing
        git_remote_add(database['backup_dir'], database['git_remote'])

        # push changes
        git_push(database['backup_dir'])

        # done
        print 'Done! Database backuped!'


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-c', '--config', dest='config',
                      help='Configuration file')
    options, _ = parser.parse_args()

    main(options.config)
