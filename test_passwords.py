

def crack(first, last, dob, date2, mothers_maiden, spouse, date3, pet1, pet2,
          first_love, child1, child2):
    pass


def test_Isaiah():
    result = crack("Isaiah", "Bailey", "03/29/1956", "03/27/1951", "Morgan",
                   "Brody", "09/20/1954", "Sparky", "Mia", "Ava", "Serenity",
                   "Nevaeh")

    assert("Sparky" in result, "crack in not finding pet as password")
