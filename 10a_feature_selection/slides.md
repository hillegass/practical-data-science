[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)

### Practical Data Science with Python

# 10a. Feature Selection

[comment]: # (!!!)

## Features

### Often you already know.

- Important: helps us make predictions
- Worthless: doesn't help us make predictions

***

### Flavors of worthless:
- Irrelevant
- Redundant

[comment]: # (!!!)

## Feature selection is hard

You have $n$ features?

Train and test all $2^n - 1$ possibilities!

[comment]: # (!!!)

## Practical appoaches

- Forward: Start with one and keep adding
- Backward: Start with the all and keep subtracting
- Instrisic: Lasso regression, for example

[comment]: # (!!!)


# Demo

### [Colab](https://colab.research.google.com/drive/17MUpZ_wMrSYqRORWfA-3CkpejtmAKzt0)

[comment]: # (!!!)

## Forward Selection for regression

Let $y$ be what you are trying to match.

Find an input $x_i$ that has high $\phi-k$ correlation with $y$

Fit a model using just $x_i$, find the residual. Get the $R^2$ score.

Find an input $x_j$ that has high $\phi-k$ correlation with the residual.

Fit a model using just $x_i$ and $x_j$,  find the residual.

Repeat.

[comment]: # (!!!)


## Mutual Information

What about classification?

How much does observing one random variable tell me about another?

Best for categorical data.

[comment]: # (!!!)

# Demo (Mutual Information)

### [Colab](https://colab.research.google.com/drive/1lZix0OAKgK_jJhA47eBD_tG7NeM58EuC)

[comment]: # (!!!)


## What about continuous in classification?

Nothing great, honestly.

Kendall's Ranking Coefficient for simple models.

[comment]: # (!!!)


# Questions?

[comment]: # (!!!)
