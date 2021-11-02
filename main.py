from calcCpuUtil import calc_cpu_util
from calcQueueAverage import calc_queue_avg
from calcThroughput import calc_throughput
from calcTurnaround import calc_turnaround
import generateProcesses 
import calculateProcesses
from generateProcesses import generate_processes
# can't test this yet - imports were written by VSCode... don't need all of them?
def main():
   log = generate_processes()

   cpu_util = calc_cpu_util(log)
   queue_avg = calc_queue_avg(log)
   turnaround = calc_turnaround(log)
   throughput = calc_throughput(log)

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
