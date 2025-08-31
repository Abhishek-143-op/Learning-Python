#               Learning about the concept of Recursion 

print("""
🔹 Definition:
            Recursion is a process in which a function calls itself directly or indirectly to solve a problem.
            It breaks down a big problem into smaller sub-problems of the same type.

      
🔹 Structure of Recursion:
                Every recursive function must have:
                Base Case → Condition to stop recursion (otherwise infinite loop).
                Recursive Case → Function calls itself with a smaller/simpler input.
      

🔹 General Syntax : 
            def function_name(parameters):
                if base_condition:
                    return result       # base case
                else:
                    return function_name(modified_parameters)   # recursive call

""")
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive case

print("Factorial of 5 =", factorial(5))


"""
🔹 Logic Step by Step

                        Start: Call factorial(5).
                        n = 5, not base case → goes to return 5 * factorial(4).

                        Next: To compute factorial(5), Python needs factorial(4).
                        n = 4, not base case → return 4 * factorial(3).

                        Next: To compute factorial(4), Python needs factorial(3).
                        n = 3, not base case → return 3 * factorial(2).

                        Next: To compute factorial(3), Python needs factorial(2).
                        n = 2, not base case → return 2 * factorial(1).

                        Base Case: Now factorial(1).
                        Condition true → returns 1.
                        
                        This stops recursion.

🔹 Unwinding the Calls (Bottom → Up)

Now Python resolves each call in reverse order (stack unwinding):

factorial(1) → 1

factorial(2) → 2 * 1 = 2

factorial(3) → 3 * 2 = 6

factorial(4) → 4 * 6 = 24

factorial(5) → 5 * 24 = 120

✅ Final Answer = 120

"""
