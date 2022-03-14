from ci_practice import __version__, main


def test_name():
    assert "This is ci-practice" == main.app()


def test_version():
    assert __version__ == "0.2.0"


def test_addition():
    assert 4 == main.add(2, 2)


def test_subtraction():
    assert 2 == main.subtract(4, 2)
