# Personal Data

This project focuses on handling Personally Identifiable Information (PII) in a secure manner within a web back-end context.

## Learning Objectives
* Identify examples of PII.
* Implement log filters to obfuscate sensitive data.
* Encrypt user passwords using `bcrypt`.
* Authenticate to a database using environment variables.

## Tasks

### 0. Regex-ing
- **File:** `filtered_logger.py`
- **Description:** Contains a function `filter_datum` that uses `re.sub` to obfuscate PII in log messages based on a list of fields.