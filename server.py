# import asyncio
# import websockets

# async def echo(websocket, path):
#     async for message in websocket:
#         await websocket.send(message)

# async def main():
#     async with websockets.serve(echo, "localhost", 8765):
#         await asyncio.Future()  # run forever

# asyncio.run(main())


# 
import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        while True:
            # Receive a message from the client
            message = await websocket.recv()
            print(f"Received from client: {message}")

            # Respond to the client's message
            response = input("Server, what is your response?: ")
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        print("Server started")
        await asyncio.Future()  # Run forever

asyncio.run(main())

