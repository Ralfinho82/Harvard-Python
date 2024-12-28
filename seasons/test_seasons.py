from seasons import validate
from seasons import calculate_delta


def test_validate():
    assert validate("1982-08-30").strftime("%Y-%m-%d %H:%M:%S") == "1982-08-30 00:00:00"

