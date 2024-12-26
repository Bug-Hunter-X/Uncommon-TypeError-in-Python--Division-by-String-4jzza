def function_with_uncommon_error(x):
    try:
        if not isinstance(x,(int,float)):
            raise TypeError("Cannot divide by non-numeric type")
        result = 10 / x
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None
    return result

# The following lines test the robust function
result1 = function_with_uncommon_error(5)
print(f"Result 1: {result1}") # Output: Result 1: 2.0

result2 = function_with_uncommon_error(0)
print(f"Result 2: {result2}") # Output: Error: Division by zero
Result 2: None

result3 = function_with_uncommon_error("hello")
print(f"Result 3: {result3}") # Output: Error: Cannot divide by non-numeric type
Result 3: None

result4 = function_with_uncommon_error(3.14)
print(f"Result 4: {result4}") # Output: Result 4: 3.1847133757961783