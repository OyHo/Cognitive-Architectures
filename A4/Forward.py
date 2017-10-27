from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.supervised.trainers import BackpropTrainer

# maps input -> output
ds = SupervisedDataSet(1, 1)
for set in range (1,9):
    ds.addSample(set,set)

attempt = SupervisedDataSet(1, 1)
attempt.addSample(-5, -5)
attempt.addSample(5, 5)
attempt.addSample(50, 50)
attempt.addSample(2000, 2000)

net = buildNetwork(1, 8, 1, hiddenclass=TanhLayer) # minimun 3 hidden
net.sortModules()
trainer = BackpropTrainer(net, ds)

trainer.trainUntilConvergence(verbose=False, validationProportion=0.15, maxEpochs=1000, continueEpochs=10)
# print training results
print net.activateOnDataset(ds)
# print testing results
print net.activateOnDataset(attempt)

print(net)
print(net.params)
print(sum(net.params))