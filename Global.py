# creating a class for nodes

class Node:
    def __init__(self):
        self.hours = 0
        self.mins = 0
        self.name = ""
        self.node_time_diff_list = []
        self.avg_time_diff = 0

agreed_time_hr = int(input("\nEnter the agreed time in hours: "))
agreed_time_mins = int(input("Enter the agreed time in minutes: "))

initial_time_hr = int(input("\nEnter the initial time in hours: "))
initial_time_mins = int(input("Enter the initial time in minutes: "))

# Calculating time difference between agreed and initial time minutes

time_diff = (agreed_time_hr - initial_time_hr) + (agreed_time_mins - initial_time_mins)

# Creating nodes containing hours and minutes

n = int(input("\nEnter the number of nodes to synchronize their clock time: "))

# Creating n instances of the Node class and set their local clock times
nodes_li = []
for i in range(1,n+1):
    node = Node()
    node.name = f"Node '{chr(64+i)}'"
    node.hours = int(input(f"\nEnter the local clock time in hrs for {node.name}: "))
    node.mins = int(input(f"Enter the local clock time in minutes for {node.name}: "))
    nodes_li.append(node)


time_elapsed = 5
time_diff_li = []

# Calculating time difference for each node

iterations =  int(time_diff / time_elapsed) + 1

for i in range(iterations):

    diff_li = []
    print(f"\nStep {i+1} current time:")

    for node in nodes_li:

        print(f"{node.name} = {node.hours}:{node.mins}")
        curr_diff = (node.hours - agreed_time_hr) + (node.mins - agreed_time_mins)
        diff_li.append(curr_diff)
        node.node_time_diff_list.append(curr_diff)

        # updating the local time of all nodes after the time has elapsed
        if i != iterations:
            node.mins += time_elapsed

    print(f"Skeww after step {i+1}: {diff_li}")
    print("")
    time_diff_li.append(diff_li)

ctr = 1
no_of_nodes = len(nodes_li)

avg_li = []

for n in nodes_li:

    sum_diff = 0
    for diff in n.node_time_diff_list:
        sum_diff += diff

    avg_li.append((sum_diff/no_of_nodes))
    n.avg_time_diff = sum_diff/no_of_nodes

print(f"Average List: {avg_li}")

# Calculating the common time difference

common_time_diff = []
second_li = []

for i in range(no_of_nodes):

    res = 0
    min_part = int(avg_li[i]/1)
    sec_part = avg_li[i] % 1
    second_li.append(sec_part)

    if(avg_li[i] < 0):
        res = nodes_li[i].mins + abs(min_part)
    else:
        res = nodes_li[i].mins - min_part

    common_time_diff.append(res)

results = []

for i in range(no_of_nodes):

    n = nodes_li[i]
    if n.avg_time_diff % 1 >= 0.5:
        results.append(str(n.hours) + ":" + str(common_time_diff[i]) + ":" + str(30))
    else:
        results.append(str(n.hours) + ":" + str(common_time_diff[i]))

print(f"\nResults: {results}\n")


'''

Enter the agreed time in hours: 2
Enter the agreed time in minutes: 120

Enter the initial time in hours: 1
Enter the initial time in minutes: 40

Enter the number of nodes to synchronize their clock time: 3

Enter the local clock time in hrs for Node 'A': 1
Enter the local clock time in minutes for Node 'A': 50

Enter the local clock time in hrs for Node 'B': 1
Enter the local clock time in minutes for Node 'B': 20

Enter the local clock time in hrs for Node 'C': 1
Enter the local clock time in minutes for Node 'C': 30

Step 1 current time:
Node 'A' = 1:50
Node 'B' = 1:20
Node 'C' = 1:30
Skeww after step 1: [-71, -101, -91]


Step 2 current time:
Node 'A' = 1:55
Node 'B' = 1:25
Node 'C' = 1:35
Skeww after step 2: [-66, -96, -86]


Step 3 current time:
Node 'A' = 1:60
Node 'B' = 1:30
Node 'C' = 1:40
Skeww after step 3: [-61, -91, -81]


Step 4 current time:
Node 'A' = 1:65
Node 'B' = 1:35
Node 'C' = 1:45
Skeww after step 4: [-56, -86, -76]


Step 5 current time:
Node 'A' = 1:70
Node 'B' = 1:40
Node 'C' = 1:50
Skeww after step 5: [-51, -81, -71]


Step 6 current time:
Node 'A' = 1:75
Node 'B' = 1:45
Node 'C' = 1:55
Skeww after step 6: [-46, -76, -66]


Step 7 current time:
Node 'A' = 1:80
Node 'B' = 1:50
Node 'C' = 1:60
Skeww after step 7: [-41, -71, -61]


Step 8 current time:
Node 'A' = 1:85
Node 'B' = 1:55
Node 'C' = 1:65
Skeww after step 8: [-36, -66, -56]


Step 9 current time:
Node 'A' = 1:90
Node 'B' = 1:60
Node 'C' = 1:70
Skeww after step 9: [-31, -61, -51]


Step 10 current time:
Node 'A' = 1:95
Node 'B' = 1:65
Node 'C' = 1:75
Skeww after step 10: [-26, -56, -46]


Step 11 current time:
Node 'A' = 1:100
Node 'B' = 1:70
Node 'C' = 1:80
Skeww after step 11: [-21, -51, -41]


Step 12 current time:
Node 'A' = 1:105
Node 'B' = 1:75
Node 'C' = 1:85
Skeww after step 12: [-16, -46, -36]


Step 13 current time:
Node 'A' = 1:110
Node 'B' = 1:80
Node 'C' = 1:90
Skeww after step 13: [-11, -41, -31]


Step 14 current time:
Node 'A' = 1:115
Node 'B' = 1:85
Node 'C' = 1:95
Skeww after step 14: [-6, -36, -26]


Step 15 current time:
Node 'A' = 1:120
Node 'B' = 1:90
Node 'C' = 1:100
Skeww after step 15: [-1, -31, -21]


Step 16 current time:
Node 'A' = 1:125
Node 'B' = 1:95
Node 'C' = 1:105
Skeww after step 16: [4, -26, -16]


Step 17 current time:
Node 'A' = 1:130
Node 'B' = 1:100
Node 'C' = 1:110
Skeww after step 17: [9, -21, -11]

Average List: [-175.66666666666666, -345.6666666666667, -289.0]

Results: ['1:310', '1:450', '1:404']


'''