import statistics as st

from numpy import random, sqrt, log, sin, cos, pi, argmax
from matplotlib import pyplot as plt
import math


# transformation function
def gaussian(u1, u2):
    z1 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
    z2 = sqrt(-2 * log(u1)) * sin(2 * pi * u2)
    return z1, z2


def normal(mean, variance):
    """
    Normal implementation
    :param mean:
    :param variance:
    :return:
    """
    u1 = random.rand()
    u2 = random.rand()
    z1, z2 = gaussian(u1, u2)
    return mean + (z1 * variance)


def choose_arm(arms, q, e):
    """
    This method with choose the arms based on
        1.argmax of "Q" with a probablity of e and
        2.Randomly with probablity of 1-e
    :param arms: consists of mean reward for each arm
    :param q: Value for each arm
    :param e: epsilon
    :return: The chosen arm
    """
    ran_prob = random.random()
    if ran_prob < e:
        arm = random.choice(len(arms))
    else:
        arm = argmax(q)
    return arm
    # return random.choice((random.choice(len(arms)), argmax(q)), None, False, (e, 1 - e))


def choose_arm_ucb(q, c, n, step):
    """
    This method will choose arm based on UCB algorithm
    :param q: Value for each arm (arm is referred with the index of the array)
    :param c: constant
    :param n: Number of times the arm has been chosen till time t
    :param step: the current step or time t
    :return: The arm chosen
    """
    if step > 0:
        resultant = [q[i] + (c * sqrt(math.log(step) / n[i])) for i in range(len(q))]
        return argmax(resultant)

    return argmax(q)


def initialize_arms_ucb(arms, q, n, number_of_initial_runs):
    """
    To initialize arms n number of times to avoid divide by zero error
    :param arms: arms with mean reward
    :param q: value for each arm
    :param n: number of times arm has been chosen till time t
    :param number_of_initial_runs: number of times arms are initialised
    :return: no return
    """
    for arm in range(len(arms)):
        for i in range(number_of_initial_runs):
            reward_obtained(arms, arm, q, n)


def reward_obtained(arms, k, q, n):
    """
    This method calculates the reward obtained for the chosen arm and updates the value of Q and N
    :param arms: arms with mean reward
    :param k: chosen arm
    :param q: value for each arm
    :param n: number of times arm has been chosen till time t
    :return: The reward obtained for the given step
    """
    reward = random.normal(arms[k], scale=sqrt(10))
    # reward = normal(arms[k], 1)
    n[k] += 1
    q[k] = q[k] + ((reward - q[k]) / n[k])
    return reward


def average(sim_value, num_steps, num_simulation):
    """
    Return the average value of simulations
    :param sim_value: Values obtained across all the simulations
    :param num_steps: Number of steps in each simualtion
    :param num_simulation: Number of simulations
    :return: Average value (reward/optimal action)
    """
    avg_list = []
    for i in range(0, num_steps):
        temp_list = [step[i] for step in sim_value]
        step_avg = sum(temp_list) / num_simulation
        avg_list.append(step_avg)
    return avg_list


def simulate_greedy(num_arms, num_simualtion, num_steps, e):
    """
    Simulate method for Greedy algorithm
    :param num_arms: number of arms
    :param num_simualtion: number of simulations to run
    :param num_steps: number of steps in each simulation
    :param e: epsilon value
    :return: average reward and optimal action
    """
    # arms = {i: normal(0, 1) for i in range(num_arms)}
    arms = random.normal(0, 1, num_arms)
    arm_with_max_reward = argmax(arms)
    result_sim = []
    optimal_action_sim = []

    for sim in range(num_simualtion):
        # count_optimal = 0
        q = [0 for i in range(num_arms)]
        n = [0 for i in range(num_arms)]
        optimal_action_step = [0 for i in range(1000)]
        result_step = [0 for i in range(num_steps)]
        for step in range(num_steps):
            armchosen = choose_arm(arms, q, e)
            result_step[step] = reward_obtained(arms, armchosen, q, n)
            if armchosen == arm_with_max_reward:
                optimal_action_step[step] = 1
            else:
                optimal_action_step[step] = 0
        result_sim.append(result_step)
        optimal_action_sim.append(optimal_action_step)

    return average(result_sim, num_steps, num_simualtion), average(optimal_action_sim, num_steps,
                                                                   num_simualtion)


