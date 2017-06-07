models = []

class Model(object):
    def __init__(self, root, inner_func, n):
        self.inner_func = inner_func
        self.label = root + str(n)
        self.last_output = None
        self.n = n

    def execute(self, val):
        temp = self.inner_func(val, self.n)
        self.last_output = temp
        return temp

plus_n = lambda x, n: x + n
min_n = lambda x, n: x - n
square_n = lambda x, n: x ** n
times_n = lambda x, n: x * n

models.append(plus_n)
#models.append(min_n)
#models.append(square_n)
models.append(times_n)

label_roots = {plus_n: "plus_", min_n: "min_", square_n: "square_", times_n: "times_"}

modelObjs = [Model(label_roots[model], model, i) for model in models for i in range(11)]

inputs = [1, 1, 4, 1, 7, 1, 10, 1, 13, 1, 16]

maxSpace = 4

for i in range(1,min(maxSpace,len(inputs)-1)):
    for j in range(i):
        input = inputs[j::i]

        consider_models = modelObjs[:]

        last_input = None
        for val in input:
            consider_models_next = consider_models[:]
            for model in consider_models:
                if last_input is not None and model.execute(last_input) != val:
                    consider_models_next.remove(model)
                else:
                    # predict next
                    pred = model.execute(val)
            consider_models = consider_models_next
            last_input = val

        for model in consider_models:
            print str(i) + "-space from", j, ": ", model.label
