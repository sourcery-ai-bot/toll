from .run import Runner
import pkg_resources
import sys


class MockConfig:
    """Mock of the the configuration."""

    commands = {'test': '{0.executable} setup.py -q test'.format(sys)}

    def __init__(self, packages):
        self.packages = [
            pkg_resources.resource_filename('toll', 'fixtures/{}'.format(x))
            for x in packages]


def test_run____call____1():
    """It returns `True` on success of all packages."""
    runner = Runner(MockConfig(['fine', 'finetoo']))
    assert True is runner()


def test_run____call____2(capsys):
    """It prints the tests results to stdout."""
    runner = Runner(MockConfig(['fine', 'finetoo']))
    runner()
    out, err = capsys.readouterr()
    assert 'Testing {}'.format(runner.config.packages[0]) in out
    assert 'Testing {}'.format(runner.config.packages[1]) in out
    assert 2 == out.count('OK')
    assert out.strip().endswith('SUCCESS :-)')


def test_run____call____3(capsys):
    """It stops after the first package with a failure."""
    runner = Runner(MockConfig(['bad', 'fine']))
    runner()
    out, err = capsys.readouterr()
    assert 'Testing {}'.format(runner.config.packages[0]) in out
    assert 'FAILED (failures=1)' in out
    assert 'Testing {}'.format(runner.config.packages[1]) not in out
    assert 'OK' not in out
    assert out.strip().endswith('FAILURE :-(')
