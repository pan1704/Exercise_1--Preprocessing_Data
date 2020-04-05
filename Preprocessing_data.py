import pandas as pd
import numpy as np


class ProcessingData:
    """
    :type input_data: pandas dataframe
    """
    def __init__(self, input_data):
        self.input_data = input_data

    def summary(self):
        pass

    def replace(self):
        pass

    def discretize(self):
        pass

    def normalize(self):
        pass


if __name__ == '__main__':
    data = input("Input your data here: ")
    while True:
        try:
            input_data = pd.read_csv(data)
            break
        except:
            print("There is no file name.")
            data = input("Try again! Input your data here: ")
    

