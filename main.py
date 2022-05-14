from cv2 import mean
import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df=pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean= statistics.mean(data)

print(population_mean)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean= statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()


def setup():
    mean_list=[]
    for i in range(0, 100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("sampling mean:- ", statistics.mean(mean_list))

setup()

#50,000----- mean_entire

#1 dataset d1-  random 30 rows
#                mean d1
#2. dataset d2 - random 30 rows
#                mean d2
#.........................100 times...................
#Pick of 30 samples for 100 times
#it will give us 100 means

#mean of these 100 means----- mean_sampling

# mean_entire= mean_sampling