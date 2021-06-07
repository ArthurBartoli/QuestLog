from tests.objective_test import obj_test
from tests.questlog_test import questlog_test

if obj_test and questlog_test:
    print("ALL TESTS COMPLETED AND VALID")
else:
    print("ONE OF THE TESTS RETURNED FALSE")
