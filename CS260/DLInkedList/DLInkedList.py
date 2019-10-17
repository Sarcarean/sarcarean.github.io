class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None
		self.previous = None

class DLinkedList: 

    def __init__(self): 
        self.first_node = None
        self.last_node = None
        self.count = 0

    def add(self, index, data):
        existing_node = getNode(self, index)
        new_node = Node(data)
        prev_node = existing_node.previous
        prev_node.next = new_node
        new_node.next = existing_node
        new_node.previous = prev_node
        self.count = self.count + 1

    def addFirst(self, data):
        new_node = Node(data)
        if self.count==0:
            self.first_node = new_node
            self.last_node = new_node
        else:
            self.first_node.previous = new_node
            new_node.previous = self.last_node
            new_node.next = self.first_node
            self.first_node = new_node
        self.count = self.count + 1

    def addLast(self, data):
        new_node = Node(data);
        if (node_count==0):
            this.first_node = new_node;
            this.last_node = new_node;
            new_node.next = new_node;
            new_node.previous = new_node; 
        else:
            self.last_node.next = new_node
            new_node.next = self.first_node
            new_node.previous = self.last_node
            self.last_node = new_node
            self.first_node.previous = new_node
        self.count = self.count + 1

    def delete(self, index):
        existing_node = getNode(self, index)
        prev_node = existing_node.previous
        next_node = existing_node.next
        prev_node.next = next_node
        next_node.previous = prev_node
        if (index==0):
            this.first_node = next_node
        elif (index==(node_count-1)):
            this.last_node = prev_node
        self.count = self.count - 1

    def size(self):
        return self.count

    def clear(self):
        this.first_node = None
        this.last_node = None
        self.count = 0

    def get(self, index):
        existing_node = getNode(self, index)
        return selected_node.data;

    def getNode(self, index):
        selected_node = self.first_node;
        for i in range(index):
            selected_node = selected_node.next
        return selected_node