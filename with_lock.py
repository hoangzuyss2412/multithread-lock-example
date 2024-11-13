import threading
import time
from typing import List

class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance
        self.lock = threading.Lock()
        
    def withdraw(self, amount: float) -> bool:
        with self.lock:  # Acquire lock before checking and updating balance
            time.sleep(0.1)  # Simulate some processing time
            
            if self.balance >= amount:
                time.sleep(0.1)  # Simulate some processing time
                self.balance -= amount
                return True
            return False

def make_withdrawal(account: BankAccount, amount: float, thread_name: str):
    if account.withdraw(amount):
        print(f"{thread_name}: Successfully withdrew ${amount}. New balance: ${account.balance}")
    else:
        print(f"{thread_name}: Failed to withdraw ${amount}. Insufficient funds. Balance: ${account.balance}")

# Test with lock
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