[comment]: # (THEME = pdsp)
[comment]: # (CODE_THEME = base16/zenburn)

### Practical Data Science with Python

# 11a. Cross Validation and Regularization

[comment]: # (!!!)

## Overfitting

<img src="11a_media/overfitting.png" height="350" /> 


| Fit  |   On Training  |  On Test  |
| :---: | :---: | :---: |
| Under | Lousy  | Lousy |
| Good  | Good   | Good   |
| Over  | Great  | Lousy |

[comment]: # (!!!)

## Logistic regression + Regularization

### $J = \left(\frac{1}{N}\sum_{i = 1}^{N} \left(-y_i \ln \hat{y_i} - (1 - y_i) \ln (1 -\hat{y_i}) \right) \right) + $
### $\frac{1}{C} \sum_{i = 0}^{d}\beta_i^2$

```python
logreg = sklearn.linear_model.LogisticRegression(C=2.0)
```

[comment]: # (!!!)


## Test set

```python
from sklearn.cross_validation import train_test_split 
...
split_list = train_test_split(df, test_size=0.2)
train_df = split_list[0]
test_df = split_list[1]
X_train = ..., Y_train = ..., X_test = ... Y_test = ...
c_values = [0.1, 0.5, 1.0, 2.0, 5.0]
for c in c_values:
	logreg = sklearn.linear_model.LogisticRegression(C=c)
	logreg.fit(X_train, Y_train)
	accuracy = logreg.score(X_test, Y_test)
	print(f"{c}: {accuracy}")
```
[comment]: # (!!!)

## Train/Validation/Test data

- **Training** data: model is fitted to it for every hyperparameter
- **Validation** data: model is scored for every hyperparameter
- **Test** data: Scored after hyperparameter is fixed

### Golly, we need an awful lot of data!

[comment]: # (!!!)

## Cross Validation

### Use training data for validation too!

<img src="11a_media/crossvalidation.png" height="350" /> 

[comment]: # (!!!)


## Cross Validation in Python

```pyton
possible_values = ...
best_score = 0.0
for c in possible_values:
    clf = LogisticRegression(C=c)
    scores = cross_val_score(clf, X_train, Y_train, cv=5)
    mean_score = scores.mean()
    print(f"{c}: {mean_score}")
```

[comment]: # (!!!)


# Demo

### [Colab](https://colab.research.google.com/drive/1qHYwpsYGqzzENLJflkJ9naBUsMXWu-j2?usp=sharing)


[comment]: # (!!!)

# Questions?

