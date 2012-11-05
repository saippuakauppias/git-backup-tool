git-backup-tool [![Build Status](https://secure.travis-ci.org/saippuakauppias/git-backup-tool.png)](http://travis-ci.org/saippuakauppias/git-backup-tool)
===============

Backup your data (mysql or pgsql dumps, media files, scripts, etc) in private git repositories (bitbucket or github).

**Important**: I know - this is a very hardcore way to save data. But I need collect my sql diff's.

It scripts for test this possibility.


Installation
------------

It is a very simple (without 'pip/easy_install' and install requirements)!

Clone/download this repository in any folder. Enjoy! ;)


Example Of Usage
----------------

Create config file (*.ini syntax) for all backups (databases, files):

    [mysql_database]
    ; settings for backup MySQL database
    type        = mysql
    db_host     = localhost
    ; db_host or db_socket
    ; db_socket   = /var/run/mysqld/mysqld.sock
    db_port     = 3306
    db_user     = project
    db_password = pwd
    db_name     = first_db
    backup_dir  = /home/backups/mysql_first_db
    git_remote  = ssh://git@bitbucket.org/user/private_repo.git

    [pgsql_database]
    ; settings for backup PostgreSQL
    type        = pgsql
    db_host     = localhost
    db_port     = 5432
    db_user     = project
    db_password = pwd
    db_name     = database_name
    backup_dir  = /home/backups/pgsql_db
    git_remote  = git@github.com:user/private_repo.git

    [scripts_backup]
    ; settings for backup scripts (any files)
    type        = files
    ; copy all files from files_dir to backup_dir
    ; create in files_dir .gitignore file for exclude any files/dirs
    files_dir   = /home/user/src
    backup_dir  = /home/backups/src
    git_remote  = git@github.com:user/private_src_repo.git


Generate [SSH key](https://help.github.com/articles/generating-ssh-keys) in server for your repositories hoster (github, bitbucket).


Run manually for test errors and add this command in crontab:

    /path/to/git_backup_tool/git_backuper.py --config=/path/to/config.ini

Get profit!


Run Tests
---------

    $ python -m unittest tests
