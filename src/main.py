from src.constants import SIMULATION_RESULTS_PATH


if __name__ == '__main__':
    with open(f"{SIMULATION_RESULTS_PATH}simulation_output.txt", "w") as f:
        f.write("Hello World! from a simulation.")
        
