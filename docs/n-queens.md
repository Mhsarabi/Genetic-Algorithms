# N-Queens Problem Using Genetic Algorithm

## 1. Problem Description

The N-Queens problem is a classic combinatorial optimization problem. The goal is to place N queens on an N × N chessboard so that no two queens attack each other.

In chess, a queen can attack another queen if they are in the same row, column, or diagonal.

A valid solution must satisfy the following constraints:

- No two queens share the same row.
- No two queens share the same column.
- No two queens share the same diagonal.

In this implementation, the board size is 8 × 8, and the goal is to find a valid arrangement of 8 queens.

## 2. Genetic Algorithm Approach

A Genetic Algorithm (GA) is used to search for a valid arrangement of queens.

Each individual in the population represents a possible solution to the problem.

### 2.1. Chromosome Representation

Each chromosome is represented as a list of N + 1 elements.

- The first N elements represent the positions of the queens.
- Each index represents a column.
- Each value represents the row in which the queen is placed.
- The last element stores the fitness value.

For example:

`[1, 5, 8, 6, 3, 7, 2, 4, 0]`

The first eight elements represent the positions of the queens, while the last element (`0`) is the initial fitness placeholder.

This representation guarantees that no two queens are placed in the same column.

### 2.2. Initial Population

The initial population consists of randomly generated chromosomes.

Each queen is assigned a random row between 1 and N.

### 2.3. Fitness Function

The fitness function calculates the number of conflicts between queens.

Two types of conflicts are considered:

1. **Row Conflict:** Two queens are placed in the same row.
2. **Diagonal Conflict:** Two queens are placed on the same diagonal.

The diagonal condition is:

`abs(col1 - col2) == abs(row1 - row2)`

The fitness value represents the total number of conflicts.

**A fitness value of 0 indicates a valid solution.**

Lower fitness values represent better solutions.

### 2.4. Crossover

A one-point crossover operation is used.

Two parent chromosomes are combined by exchanging the second half of their genes.

The crossover point is located at the midpoint of the chromosome, excluding the fitness element.

Two offspring are generated from each pair of parents.

### 2.5. Mutation

Mutation introduces random changes into the population to maintain genetic diversity.

In this implementation:

- The mutation rate is 0.8 (80%).
- Selected offspring are randomly chosen for mutation.
- One gene in each selected chromosome is replaced with a random row value.

### 2.6. Selection

After crossover and mutation, the fitness of the population is evaluated.

The population is sorted in ascending order based on fitness.

Only the best 50% of individuals are retained for the next generation.

## 3. Algorithm Parameters

| Parameter | Value | Description |
|---|---:|---|
| Board Size (N) | 8 | Number of queens and board dimensions |
| Population Size | 200 | Number of individuals in the initial population |
| Mutation Rate | 0.8 | Probability of selecting offspring for mutation |
| Maximum Epochs | 200 | Maximum number of generations |

## 4. Execution

Run the following command:

```bash
python N-Queens/main.py
```

The algorithm continues evolving the population until either a valid solution is found or the maximum number of epochs is reached.

## 5. Output

When a valid solution is found, the program prints the chromosome representing the queen positions.

If no valid solution is found within the maximum number of epochs, the program prints the best solution found in each generation.