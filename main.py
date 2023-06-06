from prob_calculator import Hat
from prob_calculator import experiment

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                             expected_balls={"red": 2, "green": 1},
                             num_balls_drawn=5,
                             num_experiments=2000)
    print(probability, "%")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
