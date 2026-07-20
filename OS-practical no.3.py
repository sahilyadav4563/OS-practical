import threading
import time

# Function to simulate a task
def task(name):
    print(f"{name} started - Sahil Yadav")
    time.sleep(2)  # Simulate a task taking 2 seconds
    print(f"{name} finished - Sahil Yadav")


# -------- Sequential Execution --------
print("\n--- Sequential Execution ---")

start_time = time.time()

task("Task 1")
task("Task 2")
task("Task 3")
task("Task 4")

end_time = time.time()

print("Sequential Execution Time:", round(end_time - start_time, 2), "seconds")


# -------- Threaded Execution --------
print("\n--- Threaded Execution ---")

start_time = time.time()

# Create threads
t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))
t3 = threading.Thread(target=task, args=("Task 3",))
t4 = threading.Thread(target=task, args=("Task 4",))

# Start all threads
t1.start()
t2.start()
t3.start()
t4.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()
t4.join()

end_time = time.time()

print("Threaded Execution Time:", round(end_time - start_time, 2), "seconds")


# -------- Comparison --------
print("\n--- Comparison ---")
print("Sequential execution takes about 8 seconds because each task runs one after another.")
print("Threaded execution takes about 2 seconds because all four tasks run concurrently.")
print("Threading is more efficient for tasks that involve waiting (I/O-bound tasks).")

print("\nProgram Developed By: Sahil Yadav")
