"""
Python Fundamentals
08 - Error Handling
Topic: Exceptions

This file covers:
- What exceptions are
- Common Python exceptions
- try and except
- Handling specific exceptions
- Multiple except blocks
- Exception messages
- else
- finally
- Raising exceptions
- Practical error handling examples
"""


# ============================================================
# 1. What Is an Exception?
# ============================================================

"""
An exception is an error that occurs while a program is running.

Examples:

- Dividing by zero
- Converting invalid text to a number
- Accessing an invalid list index
- Accessing a missing dictionary key
- Opening a file that does not exist

If an exception is not handled, the program may stop.
"""


# ============================================================
# 2. Common Exceptions
# ============================================================

"""
Some common Python exceptions:

ZeroDivisionError
    Dividing a number by zero.

ValueError
    Using an invalid value.

TypeError
    Using incompatible data types.

IndexError
    Accessing an invalid list index.

KeyError
    Accessing a missing dictionary key.

FileNotFoundError
    Trying to open a file that does not exist.

NameError
    Using a variable that has not been defined.

AttributeError
    Accessing an attribute or method that does not exist.
"""


# ============================================================
# 3. An Unhandled Exception
# ============================================================

# The following code would stop the program:

# number = 10 / 0

# ZeroDivisionError would occur.


# ============================================================
# 4. Basic try and except
# ============================================================

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================================
# 5. Handling ValueError
# ============================================================

user_input = "abc"

try:
    number = int(user_input)
    print(number)
except ValueError:
    print("Invalid number.")


# ============================================================
# 6. Handling TypeError
# ============================================================

try:
    result = "10" + 5
    print(result)
except TypeError:
    print("Cannot combine these data types.")


# ============================================================
# 7. Handling IndexError
# ============================================================

numbers = [10, 20, 30]

try:
    print(numbers[10])
except IndexError:
    print("Index is out of range.")


# ============================================================
# 8. Handling KeyError
# ============================================================

user = {
    "name": "Mohsen",
    "age": 24
}

try:
    print(user["email"])
except KeyError:
    print("Email key does not exist.")


# ============================================================
# 9. Multiple except Blocks
# ============================================================

try:
    value = int("abc")
    result = 100 / value

except ValueError:
    print("Invalid value.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================================
# 10. Catching Multiple Exceptions
# ============================================================

try:
    value = int("abc")
    result = 100 / value

except (ValueError, ZeroDivisionError):
    print("Invalid calculation.")


# ============================================================
# 11. Getting the Exception Object
# ============================================================

try:
    number = int("abc")

except ValueError as error:
    print(f"Error: {error}")


# ============================================================
# 12. General Exception
# ============================================================

try:
    result = 10 / 0

except Exception as error:
    print(f"An error occurred: {error}")


"""
Using Exception is useful when we need a general fallback.

However, it is usually better to catch specific exceptions
when we know what can go wrong.
"""


# ============================================================
# 13. try / except / else
# ============================================================

try:
    number = int("100")

except ValueError:
    print("Invalid number.")

else:
    print(f"Number: {number}")


"""
The else block runs only when no exception occurs.
"""


# ============================================================
# 14. try / except / finally
# ============================================================

try:
    number = int("100")
    print(number)

except ValueError:
    print("Invalid number.")

finally:
    print("Operation finished.")


"""
The finally block runs whether an exception occurs or not.
"""


# ============================================================
# 15. try / except / else / finally
# ============================================================

try:
    number = int("50")

except ValueError:
    print("Invalid number.")

else:
    print(f"Converted number: {number}")

finally:
    print("Conversion process completed.")


# ============================================================
# 16. Practical Example: User Input
# ============================================================

user_input = "25"

try:
    age = int(user_input)

except ValueError:
    print("Please enter a valid age.")

else:
    print(f"Your age is {age}.")


# ============================================================
# 17. Practical Example: Division
# ============================================================

def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None


print(divide(10, 2))
print(divide(10, 0))


# ============================================================
# 18. Practical Example: Number Conversion
# ============================================================

def convert_to_integer(value):
    try:
        return int(value)

    except ValueError:
        print(f"Cannot convert '{value}' to an integer.")
        return None


print(convert_to_integer("100"))
print(convert_to_integer("Python"))


# ============================================================
# 19. Practical Example: List Access
# ============================================================

def get_item(items, index):
    try:
        return items[index]

    except IndexError:
        print("Invalid index.")
        return None


numbers = [10, 20, 30]

print(get_item(numbers, 1))
print(get_item(numbers, 10))


# ============================================================
# 20. Practical Example: Dictionary Access
# ============================================================

def get_user_email(user):
    try:
        return user["email"]

    except KeyError:
        print("User does not have an email.")

        return None


user = {
    "name": "Mohsen",
    "age": 24
}

print(get_user_email(user))


# ============================================================
# 21. Practical Example: Safe Calculation
# ============================================================

def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)

    except ZeroDivisionError:
        print("Cannot calculate average of an empty list.")

        return None


print(calculate_average([10, 20, 30]))
print(calculate_average([]))


# ============================================================
# 22. Handling Different Errors
# ============================================================

