from behave import __main__ as behave

def run_bdd_tests():
    args = ['--format', 'progress', '--no-capture', '--no-capture-stderr', 'features']  # to set cli for Behave
    behave.main(args)  # to run Behave using the cli

if __name__ == '__main__':
    run_bdd_tests()
