def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    stack = []
    matching = {')', '(', '}', '{', ']', '['}

    for character in s:
        if character in matching.values():
            stack.append(character)
        elif character in matching:
            if not stack or stack[-1] != matching[character]:
                return False
            stack.pop()

    return not stack

# Create an empty list to simulate stack
# Create a dict to map closing -> opening brackets
# Loop through the input string
    # If its an opening bracket, push to stack
    # If its a closing bracket:
        # If the stack is empty, return false
        # If the top of the stack doesnt match the cooresponding opening, return false
        # Otherwise, pop the opening
    # After the loop:
        # If yes, return True
        # If not, return False

