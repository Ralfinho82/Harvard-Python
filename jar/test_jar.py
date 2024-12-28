import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
        assert init(jar) == "Capacity cannot be negative"


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        assert jar.deposit(-1) == "Deposit amount cannot be negative"


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        assert jar.withdraw(-1) == "Withdrawal amount cannot be negative"
