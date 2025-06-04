# Python Unit and Integration Testing Fundamentals

This project explores the fundamental concepts and practices of unit and integration testing in Python, primarily using the built-in `unittest` framework and associated libraries like `unittest.mock` and `parameterized`. The goal is to understand how to write effective, isolated, and maintainable tests for Python code.

## Core Concepts Covered

### 1. Unit Tests vs. Integration Tests

* **Unit Tests:**
    * Focus: Test the smallest individual components (functions/methods) in isolation.
    * Goal: Verify a single unit works correctly, assuming its external dependencies are perfect (often achieved by mocking).
    * Characteristics: Fast, precise, heavy use of mocks for isolation.
* **Integration Tests:** (Briefly touched upon conceptually)
    * Focus: Test how multiple components interact.
    * Goal: Verify that different parts of the system work together as expected.
    * Characteristics: Less mocking of internal components, potentially slower.

### 2. The `unittest` Framework

Python's standard library for creating and running tests.
* **`unittest.TestCase`**: Base class for test cases. Test methods must start with `test_`.
* **Assertions**: Methods like `assertEqual()`, `assertTrue()`, `assertRaises()` to verify conditions and outcomes.
* **Running Tests**: Typically via `python -m unittest path/to/test_file.py` or `python -m unittest discover`.

### 3. Mocking with `unittest.mock`

Crucial for isolating units under test by replacing dependencies with controllable "fake" objects (mocks).
* **`Mock`**: Flexible objects that can simulate behavior of other objects.
* **`@patch` / `patch.object` (decorator/context manager)**: Temporarily replaces objects (e.g., functions, methods, attributes within a module or on an object) with a mock during a test's scope.
    * Key is to patch where the object is *looked up*, not necessarily where it's defined (e.g., `patch('module_under_test.dependency_name')`).
* **Assertions on Mocks**: Verify interactions with mocks using `assert_called_once()`, `assert_called_once_with()`, `call_count`, etc.

### 4. Parameterization

Run the same test logic with multiple different sets of inputs and expected outputs, keeping tests DRY (Don't Repeat Yourself).
* The **`parameterized`** library (external) is commonly used with `unittest` for this purpose.
* Use `@parameterized.expand([...])` to provide multiple test cases (tuples of arguments) to a single test method.

### 5. Testing Exceptions

Verify that functions raise expected exceptions under specific conditions.
* Use `self.assertRaises(ExpectedException)` as a context manager to ensure the correct exception is raised.
* The context manager also allows inspection of the caught exception (e.g., to check its message).

### 6. Testing Memoization

Verify that decorators or functions designed to cache results behave as expected (e.g., an expensive operation is performed only once for repeated calls with the same effective input).
* Often involves mocking an underlying expensive call and asserting it's called a limited number of times despite multiple calls to the memoized function/method.

## Project & Coding Standards (Illustrative)

The exercises imply adherence to good Python practices:

* **Environment**: Python 3 (e.g., Python 3.9 on Ubuntu 20.04 LTS).
* **Shebang**: `#!/usr/bin/env python3` at the start of all executable `.py` files.
* **Executable Files**: Python scripts intended to be run directly should be executable (`chmod +x`).
* **Style**: Adherence to PEP 8 style guidelines (e.g., via `pycodestyle`).
* **Documentation**:
    * Comprehensive docstrings for all modules, classes, and functions/methods.
    * Docstrings should be descriptive, explaining the purpose, arguments, and return values.
* **Type Annotations**: All functions and methods should include type hints for clarity and static analysis.

## Running Tests

Execute tests using the `unittest` module's command-line interface:

```bash
python -m unittest path/to/your_test_file.py