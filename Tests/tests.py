from Modelle.Kunde import Customer
from Modelle.GekochtesGericht import CookedDish
from Repository.CustomerRepo import CustomerRepo
from Repository.CookedDishRepo import CookedDishRepo

test_dish = [CookedDish(2, 650,500,30)]
test_dish_repo = CookedDishRepo('test_dish.txt')
test_dish_repo.create(test_dish)
new_test_dish = test_dish_repo.read()

def test_add_dish_to_repo():
    assert test_dish[0] == new_test_dish[0]

test_customers = [Customer(32, 'Mara Oprea', 'Floresti'), Customer(21, 'Kira Fonic', 'Ferentari')]
test_customer_repo = CustomerRepo('test_file.txt')
test_customer_repo.save(test_customers)


def test_search_by_name():
    assert test_customer_repo.search_by_name('ma')[0] == test_customers[0]
    assert test_customer_repo.search_by_name('MARA')[0] == test_customers[0]

def test_search_by_address():
    assert test_customer_repo.search_by_address('Feren')[0] == test_customers[1]
    assert test_customer_repo.search_by_address("fer")[0] == test_customers[1]



def run_tests():
    test_search_by_name()
    test_search_by_address()



