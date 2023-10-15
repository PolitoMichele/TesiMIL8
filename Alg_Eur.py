import math, time


# Function to read input from a file and return a list of objects
def read_input(filename):
    objects = []
    with open(filename, 'r') as file:
        n, c = map(int, file.readline().split())
        for line in file:
            w, s = map(int, line.split())
            objects.append((w, s))
    return n, c, objects


# Function to order objects by decreasing price
def order_objects_by_price(objects):
    return sorted(objects, key=lambda x: -x[0])


# Function to pack objects into bins
def pack_objects_into_bins(objects, total_capacity):
    num_bins = math.ceil(abs(sum(obj[1] for obj in objects) / (total_capacity - max(obj[1] for obj in objects) + 1)))

    num_bins = min(num_bins, len(objects))

    bins = [[] for _ in range(num_bins)]
    total_weight = [0] * num_bins

    for obj in objects:
        w, s = obj
        best_bin = None

        for i, bin_contents in enumerate(bins):
            if total_weight[i] + w <= total_capacity:
                best_bin = i
                break

        if best_bin is not None:
            bins[best_bin].append((w, s))
            total_weight[best_bin] += w

    return bins, total_weight


# Function to calculate the objective function value
def calculate_objective_function(bins):
    objective_value = 0
    for i, bin_contents in enumerate(bins):
        for w, s in bin_contents:
            objective_value += (i + 1) * w
    return objective_value


# Main function
def main():
    filename = 'input.txt'  # Change this to the name of your input file
    n, c, objects = read_input(filename)

    # Start timing
    start_time = time.time()

    # Order objects by decreasing price
    ordered_objects = order_objects_by_price(objects)

    # Pack objects into bins
    bins, total_weight = pack_objects_into_bins(ordered_objects, c)

    # End timing
    end_time = time.time()

    # Print the bins and total weight
    print("Bins and Total Weight:")
    for i, bin_contents in enumerate(bins):
        print(f"Bin {i + 1}: Total Weight = {total_weight[i]}, Objects = {[item[0] for item in bin_contents]}")

    # Calculate and print the objective function value
    objective_value = calculate_objective_function(bins)
    print(f"Objective Function Value: {objective_value}")

    # Print the execution time
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time:.6f} seconds")


if __name__ == "__main__":
    main()
