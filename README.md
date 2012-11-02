git-backup-tool
===============

Backup your data (mysql or pgsql dumps, media files, scripts, etc) in private git repositories (bitbucket or github).

Important: I know - this is very hardcore way to save your data. But I need collect my sql diff's.

It scripts for test this possibility.


Installation
------------

Clone/download this repository in any folder. End! ;)


Example Of Usage: Backup MySQL Dumps
------------------------------------

Create config file (yaml syntax) for all databases:

    first_database:
        database:
            host: 'localhost'
            port: '3306'
            user: 'project'
            password: 'pwd'
            db: 'db_name'
        backup_dir: '/home/backups/mysql'
    second_database:
        # ...


And add this command in crontab:

    /path/to/git_backup_tool/backup_mysql.py --config=/path/to/config.yml

Get profit!
