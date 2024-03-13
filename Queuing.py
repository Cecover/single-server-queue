"""
're-written from scratch' queuing system for a single-server scenario
"""

import numpy as np


class QueuingSimulator:

    def __init__(self):
        """
        Initializing values and some variables
        """

        self.queue_limit: int = 100
        self.is_server_busy: bool = False  # Defaults to false
        self.num_events: int = 1000
        self.mean_service: float = 0.0
        self.num_delays_required: int = 0

    def initialize_simulation(self):
        sim_time = 0.0  # Simulation clock

        is_idle: bool = True
        num_in_queue: int = 0
        time_from_last_event: float = 0.0
        num_customer_delayed: int = 0
        total_delay: float = 0.0
        area_number_in_queue: float = 0.0
        area_server_status: float = 0.0
        mean_interarrival: float = 0.0

        time_next_event = list()

        time_next_event[1] = sim_time + np.exp(mean_interarrival)
        time_next_event[2] = 1.0e+30

        return (sim_time,
                is_idle,
                num_in_queue,
                time_from_last_event,
                num_customer_delayed,
                total_delay,
                area_number_in_queue,
                area_server_status,
                time_next_event,
                mean_interarrival)

    def timing(self, sim_time, num_events, time_next_event):
        """
        Timing function
        """

        next_event_type = 0
        min_time_next_event = 1.0e+29

        for i in range(num_events):
            if time_next_event[i] < min_time_next_event:
                min_time_next_event = time_next_event[i]
                next_event_type = i

        # Checking if the list is empty

        if next_event_type == 0:
            print("Event list is empty at the time!", sim_time)
            exit(1)

        else:

            sim_time = min_time_next_event

        return sim_time, next_event_type

    def update_time_average(self,
                            sim_time,
                            time_last_event,
                            num_in_queue,
                            server_status
                            ):

        time_since_last_event = sim_time - time_last_event
        time_last_event = sim_time

        area_number_in_queue = 0.0
        area_server_status = 0.0

        # Update area under number-in-queue function
        area_number_in_queue += num_in_queue * time_since_last_event

        # Update urea under server-busy indicator function
        area_server_status += server_status * time_since_last_event

        return area_number_in_queue, area_server_status, time_last_event

    def arrive(self, server_status, num_in_queue, time_next_event, sim_time, mean_interarrival):
        """
        Arrival event function
        """

        time_next_event[1] = sim_time + np.exp(mean_interarrival)
        time_arrival = list()
        total_delays = 0
        num_customers_delayed = 0

        if server_status is True:

            num_in_queue += 1

            if num_in_queue > self.queue_limit:
                print("Overflow of the array time_arrival at", sim_time)
                exit(2)

            time_arrival[num_in_queue] = sim_time

        else:

            """
            In this case, the server is idle so arriving customers has a delay of zero
            """

            delay = 0.0
            total_delays += delay

            # Incrementing the number of delayed customers

            num_customers_delayed += 1
            server_status = True

            # Schedule a departure
            time_next_event[2] = sim_time + np.exp(self.mean_service)

        return server_status, time_next_event, num_customers_delayed

    def depart(self, num_in_queue, sim_time, time_arrival, total_of_delays, num_customers_delayed, time_next_event):
        if num_in_queue == 0:

            is_busy = False
            time_next_event = 1.0e+30

        else:

            # The queue is not empty, so decrement the number of customers in the queue

            num_in_queue -= 1

            # Compute the delay

            delay = sim_time - time_arrival[1]
            total_of_delays += delay

            # Increment the number of delayed customers

            num_customers_delayed += 1
            time_next_event[2] = sim_time + np.exp(mean_service)

            # Move each customer in the queue by one place

            for i in num_in_queue:
                time_arrival[i] = time_arrival[i + 1]

        return 

    def __call__(self):

        # Initializing variables
        sim_time, is_idle, num_in_queue, time_last_event, num_customer_delayed, total_delay, area_number_in_queue, area_server_status, time_next_event, mean_interarrival = self.initialize_simulation()

        is_on: bool = True  # Infinite loop

        while is_on:

            # Determine the next event
            sim_time, next_event_type = self.timing(sim_time, self.num_events, time_next_event)

            # Update time-average statistical accumulator

            area_number_in_queue, area_server_status, time_last_event = self.update_time_average(sim_tim

            # Invoke proper functions

            if next_event_type == 1:
                server_status, time_next_event, num_customer_delayed = self.arrive(is_idle, num_in_queue, time_next_event, sim_time, mean_interarrival)

            elif next_event_type == 2:
                self.depart()

            if next_event_type == 3:
                self.report()  # replace with simple output of values and FUCK OFF
                break




