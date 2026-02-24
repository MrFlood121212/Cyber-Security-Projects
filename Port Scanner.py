import socket
import threading
from queue import Queue

target = input("Enter target IP or hostname: ")
start_port = 0
end_port = 65535
threads = 200  # adjust for speed vs stability

queue = Queue()

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))  # TCP handshake attempt
            if result == 0:
                print(f"[OPEN] Port {port}")
    except Exception:
        pass

def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

# Fill the queue
for port in range(start_port, end_port + 1):
    queue.put(port)

print(f"Scanning {target} from port {start_port} to {end_port}...")

# Start threads
thread_list = []
for _ in range(threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    thread_list.append(t)

queue.join()

print("Scan complete.")