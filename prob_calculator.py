import random

class Hat:

    def __init__(self, **kwargs):
        self.balls_in_the_hat = {}
        self.content: list[str] = []
        if kwargs.__len__() >= 1:
            self.balls_in_the_hat = kwargs
            for key, value in kwargs.items():
                for it in range(0, value):
                    self.content.append(key)
                    pass
                pass
            pass
        else:
            print("The hat most have at least one ball.\n"
                  "Nothing to do.")
            pass
        pass

    def draw(self, num_balls_to_draw: int) -> list[str]:
        drawing: list[str] = list()
        if num_balls_to_draw > len(self.content):
            drawing = self.content
            self.content.clear()
            self.balls_in_the_hat.clear()
            pass
        else:
            for to_draw in range(0, num_balls_to_draw):
                drawing.append(self.content.pop(random.randint(0, len(self.content) - 1)))
                pass
            for it in range(0, len(self.content)):
                self.balls_in_the_hat[self.content[it]] = self.balls_in_the_hat[self.content[it]] - 1
                pass
        return drawing

    def simulate_draw(self, num_balls_to_draw: int) -> list[str]:
        simulate_drawing: list[str] = list()
        if num_balls_to_draw > len(self.content):
            simulate_drawing = self.content
            self.content.clear()
            self.balls_in_the_hat.clear()
            pass
        else:
            for to_draw in range(0, num_balls_to_draw):
                simulate_drawing.append(self.content[random.randint(0, len(self.content) - 1)])
                pass
            for it in range(0, len(self.content)):
                self.balls_in_the_hat[self.content[it]] = self.balls_in_the_hat[self.content[it]] - 1
                pass
        return simulate_drawing
    pass


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> int:
    """
Determining the probability by experimentation.
For example, if you want to determine the probability of getting at least two red balls and one green ball
when you draw five balls from a hat containing six black, four red, and three green. To do this, you will
perform N experiments, count how many times M you get at least two red balls and one green ball, and estimate
the probability as M/N. Each experiment consists of starting with a hat containing the specified balls,
drawing several balls, and checking if you got the balls you were attempting to draw.
    :param hat: A hat object containing balls that should be copied inside the function.
    :param expected_balls: A dictionary indicating the probability we are looking for.
                           For example, to determine the probability of drawing 2 blue balls
                           and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
    :param num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    :param num_experiments: The number of experiments to perform. (The more experiments performed,
                            the more accurate the approximate probability will be.)
    :return: the probability
    """
    drawed: list[str] = []
    M = key_counter = 0
    key_ok = False
    for it_exp in range(0, num_experiments):
        drawed = hat.simulate_draw(num_balls_drawn)
        for key, value in expected_balls.items():
            key_counter = 0
            for it in range(0, len(drawed)):
                if drawed[it] == key:
                    key_counter += 1
                    pass
                pass
            if key_counter >= value:
                key_ok = True
                pass
            else:
                key_ok = False
                continue
                pass
            pass
        if key_ok:
            M += 1
    return M * 100 / num_experiments
    pass
