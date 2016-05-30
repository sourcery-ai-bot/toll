from .compat import mock
from .main import main


def test_main__main__1():
    """It feeds the file handle of the config file into the Configuration."""
    with mock.patch('toll.main.Configuration') as Configuration:
        main(['-c', 'pytest.ini'])
    assert Configuration.called
    assert 'pytest.ini' == Configuration.call_args[0][0].name


def test_main__main__2():
    """It defaults to `toll.ini` as the config file."""
    with mock.patch('toll.main.Configuration') as Configuration:
        main([])
    assert Configuration.called
    assert 'toll.ini' == Configuration.call_args[0][0].name
