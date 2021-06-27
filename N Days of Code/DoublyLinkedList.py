# Inserting a new node before the head. Beginning
# Inserting a new node after the tail (at the end of the list).
# Inserting a new node at the middle of the list.

# Deleting the first node
# Deleting the last node
# Deleting an intermediate node


class ListNode:
    def __init__(self, data):
        self.data = data       
        # store reference (next item)
        self.next = None
        # store reference (previous item)
        self.previous = None
        return

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next       
        return count

    def unordered_search (self, value):
        "search the linked list for the node that has this value"
        # define current_node
        current_node = self.head
        # define position
        node_id = 1
        # define list of results
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        
        return results
    def add_list_item(self, item):
        "add an item at the end of the list"
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
        
        return
    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item id"
        
        current_id = 1
        current_node = self.head
        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                # we don't have to look any further
                return
 
            # needed for the next iteration
            current_node = next_node
            current_id = current_id + 1
                
        return


node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")
node4 = ListNode(15)
track = DoubleLinkedList()
print("track length: %i" % track.list_length())
for current_node in [node1, node2, node3, node4]:
    track.add_list_item(current_node)
    print("track length: %i" % track.list_length())
    track.output_list()
results = track.unordered_search(15)
print(results)
track.remove_list_item_by_id(4)
track.output_list() 
     