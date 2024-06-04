# Dice Lab Assessment

Checkpoints 1 and 2 look good. Checkpoint 3 doesn't appear to be done--I can come 
back to this if you finish this up (or just need to `mwc submit`)

## Checkpoint 1

Using Counter was effective, although `is_three_of_a_kind`
fails with [1, 1, 1, 1, 1]. You could simplify further with 
some additional idiomatic python:

```
def is_three_of_a_kind(self):
    return max(Counter(self.faces())) >= 3
```

`is_four_of_a_kind` has a similar bug.

## Checkpoint 2
The content of your docstrings looks good. However, most are above their function
rather than inside it. This technically works, but defeats some of the purpose of 
docstrings, as there are automated tools that use them and expect to find them in 
the right place. 

## Checkpoint 3
Not done.