def simulate_ucb(num_arms, num_simualtion, num_steps, c):
    """
    Simulation method for UCB method
    :param num_arms: number of arms
    :param num_simualtion: number of simulations
    :param num_steps: number of steps in each simulation
    :param c: value of C
    :return: average reward and optimal action
    """
    # arms = {i: normal(0, 1) for i in range(num_arms)}
    arms = random.normal(0, sqrt(10), num_arms)
    arm_with_max_reward = argmax(arms)
    result_sim = []
    optimal_action_sim = []

    for sim in range(num_simualtion):
        # count_optimal = 0
        q = [0 for i in range(num_arms)]
        n = [0 for i in range(num_arms)]
        optimal_action_step = [0 for i in range(1000)]
        result_step = [0 for i in range(num_steps)]
        initialize_arms_ucb(arms, q, n, 1)
        for step in range(num_steps):
            armchosen = choose_arm_ucb(q, c, n, step)
            result_step[step] = reward_obtained(arms, armchosen, q, n)
            if armchosen == arm_with_max_reward:
                optimal_action_step[step] = 1
            else:
                optimal_action_step[step] = 0
        print(sim)
        result_sim.append(result_step)
        optimal_action_sim.append(optimal_action_step)

    return average(result_sim, num_steps, num_simualtion), average(optimal_action_sim, num_steps,
                                                                   num_simualtion)


def main():
    dict_params_greedy = {"Epsilon: 0.5": (10, 2000, 1000, 0.5), "Epsilon: 0.3": (10, 2000, 1000, 0.3),
                          "Epsilon: 0.2": (10, 2000, 1000, 0.2),"Epsilon: 0.1": (10, 2000, 1000, 0.1),
                          "Epsilon: 0.05": (10, 2000, 1000, 0.05)}

    dict_params_ucb = {"C: 5": (10, 2000, 1000, 5),
                       "C: 2": (10, 2000, 1000, 2), "C: 1": (10, 2000, 1000, 1),
                       "C: 0.5": (10, 2000, 1000, 0.5), "C: 0.1": (10, 2000, 1000, 0.1)}

    results_greedy = {key: simulate_greedy(*params) for key, params in dict_params_greedy.items()}

    results_ucb = {key: simulate_ucb(*params) for key, params in dict_params_ucb.items()}

    # Plotting for UCB
    for key, val in results_ucb.items():
        plt.plot(val[0], label=key)

    plt.ylabel("Average reward")
    plt.xlabel("Steps")
    plt.legend()
    plt.title("UCB performance at different values of c, N(0,10)")
    plt.show()
    plt.close()

    for key, val in results_ucb.items():
        plt.plot(val[1], label=key)
    plt.legend()
    plt.ylabel("% Optimal Action")
    plt.title("UCB performance at different values of c, N(0,10)")
    plt.xlabel("Steps")
    plt.show()
    plt.close()

    # # Plotting for Greedy
    for key, val in results_greedy.items():
        plt.plot(val[0], label=key)

    plt.ylabel("Average reward")
    plt.xlabel("Steps")
    plt.legend()
    plt.title("Epsilon Greedy performance at different values of e with N(0,10) reward distribution")
    plt.show()
    plt.close()

    for key, val in results_greedy.items():
        plt.plot(val[1], label=key)
    plt.legend()
    plt.ylabel("% Optimal Action")
    plt.title("Epsilon Greedy performance at different values of e with N(0,10) reward distribution")
    plt.xlabel("Steps")
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
