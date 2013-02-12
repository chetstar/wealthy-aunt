""" Test cases for our python password cracker """


def possible_passwords(first, last, dob, date2, mothers_maiden, spouse, date3,
                       pet1, pet2, first_love, child1, child2):
    '''Function takes a list of possible data values and returns a list of
    possible passwords'''
    return []


def test_Isaiah():
    result = possible_passwords("Isaiah", "Bailey", "03/29/1956",
                                "03/27/1951", "Morgan", "Brody", "09/20/1954",
                                "Sparky", "Mia", "Ava", "Serenity", "Nevaeh")

    assert("Sparky" in result, "crack in not finding pet as password")


def test_first_love():
    "check if first love is returned as a possible password"
    passwords = possible_passwords('Isaiah', 'Bailey', '03/29/1956', '03/27/1951', 'Morgan',
                                   'Brody', '09/20/1954', 'Sparky', 'Mia', 'Ava', 'Serenity', 'Nevaeh')
    
    assert 'Ava' in passwords, 'Did not find FirstLove in possible passwords'


def test_first_love1():
    "check if first love + # is returned as a possible password"
    passwords = possible_passwords('Isaiah', 'Bailey', '03/29/1956', '03/27/1951', 'Morgan',
                                   'Brody', '09/20/1954', 'Sparky', 'Mia', 'Ava', 'Serenity', 'Nevaeh')
    
    assert 'Ava1' in passwords, 'Did not find FirstLove1 in possible passwords'


def test_Isaiah_first():
    result = possible_passwords("Isaiah", "Bailey", "03/29/1956",
                                "03/27/1951", "Morgan", "Brody", "09/20/1954",
                                "Sparky", "Mia", "Ava", "Serenity", "Nevaeh")

    assert("Isaiah" in result, "crack in not finding first as password")


def test_Isaiah_first_pet1():
    result = possible_passwords("Isaiah", "Bailey", "03/29/1956",
                                "03/27/1951", "Morgan", "Brody", "09/20/1954",
                                "Sparky", "Mia", "Ava", "Serenity", "Nevaeh")

    assert("IsaiahSparky" in result, "crack in not finding first + pet1 as password")


def test_Isaiah_pet1_first():
    result = possible_passwords("Isaiah", "Bailey", "03/29/1956",
                                "03/27/1951", "Morgan", "Brody", "09/20/1954",
                                "Sparky", "Mia", "Ava", "Serenity", "Nevaeh")

    assert("SparkyIsaiah" in result, "crack in not finding pet1 + first as password")
    
def test_dob():
    "check if dob is returned as a possible password"
    passwords = possible_passwords('Isaiah', 'Bailey', '03/29/1956', '03/27/1951', 'Morgan',
                                   'Brody', '09/20/1954', 'Sparky', 'Mia', 'Ava', 'Serenity', 'Nevaeh')
    
    assert('03/29/1956' in passwords, 'Did not find dob in possible passwords')


