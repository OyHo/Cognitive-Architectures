from random import uniform

def step(value):
    if value >= 0:
        return 1
    else:
        return 0

def Plearn(input):
    w = [] # Initialisation
    for weight in range(0, 2):
        w.append(uniform(-0.5, 0.5))

    #w = [-0.4, 0.3]
    sigma = 0.2

    print "Initial Weight: ", w
    print "Threshold: ", sigma
    Y = [0] * len(input)
    Yd = []
    for i in range(len(input)):
        Yd.append(input[i][1])
    sum = 0
    epoch = 0
    limit = 50
    while True:
        epoch = epoch + 1
        for p in range(len(input)): # Activation
            print "\n" + "Epoch: ", p
            print "Inputs: ", input[p][0]
            for i in range(len(input[p][0])):
                sum += input[p][0][i]*w[i]
            print "The sum of input times weights", sum
            Y[p] = step(sum - sigma)

            # Training
            alpha = 0.1 # learing rate
            print "Initial Weight", w
            for weight in range(len(w)):
                w[weight] = w[weight] + alpha * \
                                        input[p][0][weight] *(input[p][1] - Y[p])
            print "Final Weight: ", w
        Error = [x - y for (x, y) in zip(Yd, Y)]
        #Error = list(set(Y)-set(Yd))
        if ( p != 0 and p % 3 == 0 ):
            print "Desired output, Yd: ", Yd
            print "Actual output, Y: ", Y
            print "Error, e: ", Error

        if Error == [0]*4 or epoch > limit:
            break

AND = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1)
]

OR = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 1)
]

Plearn(AND)