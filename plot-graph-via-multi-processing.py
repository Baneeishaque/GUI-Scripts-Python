import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Process


do_animation = True


def visualize_path(grid_map, start, goal, path):  # pragma: no cover
    oy, ox = start
    gy, gx = goal
    px, py = np.transpose(np.flipud(np.fliplr(path)))
    if not do_animation:
        plt.imshow(grid_map, cmap='Greys')
        plt.plot(ox, oy, "-xy")
        plt.plot(px, py, "-r")
        plt.plot(gx, gy, "-pg")
        plt.show()
    else:
        for ipx, ipy in zip(px, py):
            plt.cla()
            # for stopping simulation with the esc key.
            plt.gcf().canvas.mpl_connect(
                'key_release_event',
                lambda event: [exit(0) if event.key == 'escape' else None])
            plt.imshow(grid_map, cmap='Greys')
            plt.plot(ox, oy, "-xb")
            plt.plot(px, py, "-r")
            plt.plot(gx, gy, "-pg")
            plt.plot(ipx, ipy, "or")
            plt.axis("equal")
            plt.grid(True)
            plt.pause(0.5)


def main():
    start = [0, 0]
    goal = [20, 20]
    path1 = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    path2 = [[7, 15], [8, 16], [9, 17], [10, 18], [11, 19], [12, 20]]
    grid = [[0.0 for i in range(20)] for j in range(20)]
    print(grid)
    print(path1)
    print(path2)
    Process(target=visualize_path(grid, start, goal, path1)).start()
    Process(target=visualize_path(grid, start, goal, path2)).start()


if __name__ == "__main__":
    main()
