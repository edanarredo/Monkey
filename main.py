from generateProcesses import generate_processes
from calculateProcesses import get_cpu_util, get_queue_avg, get_turnaround, get_throughput

def main():

   # define constants
   ARRIVAL_RATE = float(input("Enter an arrival rate: "))
   AVERAGE_SERVICE_TIME = float(input("Enter an average service time: "))

   # Run simulation - log[ARRIVAL_RATE, AVERAGE_SERVICE_TIME, CLOCK, BUSY_TIME]
   log = generate_processes(ARRIVAL_RATE, AVERAGE_SERVICE_TIME)

   # Calculate simulation results
   cpu_util = get_cpu_util(log)
   queue_avg = get_queue_avg(log)
   turnaround = get_turnaround(log)
   throughput = get_throughput(log)

   # Output results
   output_results(cpu_util, queue_avg, turnaround, throughput)


def output_results(cpu_util, queue_avg, turnaround, throughput):
   print("Results")
   print("+-------------------------+")
   print(f"Average CPU Utilization: {cpu_util}")
   print(f"Average Turnaround Time: {turnaround}")
   print(f"Average Processes in Ready Queue: {queue_avg}")
   print(f"Total Throughput: {throughput}")
   print("+-------------------------+")
   print("\nNow Exiting...")

main()