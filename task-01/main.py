from queue import Queue
import time
import random

# Create queue 
queue = Queue()

# Request counter
request_id = 1

def generate_request():
    """Generate request and add to queue"""
    global request_id
    request = {
        "id": request_id,
        "data": f"Request data {request_id}"
    }
    
    queue.put(request)
    print(f"Request {request_id} added to queue (total requests: {queue.qsize()}).")
    request_id += 1

def process_request():
    """Processing request from queue"""
    if not queue.empty():
        request = queue.get()
        print(f"Request {request['id']} is being processed ...")
        time.sleep(random.uniform(1.5, 2))
        print(f"Request {request['id']} processing completed ({queue.qsize()} requests left in queue).")
    else:
        print("Queue is empty.")

def main():
    print("Program is running. Press 'Ctrl+C' to exit.")
    
    try:
        while True:
            generate_request()
            process_request()

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")

if __name__ == "__main__":
    initial_requests = random.randint(1, 5)
    for _ in range(initial_requests):
        generate_request()

    main()