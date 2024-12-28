from project import round_down_age, round_fare, survived_transformation, remove_nicknames, extract_surenames


def test_round_down_age_success():
    assert round_down_age(13.34) == 13
    assert round_down_age(51.50) == 51


def test_round_fare_success():
    assert round_fare(81.3456) == 81.35
    assert round_fare(9.5000) == 9.50
    assert round_fare(136.7792) == 136.78


def test_survived_transformation_success():
    assert survived_transformation(0) == "died"
    assert survived_transformation(1) == "survived"


def test_remove_nicknames_success():
    assert remove_nicknames("Wilkes, Mrs. James (Jamie Willi)") == "Wilkes, Mrs. James"
    assert remove_nicknames('Katavelas, Mr. Vassilios (Catavelas Vassilios")"') == 'Katavelas, Mr. Vassilios'
    assert remove_nicknames('Hocking, Miss. Ellen Nellie""') == "Hocking, Miss. Ellen"


def test_extract_surenames_success():
    assert extract_surenames("") == ""
    assert extract_surenames("Mangiavacchi, Mr. Serafino Emilio") == "Mangiavacchi"
    assert extract_surenames("Corey, Mrs. Percy C (Mary Phyllis Elizabeth Miller)") == "Corey"