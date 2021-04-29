## Data Structure and Algorithm Exercises

These data structure and algorithm exercises are thoroughly tested, but in different ways.

### Doctest

The divide and conquer exercises (div_n_conquer.py) and linked list class (linked_list.py) have tests in the doc strings.

Run `python -m doctest [filename]` to run the tests.

Add `-v` before the filename to get all the details. Use `python3` instead of `python` if necessary on your machine.

### Unit Tests

All the other flies have their tests in separate files. For me in VS Code, Pylance is unhappy with the imports, but they work for testing.

Run `python -m unittest [filename]` to run the unit tests. Add `-v` before the filename for details. Leave out the filename to run all the test files at once.

(And again, use `python3` instead of `python` if necessary on your machine.)