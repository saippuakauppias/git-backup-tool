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
