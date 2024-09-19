class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        popped_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return popped_node.data


def process_queries(queries):
    queue = Queue()
    results = []
    for query in queries:
        if query[0] == 1:
            queue.enqueue(query[1])
        elif query[0] == 2:
            popped_value = queue.dequeue()
            if popped_value is not None:
                results.append(popped_value)
    return results

Q = 5
queries = [(1, 2), (1, 3), (2,), (1, 4), (2,)]
output = process_queries(queries)
print(output)