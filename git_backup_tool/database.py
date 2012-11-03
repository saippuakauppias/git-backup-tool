import os


def construct_mysql_command(database):
    db_params = filter(lambda x: x.startswith('db_'), database)
    db_name = database.get('db_name', '')
    if db_name:
        db_params.remove('db_name')
    command = 'mysqldump'

    for param in db_params:
        command += ' --{0}={1}'.format(param.lstrip('db_'), database[param])
    if db_name:
        command += ' {0}'.format(db_name)
    command += ' > '
    if 'backup_dir' in database:
        backup = os.path.join(database['backup_dir'], 'mysql_dump.sql')
    else:
        backup = 'mysql_dump.sql'
    command += '{0}'.format(backup)
    return command
