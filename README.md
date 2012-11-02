git-backup-tool
===============

Backup your data (mysql or pgsql dumps, media files, scripts, etc) in private git repositories (bitbucket or github).

**Important**: I know - this is a very hardcore way to save data. But I need collect my sql diff's.

It scripts for test this possibility.


Installation
------------

It is a very simple (without 'pip/easy_install' and install requirements)!

Clone/download this repository in any folder. Enjoy! ;)


Example Of Usage: Backup MySQL Dumps
------------------------------------

Create config file (yaml syntax) for all databases:

    first_database:
        database:
            host: 'localhost'
            port: '3306'
            user: 'project'
            password: 'pwd'
            db: 'first_db'
        backup_dir: '/home/backups/mysql_first_db'
        git_remote: 'git@github.com/username/privaterepo.git' # this repo must be empty!
    second_database:
        # ...

And add this command in crontab:

    /path/to/git_backup_tool/backup_mysql.py --config=/path/to/mysql_config.yml

Get profit!
