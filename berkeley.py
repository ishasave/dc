import datetime

n = int(input('Enter the number of nodes in n/w : '))
current_time = []

for i in range(n):
    time = input(f"Enter time in hh:mm format of node {i} in n/w : ")
    time = datetime.datetime.strptime(time, "%H:%M")  # convert string time to datetime object
    current_time.append((i, time))

agreed_time = input("Enter agreed upon time for resync in hh:mm format : ")
agreed_time = datetime.datetime.strptime(agreed_time, "%H:%M")
current_time = sorted(current_time, key=lambda node_time: node_time[1],
                      reverse=True)  # sort nodes in descending order of time

def print_time(current_time):
    for i in range(len(current_time)):
        print(f'Node {current_time[i][0]} = {current_time[i][1].time()}')

def print_skews(current_skews):
    for i in range(len(current_skews)):
        print(f'Node {current_skews[i][0]} = {current_skews[i][1]} seconds')

def adjust_time(current_time, skews):
    print('Skews :-')
    for node, skew in skews.items():
        print(f'Node {node} : {skew}')

    avg_skews = {node: sum(skew)/len(skew) for node, skew in skews.items()}
    print()
    print('Average Skews Computed :-')
    for node, avg in avg_skews.items():
        print(f'Node {node} : {avg} ', end='')
        status = 'ahead' if avg >= 0 else 'behind'
        print(f'(Node {node} is {abs(avg)} seconds {status})')
        print()

    print('Final Adjusted Time : ')
    current_time = [(node_time[0], node_time[1] - datetime.timedelta(seconds=avg_skews[node_time[0]]))
                       for node_time in current_time]
    print_time(current_time)

def DGA(current_time):
    skews = dict()
    for j in range(len(current_time)):
        skews[j] = []

    for i in range(len(current_time)):
        current_sender = current_time[i][0]
        time_to_resync = agreed_time - current_time[i][1]
        current_time = [(node_time[0], time_to_resync + node_time[1]) for node_time in current_time]
        print()

        print(f'--- After {time_to_resync} ---')
        current_skews = [(node_time[0], int((node_time[1] - agreed_time).total_seconds()))
                         for node_time in current_time]

        print('Current Time :-')
        print_time(current_time)

        print('Current Skews :-')
        print_skews(current_skews)

        print('Current Sender who broadcast resync : ', 'Node', current_sender)
        for node, skew in current_skews:
            skews[node].append(skew)

    print()
    adjust_time(current_time, skews)

print()
print('--- Initial Time ---')
print_time(current_time)
print(f'Agreed upon time for resync = {agreed_time.time()}')
DGA(current_time)

"""
Enter the number of nodes in n/w : 5
Enter time in hh:mm format of node 0 in n/w : 02:50
Enter time in hh:mm format of node 1 in n/w : 03:20
Enter time in hh:mm format of node 2 in n/w : 02:00
Enter time in hh:mm format of node 3 in n/w : 5:00
Enter time in hh:mm format of node 4 in n/w : 04:56
Enter agreed upon time for resync in hh:mm format : 04:00

--- Initial Time ---
Node 3 = 05:00:00
Node 4 = 04:56:00
Node 1 = 03:20:00
Node 0 = 02:50:00
Node 2 = 02:00:00
Agreed upon time for resync = 04:00:00

--- After -1 day, 23:00:00 ---
Current Time :-
Node 3 = 04:00:00
Node 4 = 03:56:00
Node 1 = 02:20:00
Node 0 = 01:50:00
Node 2 = 01:00:00
Current Skews :-
Node 3 = 0 seconds
Node 4 = -240 seconds
Node 1 = -6000 seconds
Node 0 = -7800 seconds
Node 2 = -10800 seconds
Current Sender who broadcast resync :  Node 3

--- After 0:04:00 ---
Current Time :-
Node 3 = 04:04:00
Node 4 = 04:00:00
Node 1 = 02:24:00
Node 0 = 01:54:00
Node 2 = 01:04:00
Current Skews :-
Node 3 = 240 seconds
Node 4 = 0 seconds
Node 1 = -5760 seconds
Node 0 = -7560 seconds
Node 2 = -10560 seconds
Current Sender who broadcast resync :  Node 4

--- After 1:36:00 ---
Current Time :-
Node 3 = 05:40:00
Node 4 = 05:36:00
Node 1 = 04:00:00
Node 0 = 03:30:00
Node 2 = 02:40:00
Current Skews :-
Node 3 = 6000 seconds
Node 4 = 5760 seconds
Node 1 = 0 seconds
Node 0 = -1800 seconds
Node 2 = -4800 seconds
Current Sender who broadcast resync :  Node 1

--- After 0:30:00 ---
Current Time :-
Node 3 = 06:10:00
Node 4 = 06:06:00
Node 1 = 04:30:00
Node 0 = 04:00:00
Node 2 = 03:10:00
Current Skews :-
Node 3 = 7800 seconds
Node 4 = 7560 seconds
Node 1 = 1800 seconds
Node 0 = 0 seconds
Node 2 = -3000 seconds
Current Sender who broadcast resync :  Node 0

--- After 0:50:00 ---
Current Time :-
Node 3 = 07:00:00
Node 4 = 06:56:00
Node 1 = 05:20:00
Node 0 = 04:50:00
Node 2 = 04:00:00
Current Skews :-
Node 3 = 10800 seconds
Node 4 = 10560 seconds
Node 1 = 4800 seconds
Node 0 = 3000 seconds
Node 2 = 0 seconds
Current Sender who broadcast resync :  Node 2

Skews :-
Node 0 : [-7800, -7560, -1800, 0, 3000]
Node 1 : [-6000, -5760, 0, 1800, 4800]
Node 2 : [-10800, -10560, -4800, -3000, 0]
Node 3 : [0, 240, 6000, 7800, 10800]
Node 4 : [-240, 0, 5760, 7560, 10560]

Average Skews Computed :-
Node 0 : -2832.0 (Node 0 is 2832.0 seconds behind)

Node 1 : -1032.0 (Node 1 is 1032.0 seconds behind)

Node 2 : -5832.0 (Node 2 is 5832.0 seconds behind)

Node 3 : 4968.0 (Node 3 is 4968.0 seconds ahead)

Node 4 : 4728.0 (Node 4 is 4728.0 seconds ahead)

Final Adjusted Time : 
Node 3 = 05:37:12
Node 4 = 05:37:12
Node 1 = 05:37:12
Node 0 = 05:37:12
Node 2 = 05:37:12

"""