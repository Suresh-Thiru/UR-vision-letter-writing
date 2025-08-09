import socket
import time
from time import sleep
from stroke import text_to_strokes

ROBOT_IP = "192.168.1.13"
ROBOT_PORT = 30002
GRIPPER_PORT = 63352

HOME_POSITION = [0.0, -0.48665, 0.4, 0, -3.14, 0]
Z_UP = 0.30
Z_DOWN = 0.29

def gripper_set_position(ip, pos):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as gripper_socket:
        gripper_socket.connect((ip, GRIPPER_PORT))
        command = f'SET SPE 255 POS {pos}\n'.encode('utf-8')
        gripper_socket.sendall(command)
        response = gripper_socket.recv(1024)
      
def send_move_l(pose, a=0.15, v=0.1):
    script = f"movel(p[{pose[0]:.8f},{pose[1]:.8f},{pose[2]:.8f},{pose[3]},{pose[4]},{pose[5]}], a={a}, v={v})\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ROBOT_IP, ROBOT_PORT))
        gripper_set_position(ROBOT_IP, pos=255)
        s.send(script.encode('utf-8'))
        s.send(f"sync()".encode('utf-8'))
        time.sleep(1.5)

def draw_stroke(p1, p2, origin):
    ox, oy = origin
    x1, y1 = p1[0] + ox, p1[1] + oy
    x2, y2 = p2[0] + ox, p2[1] + oy
    time.sleep(0.1)
    send_move_l([x1, y1, Z_UP, 0, -3.14, 0])
    time.sleep(0.6)
    # Pen down
    send_move_l([x1, y1, Z_DOWN, 0, -3.14, 0])
    time.sleep(0.1)
    # Draw line
    send_move_l([x2, y2, Z_DOWN, 0, -3.14, 0])
    time.sleep(0.1)
    # Pen up
    send_move_l([x2, y2, Z_UP, 0, -3.14, 0])
    time.sleep(0.1)

def main():
    try:
        with open("recognized_text.txt", "r") as f:
            word = f.read().strip().upper()
    except FileNotFoundError:
        print("recognized_text.txt not found.")
        return

    if not word:
        print("No text found.")
        return

    print("Writing:", word)
    strokes = text_to_strokes(word)
    print(f"{len(strokes)} strokes generated.")
    # Move to HOME
    print("Moving to HOME position...")
    send_move_l(HOME_POSITION)
    time.sleep(2)

    origin_x, origin_y = HOME_POSITION[0], HOME_POSITION[1]

    for i, (p1, p2) in enumerate(strokes):
        print(f"Stroke {i+1}: From {p1} to {p2}")
        draw_stroke(p1, p2, (origin_x, origin_y))
        time.sleep(0.2)

    print("Writing complete.")

if __name__ == "__main__":
    main()
