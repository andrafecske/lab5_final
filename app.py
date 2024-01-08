from UI.Console import Console
from Tests import tests
from Tests import test_update

def main():
    console = Console()
    console.run()
    tests.run_tests()
    test_update.test_update_customer()

main()

