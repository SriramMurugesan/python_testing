def get_weather(temp):
    if temp >= 30:
        return "Hot"
    elif temp <= 10:
        return "Cold"
    else:
        return "Normal"
    
def add(a, b):
    return a + b
    
def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class UserManager:
    def __init__(self):
        self.users = {}
    
    def add_user(self, user_id, user):
        if user_id in self.users:
            raise ValueError("User already exists")
        self.users[user_id] = user
        return True

    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def remove_user(self, user_id):
        if user_id not in self.users:
            raise ValueError("User does not exist")
        del self.users[user_id]
        return True


def is_prime(n):
    """Check if a number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if number is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True