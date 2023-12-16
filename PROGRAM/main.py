
class Process:
    def __init__(self, name, arrival_time, priority, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.priority = priority
        self.burst_time = burst_time
        self.wait_time = 0  # Track wait time for priority promotion

# Function to perform MLQ scheduling with automatic priority promotion
def mlq_scheduling(processes):
    queue1 = []  # Priority 1 queue (Highest priority - Round Robin)
    queue2 = []  # Priority 2 queue (Medium priority - Shortest Job First)
    queue3 = []  # Priority 3 queue (Lowest priority - First Come First Serve)

    time = 0  # Initialize time

    # Function to promote lower priority processes to higher priority queues
    def promote_priority(queue):
        for process in queue:
            process.wait_time += 1
            if process.priority > 1 and process.wait_time >= 5:
                process.priority -= 1
                process.wait_time = 0
                if process.priority == 1:
                    queue.remove(process)
                    queue1.append(process)
                elif process.priority == 2:
                    queue.remove(process)
                    queue2.append(process)

    # Distributing processes into respective queues based on arrival time
    while processes or queue1 or queue2 or queue3:
        for process in processes:
            if process.arrival_time <= time:
                if process.priority == 1:
                    queue1.append(process)
                elif process.priority == 2:
                    queue2.append(process)
                elif process.priority == 3:
                    queue3.append(process)
                processes.remove(process)

        if queue1:
            current_process = queue1.pop(0)
            print(f"At time {time}: Running process {current_process.name} from Round Robin queue")
            current_process.burst_time -= 2  # Decrease burst time by 2 units for Round Robin
            time += 2

            if current_process.burst_time > 0:
                queue1.append(current_process)

        elif queue2:
            queue2.sort(key=lambda x: x.burst_time)
            current_process = queue2.pop(0)
            print(f"At time {time}: Running process {current_process.name} from Shortest Job First queue")
            current_process.burst_time -= 1  # Decrease burst time by 1 unit for Shortest Job First
            time += 1

            if current_process.burst_time > 0:
                queue2.append(current_process)

        elif queue3:
            current_process = queue3.pop(0)
            print(f"At time {time}: Running process {current_process.name} from First Come First Serve queue")
            current_process.burst_time -= 1  # Decrease burst time by 1 unit for First Come First Serve
            time += 1

            if current_process.burst_time > 0:
                queue3.append(current_process)

        promote_priority(queue3)
        promote_priority(queue2)
def get_user_input():
    processes = []
    num_processes = int(input("Enter the number of processes: "))
    for i in range(1, num_processes + 1):
        name = f"P{i}"
        arrival_time = int(input(f"Enter arrival time for process {name}: "))
        burst_time = int(input(f"Enter burst time for process {name}: "))
        priority = int(input(f"Enter priority level for process {name} (1, 2, or 3): "))
        processes.append(Process(name, arrival_time, priority, burst_time))
    return processes

# Example usage
if __name__ == "__main__":
    # Creating processes with arrival time, priority, and burst times
    processes = get_user_input()

    # Running MLQ scheduling with automatic priority promotion
    mlq_scheduling(processes)