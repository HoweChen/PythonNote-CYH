from random import choice
import matplotlib.pyplot as plt


class RandomWalk():

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_value = [0]

    @staticmethod
    def get_step():
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # choose which the way to go
            x_step = self.get_step()
            y_step = self.get_step()

            # do not allow stay on the same position
            if x_step and y_step == 0:
                continue

            # get the point of next move based on the last move
            x_next = self.x_values[-1] + x_step
            y_next = self.y_value[-1] + y_step

            # append to the list
            self.x_values.append(x_next)
            self.y_value.append(y_next)


rw = RandomWalk(50000)
rw.fill_walk()
point_numbers = list(range(rw.num_points))

# draw the map
plt.scatter(rw.x_values, rw.y_value, c=point_numbers,
            cmap=plt.cm.Blues, edgecolors='none', s=15)

# re-draw the start and termination
plt.scatter(rw.x_values[0], rw.y_value[0], c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)

# hide the cordinate axis
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
