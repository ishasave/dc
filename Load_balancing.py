n_servers = int(input("Enter no. of servers: "))
n_processes = int(input("Enter no. of processes: "))

def rrlb(n_servers,n_processes):
    lst = []
    for i in range(n_processes):
        lst.append((i%n_servers)+1)

    print()

    for i in range(n_servers):
        print("Server {} has {} processes".format(i+1,lst.count(i+1)))


while True:
    rrlb(n_servers, n_processes)
    choice = int(input("\n1.Add Server\n2.Remove Server\n3.Add Process\n4.Remove Process\n5.Exit\n\nEnter your choice: "))

    if choice == 1:
        n_servers += 1
    elif choice == 2:
        n_servers -= 1
    elif choice == 3:
        n_processes += 1
    elif choice == 4:
        n_processes -= 1
    else:
        break

"""
output- 
Enter no. of servers: 5
Enter no. of processes: 12

Server 1 has 3 processes
Server 2 has 3 processes
Server 3 has 2 processes
Server 4 has 2 processes
Server 5 has 2 processes

1.Add Server
2.Remove Server
3.Add Process
4.Remove Process
5.Exit

Enter your choice: 1

Server 1 has 2 processes
Server 2 has 2 processes
Server 3 has 2 processes
Server 4 has 2 processes
Server 5 has 2 processes
Server 6 has 2 processes

1.Add Server
2.Remove Server
3.Add Process
4.Remove Process
5.Exit

Enter your choice: 3

Server 1 has 3 processes
Server 2 has 2 processes
Server 3 has 2 processes
Server 4 has 2 processes
Server 5 has 2 processes
Server 6 has 2 processes

1.Add Server
2.Remove Server
3.Add Process
4.Remove Process
5.Exit

Enter your choice: 5
"""
