import socket, sys

if len(sys.argv) < 2 or sys.argv[1] == "-h":
    print(f"""
     __   __       
    |__) /__` \\  / 
    |  \\ .__/  \\/  by mdsm 
    """)

    print(f"How to use: {sys.argv[0]} site.com")
    print("Options:\n -h, Shows how to use the tool and available options\n -f, Enables the resolution of multiple hosts through a file\n --silent, Returns a clean data output")
    sys.exit(1)

try:
    if len(sys.argv) >= 3 and sys.argv[1] == "-f":
        file = sys.argv[2]
        try:
            with open(file, 'r') as hosts:
                host = hosts.readline().strip()
                while host:
                    try:
                        if '--silent' in sys.argv:
                            resolv = socket.gethostbyname(host)
                            print(resolv)
                        else:        
                            resolv = socket.gethostbyname(host)
                            print(f"The host {host} resolution is {resolv}")
                    except socket.gaierror:
                        print(f"Failed to resolve the host: {host}")

                    host = hosts.readline().strip()
        except FileNotFoundError:
            print(f"Error: The file '{file}' was not found.")
            sys.exit(1)
        except PermissionError:
            print(f"Error: Permission denied to access the file '{file}'.")
            sys.exit(1)

    else:
        host = sys.argv[1]
        try:
            if '--silent' in sys.argv:
                resolv = socket.gethostbyname(host)
                print(resolv)
            else:
                resolv = socket.gethostbyname(host)
                print(f"The host {host} resolution is {resolv}")
        
        except socket.gaierror:
            print(f"Failed to resolve the host: {host}")
            sys.exit(1)

except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)

if '--silent' in sys.argv:
            resolv = socket.gethostbyname(host)
            print(resolv)