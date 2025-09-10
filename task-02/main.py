from collections import deque

def is_palindrome(s: str) -> bool:

    # Format string: keep only alphanumeric in lower case 
    formatted_str = ''.join(c.lower() for c in s if c.isalnum())

    # Create double-ended queue
    dq = deque(formatted_str)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

test = [
    "A man, a plan, a canal, Panama!",
    "Not a palindrome",
    "Do geese see God?",
    "Was it a car or a cat I saw",
    "Mr. Owl ate my metal worm."
]

for str in test:
    print(f"'{str}' -> {is_palindrome(str)}")