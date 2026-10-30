# Genetic Algorithms

A collection of optimization problems implemented using Genetic Algorithms (GA) in Python.

This repository contains two classic problems that demonstrate how Genetic Algorithms can be applied to search for solutions in different problem domains.

## Projects

### 1. N-Queens Problem

The N-Queens problem aims to place N queens on an N × N chessboard so that no two queens attack each other.

**Implementation highlights:**
- Random population initialization
- One-point crossover
- Mutation
- Fitness evaluation based on queen conflicts
- Selection of the best individuals

[Read Documentation](docs/n-queens.md)

### 2. Traveling Salesperson Problem (TSP)

The Traveling Salesperson Problem aims to find the shortest possible route that visits every city exactly once and returns to the starting city.

**Implementation highlights:**
- Random city generation
- Random route initialization
- Mutation through city swapping
- Euclidean distance calculation
- Selection based on route length
- Visualization using OpenCV and Matplotlib

**Note:** The current implementation uses parent copying followed by mutation rather than traditional crossover.

[Read Documentation](docs/tsp.md)

## Project Structure

```text
Genetic-Algorithms/
│
├── N-Queens/
│   └── main.py
│
├── TSP/
│   └── main.py
│
├── docs/
│   ├── n-queens.md
│   └── tsp.md
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.10 or higher
- NumPy
- Matplotlib
- OpenCV

## Installation

Clone the repository:

```bash
git clone https://github.com/Mhsarabi/Genetic-Algorithms
```

Navigate to the project directory:

```bash
cd Genetic-Algorithms
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run each project independently:

**N-Queens:**

```bash
python N-Queens/main.py
```

**Traveling Salesperson Problem:**

```bash
python TSP/main.py
```

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.