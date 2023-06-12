from prob_calculator import Hat
from prob_calculator import experiment

if __name__ == '__main__':
    # hat1 = Hat()
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                             expected_balls={"red": 2, "green": 1},
                             num_balls_drawn=5,
                             num_experiments=2000)
    print(probability, "%")
