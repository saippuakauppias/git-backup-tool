import os
from subprocess import Popen, PIPE
from ConfigParser import ConfigParser

#import exceptions


def config_from_file(filename):
    cfg = ConfigParser()
    cfg.read(filename)
    result = {}
    for section in cfg.sections():
        result.update({section: dict(cfg.items(section))})
    return result


def run_command(command, cwd=None, safe=False):
    if isinstance(command, list):
        command = ' '.join(command)
    cmd = Popen(command, cwd=cwd, stdout=PIPE, stderr=PIPE, shell=True)
    err = cmd.stderr.read()
    out = cmd.stdout.read()
    if err:
        if safe:
            print '{0}: {1}'.format(command, err)
        else:
            raise Exception(err)
    return out


def construct_dump_command(database, db_type):
    if db_type == 'pgsql' and 'db_user' in database:
        # magic for pgsql param
        database['db_username'] = database.pop('db_user')

    db_params = filter(lambda x: x.startswith('db_') and x != 'db_name',
                       database)
    db_name = database.get('db_name', '')

    backup = 'mysql_dump.sql' if db_type == 'mysql' else 'pgsql_dump.sql'
    if 'backup_dir' in database:
        backup = os.path.join(database['backup_dir'], backup)

    if db_type == 'mysql':
        command = ['mysqldump']
    elif db_type == 'pgsql':
        command = ['pg_dump', '--format=plain']

    for param in db_params:
        command.append('--{0}={1}'.format(param[3:], database[param]))
    if db_name:
        command.append(db_name)
    command += ['>', backup]
    return command
