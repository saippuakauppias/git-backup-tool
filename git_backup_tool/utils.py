from subprocess import Popen, PIPE
from ConfigParser import ConfigParser

from exceptions import RunCommandError


def config_from_file(filename):
    cfg = ConfigParser()
    cfg.read(filename)
    result = {}
    for section in cfg.sections():
        result.update({section: dict(cfg.items(section))})
    return result


def run_command(command, cwd=None):
    cmd = Popen(command, cwd=cwd, stdout=PIPE, stderr=PIPE)
    err = cmd.stderr.read()
    out = cmd.stdout.read()
    if err:
        raise RunCommandError(err)
    return out
