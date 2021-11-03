# Calculate Results

def get_turnaround(log):
   return 1

def get_throughput(log):
   return 1

def get_queue_avg(log):
   avg_customers_in_system = 10
   return avg_customers_in_system - (log[0] / log[1])

def get_cpu_util(log):
   # util = arrival_rate / service_rate
   return log[0] / log[1]