def calculate(value):
    try:
        number = int(value)
        result = 100 / number

        return result

    except ValueError:
        print("Value must be a number.")

    except ZeroDivisionError:
        print("Number cannot be zero.")

    return None


print(calculate("20"))
print(calculate("abc"))
print(calculate("0"))


# ============================================================
# 23. Nested try Blocks
# ============================================================

try:
    value = "100"

    try:
        number = int(value)
        print(number)

    except ValueError:
        print("Inner conversion error.")

except Exception:
    print("Outer error.")


# Nested try blocks should only be used when
# they make the error-handling structure clearer.


# ============================================================
# 24. Raising an Exception
# ============================================================

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age


try:
    age = set_age(-5)
    print(age)

except ValueError as error:
    print(f"Error: {error}")


# ============================================================
# 25. raise with Conditions
# ============================================================

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount


try:
    balance = withdraw(1000, 1500)
    print(balance)

except ValueError as error:
    print(f"Withdrawal failed: {error}")


# ============================================================
# 26. Practical Example: Login Validation
# ============================================================

def login(username, password):
    if not username:
        raise ValueError("Username is required.")

    if not password:
        raise ValueError("Password is required.")

    if username != "admin" or password != "1234":
        raise ValueError("Invalid username or password.")

    return True


try:
    login("admin", "1234")
    print("Login successful.")

except ValueError as error:
    print(f"Login failed: {error}")


# ============================================================
# 27. Practical Example: Product Price
# ============================================================

def set_price(price):
    if price < 0:
        raise ValueError("Price cannot be negative.")

    return price


try:
    price = set_price(500)

    print(f"Price: {price}")

except ValueError as error:
    print(f"Invalid price: {error}")


# ============================================================
# 28. Practical Example: Shopping Cart
# ============================================================

def calculate_cart_total(cart):
    total = 0

    try:
        for item in cart:
            price = item["price"]
            quantity = item["quantity"]

            total += price * quantity

    except KeyError as error:
        print(f"Missing cart field: {error}")
        return None

    except TypeError:
        print("Invalid cart data.")
        return None

    return total


cart = [
    {
        "name": "Keyboard",
        "price": 50,
        "quantity": 2
    },
    {
        "name": "Mouse",
        "price": 25,
        "quantity": 1
    }
]

print(calculate_cart_total(cart))


# ============================================================
# 29. Practical Example: API-Like Data
# ============================================================

response = {
    "status": 200,
    "data": {
        "name": "Mohsen",
        "age": 24
    }
}

try:
    user_name = response["data"]["name"]
    print(f"User: {user_name}")

except KeyError as error:
    print(f"Missing response field: {error}")


# ============================================================
# 30. Practical Example: File Operation
# ============================================================

filename = "example.txt"

try:
    file = open(filename, "r")
    content = file.read()
    file.close()

    print(content)

except FileNotFoundError:
    print(f"File '{filename}' was not found.")


# ============================================================
# 31. finally for Resource Cleanup
# ============================================================

file = None

try:
    file = open("example.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("File not found.")

finally:
    if file is not None:
        file.close()


# ============================================================
# 32. Avoid Bare except
# ============================================================

"""
Avoid writing:

try:
    something()
except:
    pass

This hides errors and makes debugging difficult.

Prefer:

try:
    something()
except ValueError:
    handle_value_error()
"""


# ============================================================
# 33. Do Not Hide Errors Unnecessarily
# ============================================================

def convert_number(value):
    try:
        return int(value)

    except ValueError:
        return None


result = convert_number("Python")

print(result)


# Returning None is appropriate here because
# the caller can decide how to handle the failure.


# ============================================================
# 34. Exception Handling Flow
# ============================================================

"""
The basic flow is:

try
    Code that might raise an exception

except
    Handle the exception

else
    Run when no exception occurred

finally
    Always run cleanup code
"""


# ============================================================
# 35. Practical Example: Order Processing
# ============================================================

def process_order(order):
    try:
        price = order["price"]
        quantity = order["quantity"]

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        total = price * quantity

    except KeyError as error:
        print(f"Missing order field: {error}")
        return None

    except TypeError:
        print("Invalid order data.")
        return None

    except ValueError as error:
        print(f"Invalid order: {error}")
        return None

    else:
        print("Order processed successfully.")

        return total


order = {
    "price": 100,
    "quantity": 3
}

total = process_order(order)

print(f"Total: {total}")


# ============================================================
# 36. Exception Handling Best Practices
# ============================================================

"""
Best practices:

1. Catch specific exceptions.
2. Keep try blocks small.
3. Do not use bare except.
4. Use meaningful error messages.
5. Use finally for cleanup when necessary.
6. Use raise when invalid data should be rejected.
7. Do not silently ignore unexpected errors.
8. Keep business logic separate from error handling.
"""


# ============================================================
# 37. Final Practical Example
# ============================================================

def create_user(name, age):
    if not name:
        raise ValueError("Name is required.")

    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")

    if age < 0:
        raise ValueError("Age cannot be negative.")

    return {
        "name": name,
        "age": age
    }


try:
    user = create_user("Mohsen", 24)

except (ValueError, TypeError) as error:
    print(f"Could not create user: {error}")

else:
    print("User created successfully.")
    print(user)

finally:
    print("User creation process finished.")