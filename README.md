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

Create config file (*.ini syntax) for all databases:

    [first_database]
    db_host     = localhost
    db_port     = 3306
    db_user     = project
    db_password = pwd
    db_name     = first_db
    backup_dir  = /home/backups/mysql_first_db
    git_remote  = git@github.com/username/privaterepo.git

    [second_database]
    ; settings for second database

And add this command in crontab:

    /path/to/git_backup_tool/backup_mysql.py --config=/path/to/mysql_config.ini

Get profit!
