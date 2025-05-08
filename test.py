import time

start_time = time.time()
print("hello world")
print(f"time in time.time format: {time.time()}")
end_time = time.time()

run_time = end_time - start_time

print(f"used {run_time:.4f} seconds to run")

