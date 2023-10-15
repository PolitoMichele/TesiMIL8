from mip import Model, xsum, minimize, BINARY
import time, math


def solve_bin_packing(input_filename):
    try:

        with open(input_filename, 'r') as file:
            lines = file.readlines()

        num_objects, total_capacity = map(int, lines[0].split())
        objects = []

        for line in lines[1:]:
            cost, weight = map(int, line.split())
            if weight <= 0:
                print(f"Invalid object weight: {weight}")
            elif cost <= 0:
                print(f"Invalid object cost: {cost}")
            else:
                objects.append((cost, weight))

        start_time = time.time()

        model = Model()

        s_max = max(obj[1] for obj in objects)
        num_bins = math.ceil(abs(sum(obj[1] for obj in objects) / (total_capacity - s_max +1)))

        num_bins = min(num_bins, num_objects)

        x = [[model.add_var(var_type=BINARY, name=f'x{i}{j}') for j in range(num_bins)] for i in range(num_objects)]

        model.objective = minimize(xsum(
            (j + 1) * objects[i][0] * x[i][j] for i in range(num_objects) for j in range(num_bins)))

        for i in range(len(objects)):
            model += xsum(x[i][j] for j in range(num_bins)) == 1

        for j in range(num_bins):
            model += xsum(objects[i][1] * x[i][j] for i in range(num_objects)) <= total_capacity

        model.write('model.lp')

        model.optimize(max_seconds=100)
        
        end_time = time.time()

        if model.num_solutions:
            print("Solution:")
            for j in range(num_bins):
                bin_weight = sum(objects[i][1] * x[i][j].x for i in range(num_objects))
                if bin_weight != 0.0:
                    print(f"Bin {j + 1}: Weight = {bin_weight}")

            print(f"Objective Value: {model.objective_value}")
            print(f"Solution Status: {model.status}")
            print(f"Computation Time: {end_time - start_time} seconds")
            print(f"Best Lower Bound: {model.objective_bound}")
        else:
            print("No solution found.")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

solve_bin_packing('input.txt')