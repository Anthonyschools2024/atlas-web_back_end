# Project: PII, Logging, Password Encryption, and Database Authentication

## 📖 Learning Objectives

At the end of this project, you will be able to explain and implement the following:

* **Personally Identifiable Information (PII):**
    * Provide clear examples of what constitutes PII.
    * Understand the distinction between PII, non-PII, and general personal data.
* **Log Filtering:**
    * Implement a log filter in Python to obfuscate (hide or replace) PII fields within log messages, ensuring sensitive data is not exposed.
* **Password Security:**
    * Encrypt user passwords using the `bcrypt` library.
    * Implement a mechanism to check the validity of an input password against its stored encrypted version.
* **Database Authentication:**
    * Securely authenticate to a database by utilizing environment variables to store and access credentials, avoiding hardcoding sensitive information.

---

## ⚙️ Requirements

### General
* All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3 (version 3.9)**.
* All files should end with a new line.
* The first line of all your files should be exactly `#!/usr/bin/env python3`.
* A `README.md` file (this file) at the root of the folder of the project is mandatory.

### Style & Documentation
* Your code should adhere to the **pycodestyle style (version 2.5)**.
* All your files must be **executable**.
* The length of your files will be tested using `wc`.
* **Documentation is crucial:**
    * All modules must have documentation (e.g., `python3 -c 'print(__import__("my_module").__doc__)'`).
    * All classes must have documentation (e.g., `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
    * All functions (inside and outside a class) must have documentation (e.g., `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
    * A documentation string is a full sentence explaining the purpose of the module, class, or method. Its length will be verified.
* All your functions should be **type-annotated**.

