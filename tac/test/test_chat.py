import time

import socketio
from settings.conf import ServerConf

CLIENT_COUNT = 50
TEST_MESSAGES = [
    {'text': "Hello, call"},
    {'text': "Test Call"},
    {'text': "Final, call"}
]

clients = []

print("================ Load Test =======================")
print("Client count : ", CLIENT_COUNT)
print("\n")

print("\n")
print("================ Test : Connection Establishment ================")
print("Creating Virtual clients")

virtual_client = 0
for i in range(CLIENT_COUNT):
    client = socketio.Client()
    client.connect(ServerConf.test_url, headers={"user_name": "w1" })
    clients.append(client)
    if client.connected:
        virtual_client += 1
    print("Spawned client id : ", client.sid)


print("\n")
print("================ Test : Sending Messages to server================")
print("Sending Messages to server")
clients_status = []
for msg in TEST_MESSAGES:
    active_connection = 0
    for client in clients:
        try:
            client.emit('message', msg)
            if client.connected:
                active_connection += 1
                print("Virtual client {} sent {}".format(client.sid, str(msg)))
        except Exception as err:
            print(err)
        time.sleep(.02)
    clients_status.append(active_connection)

print("\n")
print("================ Killing Virtual clients ================")
killed_clients = 0
for client in clients:
    print(client.connected)
    client.disconnect()
    if client.sid is None:
        killed_clients += 1
    print("Destroyed virtual client : ", client.sid)

print("\n")
print("================ Result ================")
if len(set(clients_status)) == 1 or clients_status[0] == CLIENT_COUNT and \
        killed_clients == CLIENT_COUNT and virtual_client == CLIENT_COUNT:
    print(":::::::::::: Load Test Success ::::::::::::")
else:
    print(":::::::::::: Load Test Failed ::::::::::::")

print("Required client count : ", CLIENT_COUNT)
print("Spawned client count : ", virtual_client)
print("Active clients for each msg : ", clients_status)
print("Destroyed client count : ", killed_clients)