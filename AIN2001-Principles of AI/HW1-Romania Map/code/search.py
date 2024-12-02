from problems import *
import heapq
from collections import deque

##### Queues #####
# First-in-first-out and Last-in-first-out queues, and 
# a PriorityQueue, which allows you to keep a collection of items, 
# and continually remove from it the item with minimum f(item) score.

FIFOQueue = deque

LIFOQueue = list


class PriorityQueue:
    """A queue in which the item with minimum f(item) is always popped first."""

    def __init__(self, items=(), key=lambda x: x):
        self.key = key
        self.items = []  # a heap of (score, item) pairs
        for item in items:
            self.add(item)

    def add(self, item):
        """Add item to the queuez."""
        pair = (self.key(item), item)
        heapq.heappush(self.items, pair)

    def pop(self):
        """Pop and return the item with min f(item) value."""
        return heapq.heappop(self.items)[1]

    def top(self): return self.items[0][1]

    def __len__(self): return len(self.items)

    def __contains__(self, node):
        """Return True if the key is in PriorityQueue."""
        return any([item == node for _, item in self.items])


def depth_first_graph_search(problem):
    "Search deepest nodes in the search tree first."
    # create a frontiers queue
    frontiers = LIFOQueue()

    # create a node for initial state and append it to frontiers
    initial_node = Node(problem.initial)
    frontiers.append(initial_node)

    # create a set to keep track of reached/expanded states
    reached_states = set()

    # go through frontiers queue
    while frontiers:
        # get the node from queue
        node = frontiers.pop()

        # check if it is the goal
        if problem.is_goal(node.state):
            return node

        # add node's state to reached/expanded states set
        reached_states.add(node.state)

        # expand the node
        for child in expand(problem, node):
            # make sure child's state is not reached AND child node is not in the queue
            if child.state not in reached_states and child not in frontiers:
                frontiers.append(child)

    return failure


def breadth_first_graph_search(problem):
    "Search shallowest nodes in the search tree first."
    # create a frontiers queue
    frontiers = FIFOQueue()

    # create a node for the initial state and append it to frontiers
    initial_node = Node(problem.initial)
    frontiers.append(initial_node)

    # create a set to keep track of reached/expanded states
    reached_states = set()

    # go through frontiers queue
    while frontiers:
        # get the node from queue
        node = frontiers.popleft()

        # check if it is the goal
        if problem.is_goal(node.state):
            return node

        # add node's state to reached/expanded states set
        reached_states.add(node.state)

        # expand the node
        for child in expand(problem, node):
            # make sure child's state is not reached AND child node is not in the queue
            if child.state not in reached_states and child not in frontiers:
                frontiers.append(child)

    return failure


def astar(problem):
    # create a frontiers queue
    # Hint: you can use PriorityQueue()
    frontier = PriorityQueue(key=lambda node: problem.h(node) + node.path_cost)

    # create a node for the initial state and append it to frontiers
    initial_node = Node(problem.initial)
    frontier.add(initial_node)

    # create a set to keep track of reached/expanded states
    reached_states = set()

    # go through frontiers queue
    while frontier:
        # get the node from the queue
        node = frontier.pop()

        # check if it is the goal
        if problem.is_goal(node.state):
            return node

        # add node's state to reached/expanded states set
        reached_states.add(node.state)

        # expand the node
        for child in expand(problem, node):
            # make sure child's state is not reached AND child node is not in the queue
            if child.state not in reached_states and child not in frontier:
                frontier.add(child)
            elif child in frontier:
                # If child is already in the frontier, check if we have a cheaper solution
                existing_node = [n for n in frontier.items if n[1] == child][0]
                if node.path_cost < existing_node[0]:
                    frontier.items.remove(existing_node)
                    frontier.add(child)

    return failure



