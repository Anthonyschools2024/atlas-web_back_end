# Python Unit and Integration Testing Fundamentals

This project explores the fundamental concepts and practices of unit and integration testing in Python, primarily using the built-in `unittest` framework and related libraries. The goal is to understand how to write effective, isolated, and maintainable tests.

## Core Concepts

### 1. Unit Tests vs. Integration Tests

* **Unit Tests:**
    * Focus: Test the smallest individual components (functions/methods) in isolation.
    * Goal: Verify a single unit works correctly, assuming its external dependencies are perfect (often mocked).
    * Characteristics: Fast, precise, heavy use of mocks.
* **Integration Tests:**
    * Focus: Test how multiple components interact.
    * Goal: Verify that different parts of the system work together as expected.
    * Characteristics: Less mocking of internal components, potentially slower, tests broader workflows.

### 2. The `unittest` Framework

Python's standard library for creating and running tests.
* **`unittest.TestCase`**: Create test classes by inheriting from this. Test methods must start with `test_`.
* **Assertions**: Use methods like `assertEqual()`, `assertTrue()`, `assertRaises()` to verify outcomes.
* **Running Tests**: Typically with `python -m unittest path/to/test_file.py` or `python -m unittest discover`.

### 3. Mocking with `unittest.mock`

Essential for isolating units under test by replacing dependencies with controllable "fake" objects.
* **`Mock`**: Flexible objects that can simulate any behavior.
* **`@patch` (decorator/context manager)**: Temporarily replaces objects within a specific scope (e.g., `requests.get`). Key is to patch where the object is *looked up*, not where it's defined.
* **`PropertyMock`**: Used for mocking properties, especially read-only ones.
* **Assertions on Mocks**: Verify calls with `assert_called_once_with()`, `call_count`, etc.

### 4. Parameterization

Run the same test logic with different sets of inputs and expected outputs to keep tests DRY.
* The **`parameterized`** library (external) is commonly used with `unittest`.
* Use `@parameterized.expand([...])` to provide multiple test cases to a single test method.

### 5. Fixtures (`setUp` / `tearDown`)

Manage the state and resources needed for tests.
* **`setUp(self)` / `tearDown(self)`**: Run before/after *each* test method in a class. For per-test setup/cleanup.
* **`setUpClass(cls)` / `tearDownClass(cls)`**: Run once before/after *all* tests in a class. For shared, more expensive setup/cleanup.

### 6. Memoization

An optimization technique caching results of expensive function calls. While not strictly a testing pattern, it can be relevant when testing code that uses memoization or for optimizing test helper functions (though rare). Python 3.9+ offers `@functools.cache`.

## Project & Coding Standards

This project emphasizes clean, well-documented, and type-safe Python code:

* **Environment**: Python 3.9 on Ubuntu 20.04 LTS.
* **Shebang**: `#!/usr/bin/env python3` at the start of all `.py` files.
* **Executable Files**: All Python scripts should be executable (`chmod +x`).
* **`pycodestyle` (v2.5)**: Code must adhere to PEP 8 style guidelines.
* **Documentation**:
    * Comprehensive docstrings for all modules, classes, and functions/methods.
    * Docstrings should be descriptive sentences explaining the purpose.
* **Type Annotations**: All functions and methods must include type hints.

## Running Tests

Execute tests using the `unittest` module's command-line interface:

```bash
python -m unittest path/to/your_test_file.py