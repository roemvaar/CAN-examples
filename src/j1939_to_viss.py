import socket
import struct
import array
import kuksa_viss_client
import can
import cantools
import json


def process_can_message(msg):
    if msg.arbitration_id == 150892286:
        # vehicle_speed = int.from_bytes(msg.data, byteorder='big') # TODO: check byteorder, check the arbitration_id, these are arbitrary
        print(f"CAN ID: Electronic Engine Controller 1")
    elif msg.arbitration_id == 0x102:
        # Handle other CAN IDs and data decoding here
        pass
    else:
        print(f"Unknown CAN ID")


def main():
    print("CAN Sockets Demo - Receive")
    s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
    dbc = cantools.database.load_file('../j1939/CSS-Electronics-SAE-J1939-2020-03_v1.1.dbc')
    print("Load SAE-J1939 DBC file... done!")

    client = kuksa_viss_client.KuksaClientThread(config={})
    client.start()
    client.authorize("/usr/lib/python3.10/site-packages/kuksa_certificates/jwt/super-admin.json.token") #TODO: confirm if this is needed?
    print("Kuksa Client init... done!")

    v_temp = 65.0

    try:
        s.bind(('vcan0',))
    except OSError as e:
        print(f"Bind error: {e}")
        return 1
    
    print("-------------------------------------------------------------------")

    while True:
        try:
            frame = s.recv(16)  
        except OSError as e:
            print(f"Read error: {e}")
            return 1

        can_id, can_dlc, data = struct.unpack("<IB3x8s", frame)
        
        print(f"0x{can_id:03X} [{can_dlc}] ", end="")

        # Decode the received frame using python-can
        msg = can.Message(
            arbitration_id=can_id,
            data=data,
            dlc=can_dlc,
            is_extended_id=False  # Assuming standard CAN frames
        )


        # Call the message processing function
        process_can_message(msg)

        if can_id == 150892286:
            print("VehicleSpeed: {}".format(v_temp))
            client.setValue("Vehicle.Speed", str(v_temp))
            v_temp += 10

        print(f"Arbitration ID received: {msg.arbitration_id}")

        dictionary = dbc.decode_message(msg.arbitration_id, msg.data)
        for key, value in dictionary.items():
            print(f"{key}: {value}")

        print("-------------------------------------------------------------------")

    client.stop()


if __name__ == "__main__":
    main()
