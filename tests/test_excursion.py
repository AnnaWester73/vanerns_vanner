from src.excursion import Excursion

# Test att medlem kan läggas till
def test_add_member():
    excursion = Excursion()

    excursion.add_member("Anna")

    assert excursion.get_members() == ["Anna"]

# Test att medlem kan tas bort
def test_remove_member():
    excursion = Excursion()
    excursion.add_member("Anna")

    excursion.remove_member("Anna")

    assert excursion.get_members() == []

# Test att hämta medlemmar
def test_get_members():
    excursion = Excursion()
    excursion.add_member("Anna")
    excursion.add_member("Lena")

    members = excursion.get_members()

    assert members == ["Anna", "Lena"]


# Test vad medlem hyrt
def test_register_item_rented():
    excursion = Excursion()
    excursion.add_member("Anna")

    excursion.register_item_rented("Anna", "Tält")

    assert excursion.rented_items["Anna"] == ["Tält"]


# Test vad medlem lämnat tillbaka
def test_register_item_returned():
    excursion = Excursion()
    excursion.add_member("Anna")

    excursion.register_item_rented("Anna", "Tält")
    excursion.register_item_returned("Anna", "Tält")

    assert excursion.rented_items["Anna"] == []


# Test där medlem inte lämnat tillbaka
def test_member_has_not_returned_item():
    excursion = Excursion()

    excursion.add_member("Anna")
    excursion.register_item_rented("Anna", "Tält")
    result = excursion.get_all_who_has_not_returned_items()

    assert result == ["Anna"]

# Test där medlem lämna tillbaka
def test_member_has_returned_item():
    excursion = Excursion()

    excursion.add_member("Anna")
    excursion.register_item_rented("Anna", "Tält")
    excursion.register_item_returned("Anna", "Tält")
    result = excursion.get_all_who_has_not_returned_items()

    assert result == []

# Test med flera medlemmar där en lämnat tillbaka
def test_multiple_members_one_returned_item():
    excursion = Excursion()

    excursion.add_member("Anna")
    excursion.add_member("Lena")

    excursion.register_item_rented("Anna", "Tält")
    excursion.register_item_rented("Lena", "Stormkök")

    excursion.register_item_returned("Anna", "Tält")

    result = excursion.get_all_who_has_not_returned_items()

    assert result == ["Lena"]