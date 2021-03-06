from . import config
from .run import Runner
import argparse


def main(raw_args=None):
    """Console script entry point."""
    parser = argparse.ArgumentParser(
        description="poor man's integration testing")
    parser.add_argument(
        'cmds', metavar='cmd', default=['test'], nargs='*',
        help='Run command(s) defined in the configuration file. Each command '
             'is run on each package before proceeding with the next command. '
             '(default: "test")')
    parser.add_argument(
        '-c', '--config', dest='file', type=argparse.FileType('r'),
        default='toll.ini',
        help='ini-style file to read the configuration from')
    parser.add_argument(
        '--start-at', dest='start_at', type=str, default='',
        help='Skip over the packages in the config file listed before this'
             ' one. (It does a substring match to find the first package.)')

    args = parser.parse_args(raw_args)
    config_file = config.parsed_file(args.file)
    commands = config.commands(config_file, args.cmds)
    packages = config.packages(config_file)
    runner = Runner(commands, packages, start_at=args.start_at)
    return runner()
