[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)

### Practical Data Science with Python

# 15. Gradient Boosting

[comment]: # (!!!)

## Boosting for regression

Making $F_M: R^d \rightarrow R$.  

1. Start with a weak regressor $F_0 = h_0$
2. For each $i < M$:
	1. Compute the residual of $F_i$
	2. Make a weak regressor $h_{i+1}$ that predicts residual
	3. $F_{i+1}(x) = F_i(x) + \alpha h_{i+1}(x)$

$\alpha$ is something like 0.1

$M$ is something like 1000.

[comment]: # (!!!)

## Step 1

| gender | grip |  life_exp  |
|--------|---------------|------------|
| m  |  34  |  78  |
| m  |  56  |  88  |
| f  |  62  |  92  |

#### $h_0(x) = \frac{78 + 90  + 94}{3} = 86$

[comment]: # (!!!)

## Step 2


| gender | grip |  life_exp  | $F_0$ | $R_0$ |
|--------|---------------|------------|-------|------|
| m  |  34  |  78  | 86 | -8 |
| m  |  56  |  88  |  86 | 2  |
| f  |  62  |  92  |  86 | 6  |

#### $h_1(x) =$ if grip > 45 then 4,  else -8

[comment]: # (!!!)

## Step 3

($\alpha = 0.5$)


| gender | grip_strength |  life_exp  | $F_1$ | $R_1$ |
|--------|---------------|------------|-------|-------|
| m  |  34  |  78  |  86 - 4 |  -4 |
| m  |  56  |  88  |  86 + 2  |  0 |
| f  |  62  |  92  |  86 + 2  |  4  |

#### $h_2(x) =$ if 'f' then -2,  else 4

[comment]: # (!!!)


## Step 4

| gender | grip_strength |  life_exp  | $F_2$ | $R_2$ |
|--------|---------------|------------|-------|-------|
| m  |  34  |  78  |  86 - 4 - 1 |  -3 |
| m  |  56  |  88  |  86 + 2 -1 |  1 |
| f  |  62  |  92  |  86 + 2 + 2 |  2  |

[comment]: # (!!!)

## CatboostRegressor

- Developed at Yandex
- Open source
- Released 2017

```python
from catboost import CatBoostRegressor

regressor = CatBoostRegressor()
model.fit(X_train, y_train)

y_preds = model.predict(y_test)
```

[comment]: # (!!!)

## Others

- XGBoost
	- Developed by DMLC
	- Open source
	- Released 2014

- LightGBM
	- Developed by Microsoft
	- Open Source
	- Released 2016

[comment]: # (!!!)

## Odds

Odds are not probabilities! 

Odds are ratio between one event and all others.

Odds of rolling a 5 = $\frac{1}{5}$

Odds of rolling a 1,2,3, or 4 = $\frac{4}{2} = 2$

[comment]: # (!!!)

## Converting between odds and probability

If $p$ is the probability of an event and $r$ is the odds of the same event, we have the following:

#### $r =  \frac{p}{1 - p}$

#### $p = \frac{r}{1 + r}$

[comment]: # (!!!)


## Log Odds

Log of the odds

Log odds of rolling a 5 = $\log \frac{1}{5}$ \approx -1.61

Log dds of rolling a 1,2,3, or 4 = $\log \frac{4}{2} \approx 0.693$

[comment]: # (!!!)

## Converting between log odds and probability

If $r$ is a log odds of an event.  The probability of that event is 

#### $p = \frac{e^r}{1 + e^r}$

#### $r = \log \frac{p}{1 - p}$


[comment]: # (!!!)

## Converting between log odds and probability

If $r$ is a log odds of an event.  The probability of that event is 

#### $p = \frac{e^r}{1 + e^r}$

#### $r = \log \frac{p}{1 - p}$
[comment]: # (!!!)


## Sigmoid

#### $\sigma(r) = \frac{1}{1 + e^{-r}} = \frac{e^r}{1 + e^r} = p$

#### Logit is the inverse: $\log \frac{p}{1 - p}$

[comment]: # (!!!)

## Classification with Boosted Trees

We do regression on the probabilities.

We combine the outputs of the weak classifiers using log odds.

[comment]: # (!!!)

## Video

#### [Statquest's "Gradient Boost Part 3"](https://youtu.be/jxuNLH5dXCs)

[comment]: # (!!!)


# Questions?

