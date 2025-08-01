import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        """Return the item at the front without removing it."""
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all customers up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            return None

        winner = random.choice(self.items)

        while not self.is_empty():
            customer = self.dequeue()
            if customer == winner:
                break

        return winner
