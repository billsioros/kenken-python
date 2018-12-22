
import csv

if __name__ == "__main__":
    """
    Parse the csv resulting from a call to kenken.gather
    and print the algorithms sorted by various criteria in markdown format
    """
    path = input("filepath: ")

    with open(path, "r") as csvfile:
        data = list(csvfile)

    metrics = {}
    for values in data[1:]:
        values = values.replace('\n', '').replace(' ', '').split(',')

        element = (values[0], int(values[1]))

        metrics[element] = tuple([values[2]] + list(map(float, values[3:])))

    priorities = {
        "constraint check count": lambda value: value[1][0],
        "assignment count": lambda value: value[1][1],
        "completion time": lambda value: value[1][2]
    }

    colored = lambda word: "<span style=\"color: #f45c42\">" + word + "</span>"

    for size in range(3, 10):
        print("### **Kenken puzzles of size", size, ":**")
        entries = [entry for entry in metrics.items() if entry[0][1] == size]

        for name, priority in priorities.items():

            algorithms = [algorithm for (algorithm, _), _ in sorted(entries, key=priority)]
            
            print("The algorithms sorted by", colored(name), "are", algorithms)
    
            print()