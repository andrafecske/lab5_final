from Modelle.Kunde import Customer
from Repository.CustomerRepo import CustomerRepo

test_update_customer = Customer(18,'Maria', 'Strada Castana')
test_update_cust_repo = CustomerRepo('test_update_file.txt')
test_update_cust_repo.create(test_update_customer)
cust1 = Customer(18, 'Maria', 'Strada Aluna')

def test_update_customer():
    test_update_cust_repo.update(18, new_address='Strada Aluna')
    assert test_update_cust_repo.read()[0] == cust1
