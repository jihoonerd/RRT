import argparse
import pathlib

import cv2


def pick_start_target_pos(event, x, y, flags, param):
    coordinates = param[0]
    image = param[1]
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(coordinates) == 0:
            cv2.circle(image, (x,y), 5, (0,0,255), 5)
        elif len(coordinates) == 2:
            cv2.circle(image, (x,y), 5, (255,0,0), 5)
        else:
            return None
        coordinates.append(x)
        coordinates.append(y)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--map', type=str, default='map.png', help='path to map file')
    parser.add_argument('--stepsize', type=int, default=5, help='step size')
    args = parser.parse_args()

    pathlib.Path('images').mkdir(parents=True, exist_ok=True)

    img_for_collision_ck = cv2.imread(args.map, cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread(args.map, cv2.IMREAD_COLOR)

    stepsize = args.stepsize

    coordinates=[]

    window_name = 'Path Planning'
    print("Select start and end points by double clicking, press 'escape' to exit")
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, pick_start_target_pos, param=[coordinates, img_color])
    print(coordinates)
    while True:
        cv2.imshow(window_name, img_color)
        cv2.putText(img_color, 'Choose start/target position', (200,100), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 2)
        if len(coordinates) == 4:
            cv2.waitKey(1000)
            break
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
    print(coordinates)

    start = (coordinates[0], coordinates[1])
    target = (coordinates[2], coordinates[3])
