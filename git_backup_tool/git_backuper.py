import os

from optparse import OptionParser

from utils import config_from_file, run_command, construct_dump_command
from git import (git_init, git_add_all, git_status, git_commit,
                 git_remote_add, git_push)


def main(config_file):
    config = config_from_file(config_file)
    for section, settings in config.items():
        # create directory for backup
        if 'backup_dir' in settings and \
           not os.path.exists(settings['backup_dir']):
            os.makedirs(settings['backup_dir'])

        # create empty git repo
        if not os.path.exists(os.path.join(settings['backup_dir'], '.git')):
            git_init(settings['backup_dir'])

        if settings['type'] in ['mysql', 'pgsql']:
            # backup database
            print run_command(construct_dump_command(settings,
                                                     settings['type']))
        else:
            # backup files
            pass

        # add changes in repo
        git_add_all(settings['backup_dir'])

        # get status message for commit
        status_message = git_status(settings['backup_dir'])
        print status_message

        # commit changes
        git_commit(settings['backup_dir'], status_message)

        # add remote for pushing
        git_remote_add(settings['backup_dir'], settings['git_remote'])

        # push changes
        git_push(settings['backup_dir'])

        # done
        print 'Done! {0} backuped!'.format(section)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-c', '--config', dest='config',
                      help='Configuration file')
    options, _ = parser.parse_args()

    main(options.config)
