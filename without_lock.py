import threading
import time
from typing import List

class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance
        
    def withdraw(self, amount: float) -> bool:
        # Simulate some processing time
        time.sleep(0.1)
        
        if self.balance >= amount:
            # Simulate some processing time before updating balance
            time.sleep(0.1)
            self.balance -= amount
            return True
        return False

def make_withdrawal(account: BankAccount, amount: float, thread_name: str):
    if account.withdraw(amount):
        print(f"{thread_name}: Successfully withdrew ${amount}. New balance: ${account.balance}")
    else:
        print(f"{thread_name}: Failed to withdraw ${amount}. Insufficient funds. Balance: ${account.balance}")

# Test the race condition
if __name__ == "__main__":
    # Initialize account with $500
    account = BankAccount(500)
    
    # Create multiple threads trying to withdraw $300 each
    threads: List[threading.Thread] = []
    for i in range(3):
        thread = threading.Thread(
            target=make_withdrawal,
            args=(account, 300, f"Thread-{i+1}")
        )
        threads.append(thread)
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print(f"\nFinal balance: ${account.balance}")