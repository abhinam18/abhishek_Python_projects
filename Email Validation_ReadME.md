# Email Validation Script

A Python script to validate email addresses based on specific rules and conditions. This script ensures that the input email adheres to common standards for formatting and domain usage.

---

## Features

- Validates email length (minimum 6 characters).
- Ensures the email starts with an alphabetic character.
- Checks for exactly one `@` symbol in the email.
- Verifies the domain suffix (e.g., `.edu`, `.com`, `.in`, `.gov`).
- Disallows spaces, uppercase characters, and invalid symbols in the email.

---

## How It Works

1. The user inputs an email address.
2. The script performs the following validations:
   - Checks if the length of the email is at least 6 characters.
   - Ensures the first character is alphabetic.
   - Validates the presence of exactly one `@` symbol.
   - Verifies that the domain suffix matches allowed types.
   - Ensures the email doesn't contain spaces, uppercase letters, or invalid characters.
3. Provides feedback on whether the email is valid or invalid.

---

## Code Example

```python
email = input("Enter the Email: ")
k, j, d = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if email[-4:] in [".edu", ".com", ".in", ".gov"]:
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha() and i.isupper():
                        j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", "@", "."]:
                        continue
                    else:
                        d = 1
                if (k == 1) or (j == 1) or (d == 1):
                    print("Invalid email")
                else:
                    print("Valid email")
            else:
                print("Invalid email: wrong domain")
        else:
            print("Invalid email: incorrect @ symbol usage")
    else:
        print("Invalid email: must start with an alphabet")
else:
    print("Invalid email: too short")
```

---

## Example Usage

### Input
```plaintext
Enter the Email: test_email@domain.com
```

### Output
```plaintext
Valid email
```

### Input
```plaintext
Enter the Email: 1test_email@domain.com
```

### Output
```plaintext
Invalid email: must start with an alphabet
```

---

## Improvements Needed

The current script can be improved by:

1. Fixing logical errors:
   - Ensure correct checks for uppercase letters and invalid characters.
   - Correctly validate the `@` symbol and domain suffix conditions.
2. Refactoring for readability and efficiency.
3. Adding unit tests to verify all validation cases.

---

## Contributions

Feel free to suggest improvements, report bugs, or contribute to the script by submitting pull requests.

