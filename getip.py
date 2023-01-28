import comm
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'SYNOPSIS: {sys.argv[0]} <hostname of machine>')
        exit(1)

    ip = comm.get_ip()
    # port = 12000
    broadcast_addr = comm.get_broadcast_addr(ip)
    message = sys.argv[1]
    print("Sending message ...")
    server_addr = comm.send_discover_message((broadcast_addr, 13000), message)
    if len(server_addr) < 1:
        print("No Response. Make sure serever is running on the network.")
    else:
        print(f'BROADCAST RESPONSE: {server_addr[0]}')
