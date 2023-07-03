import tensorcircuit as tc
import numpy as np
from typing import List, Tuple
from tensorcircuit.cons import backend
import matplotlib.pyplot as plt

## created by refraction-ray
def print_output(c: tc.Circuit) -> None:
    n = c._nqubits
    N = 2**n
    # Calculate the total number of states based on the number of qubits

    x_label = r"$\left|{0:0" + str(n) + r"b}\right>$"
    labels = [x_label.format(i) for i in range(N)]
    # Generate labels for the x-axis representing the binary states

    plt.bar(range(N), c.probability())
    # Create a bar plot with the probabilities of each state

    plt.xticks(range(N), labels, rotation=70)
    # Set the x-axis ticks to the generated labels and rotate them for better visibility

def print_result_prob(c: tc.Circuit, wrap: bool = False, reverse: bool = False) -> None:
    """
    Print the results and probabilities of a given quantum circuit.
    The default order is from the highest probability to the lowest one

    :param c: The quantum circuit to print the results and probabilities.
    :param wrap (optional): A flag indicating whether to wrap the output. Default is False.
    :param reverse (optional): A flag indicating whether to reverse the order of the output. Default is False.
    """
    """try:
        K
    except NameError:
        print("select a backend and assign it to K.")"""

    states = []
    n_qubits = c._nqubits
    for i in range(2**n_qubits):
        a = f"{bin(i)[2:]:0>{n_qubits}}"
        states.append(a)
        # Generate all possible binary states for the given number of qubits

    probs = backend.numpy(c.probability()).round(decimals=4)
    # Calculate the probabilities of each state using the circuit's probability method

    sorted_indices = np.argsort(probs)[::-1]
    if reverse == True:
        sorted_indices = sorted_indices[::-1]
    state_sorted = np.array(states)[sorted_indices]
    prob_sorted = np.array(probs)[sorted_indices]
    # Sort the states and probabilities in descending order based on the probabilities

    print("\n-------------------------------------")
    print("    selection\t  |\tprobability")
    print("-------------------------------------")
    if wrap == False:
        for i in range(len(states)):
            print("%10s\t  |\t  %.4f" % (state_sorted[i], prob_sorted[i]))
            # Print the sorted states and their corresponding probabilities
    elif wrap == True:
        for i in range(4):
            print("%10s\t  |\t  %.4f" % (state_sorted[i], prob_sorted[i]))
        print("               ... ...")
        for i in range(-4, -1):
            print("%10s\t  |\t  %.4f" % (state_sorted[i], prob_sorted[i]))
    print("-------------------------------------")

def print_result_cost(
    c: tc.Circuit, Q: List[list], wrap: bool = False, reverse: bool = False
) -> None:
    """
    Print the results and costs of a given quantum circuit.
    Specificly designed for the variational circuit.
    The default order is from the highest probability to the lowest one.

    :param c: The quantum circuit to print the results and probabilities.
    :param Q: The n-by-n square and symmetric Q-matrix representing the QUBO problem.
    :param wrap (optional): A flag indicating whether to wrap the output. Default is False.
    :param reverse (optional): A flag indicating whether to reverse the order of the output. Default is False.
    """
    cost_dict = {}
    states = []
    n_qubits = c._nqubits
    for i in range(2**n_qubits):
        a = f"{bin(i)[2:]:0>{n_qubits}}"
        states.append(a)
        # Generate all possible binary states for the given number of qubits
    for selection in states:
        x = np.array([int(bit) for bit in selection])
        cost_dict[selection] = np.dot(x, np.dot(Q, x))
    cost_sorted = dict(sorted(cost_dict.items(), key=lambda item: item[1]))
    if reverse == True:
        cost_sorted = dict(
            sorted(cost_dict.items(), key=lambda item: item[1], reverse=True)
        )
    num = 0
    print("\n-------------------------------------")
    print("    selection\t  |\t  cost")
    print("-------------------------------------")
    for k, v in cost_sorted.items():
        print("%10s\t  |\t%.4f" % (k, v))
        num += 1
        if (num >= 8) & (wrap == True):
            break
    print("-------------------------------------")

def print_Q_cost(Q: List[list], wrap: bool = False, reverse: bool = False) -> None:
    n_stocks = len(Q)
    states = []
    for i in range(2**n_stocks):
        a = f"{bin(i)[2:]:0>{n_stocks}}"
        n_ones = 0
        for j in a:
            if j == "1":
                n_ones += 1
        states.append(a)

    cost_dict = {}
    for selection in states:
        x = np.array([int(bit) for bit in selection])
        cost_dict[selection] = np.dot(x, np.dot(Q, x))
    cost_sorted = dict(sorted(cost_dict.items(), key=lambda item: item[1]))
    if reverse == True:
        cost_sorted = dict(
            sorted(cost_dict.items(), key=lambda item: item[1], reverse=True)
        )
    num = 0
    print("\n-------------------------------------")
    print("    selection\t  |\t  cost")
    print("-------------------------------------")
    for k, v in cost_sorted.items():
        print("%10s\t  |\t%.4f" % (k, v))
        num += 1
        if (num >= 8) & (wrap == True):
            break
    print("-------------------------------------")