from Event import Event, EventQueue
import random
import math


idle = True
ready_queue_count = 0

def generate_processes(ARRIVAL_RATE, AVERAGE_SERVICE_TIME):

   # Initialize variables
   busy_time = 0
   clock = 0
   total_time = 0

   # Initialize event queue and schedule first event
   our_event_queue = EventQueue()
   schedule_event(0, clock + exp_dist_gen(ARRIVAL_RATE), our_event_queue)

   # Simulate 10,000 processes
   for i in range(0, 10000):
      old_clock = clock
      time_elapsed = clock - old_clock
      
      # Get current event
      current_event = our_event_queue.get_head()
      clock = current_event.get_time()

      if (not idle):
         busy_time += time_elapsed

      # Switch statement but in python 3.10
      # Arrival == 0, Departure == 1
      match current_event.get_event_type:
         case 0:
            arrival_handler(current_event, ARRIVAL_RATE, clock, our_event_queue)
            return 
         case 1:
            departure_handler(current_event, ARRIVAL_RATE, clock, our_event_queue)
            return

      our_event_queue.remove_event()
   
   # List of state variables from simulator
   return [ARRIVAL_RATE,AVERAGE_SERVICE_TIME, clock, busy_time]
         
# Arrival Handler
def arrival_handler(current_event, ARRIVAL_RATE, clock, our_event_queue):
   global idle, ready_queue_count

   if (idle):
      idle = False
      schedule_event(1, clock + exp_dist_gen(ARRIVAL_RATE), our_event_queue)
   else:
      ready_queue_count += 1
   schedule_event(0, clock + exp_dist_gen(ARRIVAL_RATE), our_event_queue)

# Departure handler
def departure_handler(current_event, ARRIVAL_RATE, clock, our_event_queue):
   global idle, ready_queue_count

   if (ready_queue_count == 0):
      idle = True
   else:
      ready_queue_count -= 1
      schedule_event(1, clock + exp_dist_gen(ARRIVAL_RATE), our_event_queue)


##########################
# HELPER FUNCTIONS BELOW #
##########################

# Schedule new event and insert into queue
def schedule_event(event_type, time, queue_head):
   new_event = Event(event_type, time, None)
   if queue_head.get_head() is None:
      queue_head.set_head(new_event)
      return 
   queue_head.add_event(new_event)

# Generate exponential distribution
def exp_dist_gen(ARRIVAL_RATE):
   random_number = uniform_random()
   return (-1) * (1 / (1 / ARRIVAL_RATE)) * math.log(random_number)

# Generate random number from 0 - 1
def uniform_random():
   return random.random()

