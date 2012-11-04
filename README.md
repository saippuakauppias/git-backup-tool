git-backup-tool [![Build Status](https://secure.travis-ci.org/saippuakauppias/git-backup-tool.png)](http://travis-ci.org/saippuakauppias/git-backup-tool)
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
    git_remote  = ssh://git@bitbucket.org/user/private_repo.git

    [second_database]
    ; settings for second database
    db_socket   = /var/run/mysqld/mysqld.sock
    git_remote  = git@github.com:user/private_repo.git


Generate [SSH key](https://help.github.com/articles/generating-ssh-keys) in server for your repositories hoster (github, bitbucket).


Run manually for test errors and add this command in crontab:

    /path/to/git_backup_tool/backup_mysql.py --config=/path/to/mysql_config.ini

Get profit!


Run Tests
---------

    $ python -m unittest tests
