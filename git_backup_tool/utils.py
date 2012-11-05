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
