                    # Infinite Loops in Python
# Infinite loops are loops that run forever. They are also called endless loops. 
# How to create an infinite loop in Python or What feature of Python causes an infinite loop? The feature of Python that causes an infinite loop is the absence of a condition that can be evaluated to False.
# Example of an infinite loop in Python:
while True:
    name = input("Enter your name: ")
    if name == "Hacker":
        continue
    if name == "exit":
        break
    print("Hello", name)
# In short, an infinite loop is a loop that runs forever. Which means that the condition that controls the loop is never evaluated to False. (The condition is always True. The condition is never False. No increment or decrement operation is performed on the variable that controls the loop. While True:)