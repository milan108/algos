from queue import *

colors = Queue()
colors.enqueue("Pthalo Blue")
colors.enqueue("Alizarin")
colors.enqueue("Magenta")
colors.dump("Three items")
colors.dequeue()
colors.dump("Two items")
colors.dequeue()
colors.dump("One item")
colors.dequeue()
colors.dump("No items")
