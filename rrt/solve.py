import cv2
import numpy as np
from rrt.utils import find_nearest_node, check_collision, get_step_point, check_arrival, make_gif, Node

def rrt_solver(map, start, target, stepsize):
    collision_ck_map = cv2.imread(map, cv2.IMREAD_GRAYSCALE)
    world_map = cv2.imread(map, cv2.IMREAD_COLOR)

    height, width = collision_ck_map.shape
    
    nodes = []
    start_node = Node(start[0], start[1], None)
    target_node = Node(target[0], target[1], None)
    nodes.append(start_node)

    cv2.circle(world_map, (start_node.x, start_node.y), 5, (0,0,255), 25)
    cv2.circle(world_map, (target_node.x, target_node.y), 5, (255,0,0), 25)

    done = False
    i = 0
    while not done:
        new_x, new_y = np.random.randint(0, width), np.random.randint(0, height)
        new_node = Node(new_x, new_y, None)
        nearest_node = find_nearest_node(nodes, new_node)
        one_step_target = get_step_point(nearest_node, new_node, stepsize)
        is_collision = check_collision(collision_ck_map, nearest_node, one_step_target)

        if is_collision:
            continue
        nodes.append(Node(one_step_target.x, one_step_target.y, nearest_node))
        cv2.circle(world_map, (int(one_step_target.x),int(one_step_target.y)), 2,(42,42,165),thickness=3, lineType=8)
        cv2.line(world_map, (int(one_step_target.x),int(one_step_target.y)), (int(nearest_node.x),int(nearest_node.y)), (0,255,0), thickness=1, lineType=8)
        cv2.imshow("Path Finder", world_map)
        cv2.imwrite(f"images/{i:05d}.jpg", world_map)
        cv2.waitKey(1)

        is_arrived = check_arrival(one_step_target, target_node)
        i += 1
        if is_arrived:
            cur_node = one_step_target
            parent_node = one_step_target.parent_node
            while parent_node.parent_node is not None:
                cv2.line(
                    world_map,
                    (int(cur_node.x), int(cur_node.y)),
                    (int(parent_node.x), int(parent_node.y)), (0,0,255), 3, 8
                )
                cur_node = parent_node
                parent_node = parent_node.parent_node

            cv2.imshow("Path Finder", world_map)
            cv2.imwrite(f"images/{i:05d}.jpg", world_map)
            cv2.imwrite("path_plot.jpg", world_map)
            cv2.waitKey(2000)
            break
