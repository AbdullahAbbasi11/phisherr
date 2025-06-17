import socket

host = '0.tcp.ap.ngrok.io'  # ✅ Same as your ngrok TCP host
port = 14270                # ✅ Same port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print("[+] Connected to remote PC. Type CMD commands.\n")

while True:
    command = input("CMD> ")
    if command.lower() == "exit":
        s.send(b"exit")
        break
    s.send(command.encode())
    output = s.recv(4096).decode()
    print(output)
