[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)

### Practical Data Science with Python

# 11e. Solvers

[comment]: # (!!!)

## Solvers solve puzzles

- Variables ($x$, $y$, $z$)
- Constraints ($x$ is an integer, $0 < y < 11$, $x + 3y + 2z \leq 9$)
- Objective (Maximize $3x + 4y + 5z$)

[comment]: # (!!!)

## Types of problem

- Linear programming: variables are floats, constraints and objectives are linear. (Gurobi, CBC, GLOP)
- Mixed-Integer: Like linear, but some variables are integers (SCIP)
- Non-linear (convex): Objectives and constraints are convex. (IPOPT)
- Non-linear, non-convex: They aren't even convex. (BARON, ANTIGONE)

[comment]: # (!!!)

## Google or-tools

Wraps GLOP and SCIP

- Linear programming, Mixed Integer Programming
- Vehicle routing
- Graph algorithms and network flows
- Assignment and scheduling problems 

[comment]: # (!!!)

# Demo

### [Colab](https://colab.research.google.com/drive/1f_fUFa-s03GhQgqHZTU0ir86UHfM9bCd?usp=sharing)

[comment]: # (!!!)


# Questions?

