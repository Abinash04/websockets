# import asyncio
# import websockets

# async def hello():
#     uri = "ws://localhost:8765"
#     async with websockets.connect(uri) as websocket:
#         await websocket.send("Hello, WebSocket! Good Day")
#         response = await websocket.recv()
#         print(f"Received: {response}")

# asyncio.run(hello())

import asyncio
import websockets

async def send_and_receive():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            # Send a question to the server
            question = input("Client, what is your question?: ")
            await websocket.send(question)

            # Receive the server's response
            response = await websocket.recv()
            print(f"Received from server: {response}")

asyncio.run(send_and_receive())



