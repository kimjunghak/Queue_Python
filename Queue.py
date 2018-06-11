class Queue:
	
	def __init__(self):
		self.length = 0
		self.head = None

	def size(self):
		return self.length

	def empty(self):
		return (self.length == 0)

	def put(self, item):
		node = Node(item)

		if(self.head == None):
			self.head = node
		else:
			p = self.head
			while(p.next != None):
				p = p.next
			p.next = node
		self.length = self.length + 1
	
	def get(self):
		temp = self.head
		
		if temp==None :
			return "Queue is Empty"
		else :
			self.head = self.head.next
	
		self.length = self.length - 1

		return temp.item

class Node:
	
	def __init__(self, item) :
		self.item = item
		self.next = None

def main():
	queue = Queue()
	while True:
		str_input = raw_input("Enter put item (Finish : no input) : ")

		if len(str_input)<1:
			print "Finish input item"
			break
	
		queue.put(str_input)
		print str_input, "input"

	print "==================="
	print "Queue size : ", queue.size()
	print "=================="

	while True:
		if queue.empty():
			print "Queue is Empty"
			break

		get_item = queue.get()
		print get_item+ " get, Queue size : ", queue.size()

if __name__ == "__main__":
	main()
