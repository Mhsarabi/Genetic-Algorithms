
import random as rnd

p_s = 200       # Population size
n = 8           # Number of queens
m_r = 0.8       # Mutation rate
epoch = 200     # Maximum number of generations


# Generate the initial population
def init_population(population_size, N):
    population_list = []

    for i in range(population_size):
        new_member = []

        # Each gene represents the row position of a queen in a column
        for j in range(N):
            new_member.append(rnd.randint(1, N))

        new_member.append(0)  # Fitness value
        population_list.append(new_member)

    return population_list


# Generate offspring using one-point crossover
def cross_over(population_list):
    for i in range(0, len(population_list), 2):

        # Exchange the second half of the parents' chromosomes
        chil1 = population_list[i][:len(population_list[0])//2] + population_list[i+1][len(population_list[0])//2:len(population_list[0])-1] + [0]
        chil2 = population_list[i+1][:len(population_list[0])//2] + population_list[i][len(population_list[0])//2:len(population_list[0])-1] + [0]

        population_list.append(chil1)
        population_list.append(chil2)

    return population_list


# Apply mutation to introduce diversity
def mutation(population_list, mutation_rate, n):
    choosen_one = [i for i in range(len(population_list)//2, len(population_list))]

    # Randomly shuffle offspring indices
    for i in range(len(population_list)//2):
        new_random = rnd.randint(0, (len(population_list)//2)-1)
        choosen_one[new_random], choosen_one[i] = choosen_one[i], choosen_one[new_random]

    # Select offspring according to the mutation rate
    choosen_one = choosen_one[:int(len(choosen_one)*mutation_rate)]

    for i in choosen_one:
        new_ch = rnd.randint(0, n-1)
        new_value = rnd.randint(1, n)
        population_list[i][new_ch] = new_value

    return population_list


# Calculate conflicts between queens and evaluate chromosomes
def fitness(population_list, n):
    i = 0
    length = len(population_list)

    while i < length:
        j = 0
        conflict = 0

        while j < n:
            k = j + 1

            while k < n:

                # Check for queens in the same row
                if population_list[i][j] == population_list[i][k]:
                    conflict += 1

                # Check for queens on the same diagonal
                if abs(j-k) == abs(population_list[i][j] - population_list[i][k]):
                    conflict += 1

                k += 1
            j += 1

        population_list[i][n] = conflict
        i += 1

    # Sort chromosomes by fitness (lower is better)
    for i in range(len(population_list)):
        _min = i

        for j in range(i, len(population_list)):
            if population_list[j][n] < population_list[_min][n]:
                _min = j

        population_list[i], population_list[_min] = population_list[_min], population_list[i]

    return population_list


# Initialize and evaluate the population
population = init_population(p_s, n)
population = fitness(population, n)

if population[0][n] == 0:
    print("Solution found:", population[0][0:n])

else:
    for i in range(epoch):
        population = cross_over(population)
        population = mutation(population, m_r, n)
        population = fitness(population, n)

        # Keep the best 50% of the population
        population = population[:len(population)//2]

        if population[0][n] == 0:
            print("Solution found:", population[0][0:n])
            break
        else:
            print("*", i+1, "------> Best Solution so far:", population[0])
