class Node:
	def __init__(self,cargo=None,next=None):
		self.cargo=cargo
		self.movenext=next ##define the verb. 

	def __str__(self): 
		return str(self.cargo)


node1=Node(1)
node2=Node(2)
node3=Node(3)
node1.movenext=node2 ## create next move
node2.movenext=node3






##pass reference from first node 
##To traverse a linked list, it is common to use a loop variable like node to refer to each of the nodes in succession.
def print_list(node):  
	while node:
		print node,
		node=node.movenext
	print



def print_backward(i):
	if i == None: return
	head = i 
	tail = i.movenext
	print_backward(tail)
	print head, #comma keeps python printing new lines. 
	# what happens after last one is printed? 

#print_backward(node1) 

def removeSecond(list):
	if list == None: return
	first  = list
	second = list.movenext
	first.movenext = second.movenext
	second.movenext=None 
	return second

print_list(node1)
removeSecond(node1)
print_list(node1)



