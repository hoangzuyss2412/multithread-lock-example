import threading
import time

class Counter:
    def __init__(self):
        self.count = 0
        
    def increment(self):
        # Get current value
        current = self.count
        # Simulate some processing time to make race condition more likely
        time.sleep(0.0001)
        # Increment
        self.count = current + 1

class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()
        
    def increment(self):
        with self.lock:
            current = self.count
            time.sleep(0.0001)  # Simulate some processing time
            self.count = current + 1

def run_counter_test(counter, num_threads=100):
    threads = []
    
    # Create threads that will increment the counter
    for _ in range(num_threads):
        thread = threading.Thread(target=counter.increment)
        threads.append(thread)
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return counter.count

# Test unsafe counter
print("Testing unsafe counter...")
unsafe_counter = Counter()
final_unsafe_count = run_counter_test(unsafe_counter)
print(f"Expected count: 100")
print(f"Actual count: {final_unsafe_count}")

# Test safe counter
print("\nTesting safe counter...")
safe_counter = SafeCounter()
final_safe_count = run_counter_test(safe_counter)
print(f"Expected count: 100")
print(f"Actual count: {final_safe_count}")