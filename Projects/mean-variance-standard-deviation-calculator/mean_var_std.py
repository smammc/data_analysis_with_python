import numpy as np

def calculate(list):
    # If a list < 9 elements raise a ValueError exception
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
        exit
    
    # The function should convert the list into a 3 x 3 Numpy array
    array = np.reshape(list, (3,3))
    
    # Mean
    M, M_0, M_1 = [], [], []
    for value in np.mean(array, axis=0):
        M_0.append(value.astype('float'))
    for value in np.mean(array, axis=1):
        M_1.append(value.astype('float'))
    M.append(M_0)
    M.append(M_1)
    M.append(np.mean(array.flatten()))

    # Variance
    V, V_0, V_1 = [], [], []
    for value in np.var(array, axis=0):
        V_0.append(value.astype('float'))
    for value in np.var(array, axis=1):
        V_1.append(value.astype('float'))
    V.append(V_0)
    V.append(V_1)
    V.append(np.var(array.flatten()))

    # Std
    Std, Std_0, Std_1 = [], [], []
    for value in np.std(array, axis=0):
        Std_0.append(value.astype('float'))
    for value in np.std(array, axis=1):
        Std_1.append(value.astype('float'))
    Std.append(Std_0)
    Std.append(Std_1)
    Std.append(np.std(array.flatten()))

    # Max
    Max_, Max_0, Max_1 = [], [], []
    for value in np.max(array, axis=0):
        Max_0.append(value.astype('int'))
    for value in np.max(array, axis=1):
        Max_1.append(value.astype('int'))
    Max_.append(Max_0)
    Max_.append(Max_1)
    Max_.append(np.max(array.flatten()))

    # Min
    Min_, Min_0, Min_1 = [], [], []
    for value in np.min(array, axis=0):
        Min_0.append(value.astype('int'))
    for value in np.min(array, axis=1):
        Min_1.append(value.astype('int'))
    Min_.append(Min_0)
    Min_.append(Min_1)
    Min_.append(np.min(array.flatten()))

    # Sum
    Sum_, Sum_0, Sum_1 = [], [], []
    for value in np.sum(array, axis=0):
        Sum_0.append(value.astype('int'))
    for value in np.sum(array, axis=1):
        Sum_1.append(value.astype('int'))
    Sum_.append(Sum_0)
    Sum_.append(Sum_1)
    Sum_.append(np.sum(array.flatten()))
    
    calculations = {
        'mean': M,
        'variance': V,
        'standard deviation': Std,
        'max': Max_,
        'min': Min_,
        'sum': Sum_
    }
    return calculations