import os


def construct_mysql_command(database):
    db_params = filter(lambda x: x.startswith('db_'), database)
    db_name = database.get('db_name', '')
    if db_name:
        db_params.remove('db_name')
    backup = 'mysql_dump.sql'
    if 'backup_dir' in database:
        backup = os.path.join(database['backup_dir'], backup)

    command = ['mysqldump']
    for param in db_params:
        command.append('--{0}={1}'.format(param[3:], database[param]))
    if db_name:
        command.append(db_name)
    command.append('>')
    command.append(backup)
    return command
