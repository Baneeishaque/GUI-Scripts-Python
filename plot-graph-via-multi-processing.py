import matplotlib.pyplot as matplotlib_plot
import numpy
import multiprocessing.pool as multi_processing_pool


do_animation = True


def visualize_path(grid_map, start, goal, path):  # pragma: no cover
    oy, ox = start
    gy, gx = goal
    px, py = numpy.transpose(numpy.flipud(numpy.fliplr(path)))
    if not do_animation:
        matplotlib_plot.imshow(grid_map, cmap='Greys')
        matplotlib_plot.plot(ox, oy, "-xy")
        matplotlib_plot.plot(px, py, "-r")
        matplotlib_plot.plot(gx, gy, "-pg")
        matplotlib_plot.show()
    else:
        for ipx, ipy in zip(px, py):
            matplotlib_plot.cla()
            # for stopping simulation with the esc key.
            matplotlib_plot.gcf().canvas.mpl_connect(
                'key_release_event',
                lambda event: [exit(0) if event.key == 'escape' else None])
            matplotlib_plot.imshow(grid_map, cmap='Greys')
            matplotlib_plot.plot(ox, oy, "-xb")
            matplotlib_plot.plot(px, py, "-r")
            matplotlib_plot.plot(gx, gy, "-pg")
            matplotlib_plot.plot(ipx, ipy, "or")
            matplotlib_plot.axis("equal")
            matplotlib_plot.grid(True)
            matplotlib_plot.pause(0.5)


def main():
    start = [0, 0]
    goal = [20, 20]
    paths = [[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [
        [7, 15], [8, 16], [9, 17], [10, 18], [11, 19], [12, 20]]]
    grid = [[0.0 for i in range(20)] for j in range(20)]
    print(grid)
    print(paths[0])
    print(paths[1])
    local_multi_processing_pool = multi_processing_pool.Pool()
    [local_multi_processing_pool.apply(func=visualize_path, args=(
        grid, start, goal, path)) for path in paths]
    local_multi_processing_pool.close()


if __name__ == "__main__":
    main()
