# n = no. of nodes
n = int(input("\nEnter the no. of nodes: "))

faulty = int(input('Enter faulty node (out of {0} to {1}): '.format(1,n)))

start = int(input('\nEnter node that detected the failure first: '))

print('\nNode {0} detected failure of coordinator...'.format(start))
print('Node {0} initiates election process...'.format(start))
new_coordinator = -1

for node in range(start, n+1):
    if node == faulty:
        continue

    print()
    print('Node {0} sending ELECTION message...'.format(node))

    oks = 0

    for neighbor in range(node+1, n+1):
        if neighbor != faulty:
            oks += 1

        print('Message sent to Node{0}'.format(neighbor))

    # Checking if there is any active higher priority process
    if oks > 0:
        print('{0} (OKs) received by Node {1}'.format(oks,node))
    else:
        print('Active higher priority process does NOT exist..')
        new_coordinator = node

print()
print('----- RESULT OF ELECTION PROCESS ------\n')
print('Node {} elected as new coordinator'.format(new_coordinator))

print('Node {0} sending message to inform that it is elected as New Coordinator..\n'.format(new_coordinator))

for neighbor in range(1,new_coordinator):
    print('Message sent to Node {0}'.format(neighbor))

'''Enter the no. of nodes: 2
Enter faulty node (out of 1 to 2): 2

Enter node that detected the failure first: 2

Node 2 detected failure of coordinator...
Node 2 initiates election process...

----- RESULT OF ELECTION PROCESS ------

Node -1 elected as new coordinator
Node -1 sending message to inform that it is elected as New Coordinator..


Process finished with exit code 0
'''
