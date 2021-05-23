import os
from collections import namedtuple

import imageio
import numpy as np

Node = namedtuple('Node', ['x', 'y', 'parent_node'])


def find_nearest_node(nodes, new_node):

    dist_list = []
    for node in nodes:
        vector = np.array([new_node.x - node.x, new_node.y - node.y])
        dist_list.append(np.linalg.norm(vector))
    min_dist_idx = dist_list.index(np.min(dist_list))
    return nodes[min_dist_idx]

def get_step_point(nearest_node, new_node, stepsize):
    vec_displ = np.array([new_node.x - nearest_node.x, new_node.y - nearest_node.y])
    unit_vec = vec_displ / np.linalg.norm(vec_displ)
    step_sized_vec = unit_vec * stepsize

    x_path_end = nearest_node.x + step_sized_vec[0]
    y_path_end = nearest_node.y + step_sized_vec[1]
    return Node(x_path_end, y_path_end, nearest_node)

def check_collision(collision_ck_map, nearest_node, one_step_target):

    x_path = np.linspace(nearest_node.x, one_step_target.x, 100)
    y_path = np.linspace(nearest_node.y, one_step_target.y, 100)

    height, width = collision_ck_map.shape
    
    # Out of bound
    if one_step_target.x >= width or one_step_target.y >= height:
        return True

    for coord in zip(x_path, y_path):
        x_coord, y_coord = int(coord[0]), int(coord[1])
        if collision_ck_map[y_coord, x_coord] == 0:
            return True
    return False

def check_arrival(one_step_target, target_node):
    vec_displ = np.array([target_node.x - one_step_target.x, target_node.y - one_step_target.y])
    distance = np.linalg.norm(vec_displ)
    if distance <= 25:
        return True
    return False


def make_gif(image_dir='images'):
    images = []
    for file_name in sorted(os.listdir(image_dir)):
        if file_name.endswith('.jpg'):
            file_path = os.path.join(image_dir, file_name)
            images.append(imageio.imread(file_path))
    imageio.mimsave('figure.gif', images, duration=0.05)
