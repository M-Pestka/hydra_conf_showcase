# quick showcase of hydra structured configs

Usage:
```
python3 test_hydra.py
```


change param:

```
python3 test_hydra.py optimizer.beta1=0.8
python3 test_hydra.py optimizer.beta1=some_string # error, because a float is expected
python3 test_hydra.py optimizer=sgd
python3 test_hydra.py optimizer=adagrad # error because the config does not match a pattern
```
