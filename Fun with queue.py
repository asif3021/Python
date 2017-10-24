from collections import deque
queue=deque(["Asif","Ahmed","Habib","Shishir"])
queue.append("Sweet")
queue.append("Pilot")
for n in queue:
	if n==queue[len(queue)-1]:
		print(n,end=".")
		break
	else:
		print(n,end=", ")
