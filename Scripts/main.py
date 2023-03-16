import os
import pandas as pd

# this script take 1 hour time to complete the operation

def main():
    
    os.system("python Scripts\scrap_population_names.py") #this script take the information of one website and save as csv
    os.system("python Scripts\scrap_population_ubication.py") #this script take the information(cities) of first script and take the ubicaton and save as another csv
    os.system("python Scripts\join_dataframes.py") # this script join the csv
    os.system("python Scripts\graph.py") #this script do graph the ubication of the cities 
        
    return 0


if __name__ == "__main__":
    main()
    