import numpy as np
import matplotlib.pyplot as plt
import numba
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


N = 100
beta = 100
j=-1
gridShape = (N,N)

spins = np.random.choice([-1,1], gridShape)

def spinFlip(x,y):
    spinsInput = spins.copy()
    spinCurrent = spinsInput[x,y]
    spinFlip = -spinCurrent

    currentEnergy = getEnergy(x,y,spinsInput, spinCurrent)
    flipEnergy = getEnergy(x,y,spinsInput, spinFlip)
    if flipEnergy < currentEnergy:
        spins[x,y] = spinFlip
    else:
        deltaEnergy = np.abs(currentEnergy - flipEnergy)
        thermalFlipProb = np.exp(-beta*deltaEnergy)
        if thermalFlipProb > np.random.uniform():
            spins[x,y] = spinFlip
        else:
            pass


def getEnergy(x,y,spins, spinCompare):
    spin_i = spins[x,y]
    spinFlip = -spin_i
    E_i = 0
    E_f = 0
    spinCompare = spinCompare * j
    # Boundary conditions
    #     # Central case
    if 0 < x < N-1 and 0 < y < N-1:
        sum = spinCompare * (spins[x+1,y] + spins[x-1,y] + spins[x, y+1] + spins[x, y-1])

    # corner cases

    elif x == 0 and y == 0: # Top left
        sum = spinCompare * (spins[1,0] + spins[0,1])
    elif x == N-1 and y == 0: # Top right
        sum = spinCompare * (spins[N-2,0] + spins[N-1, 1])
    elif x == 0 and y == N-1: # Bottom left
        sum = spinCompare * (spins[0,N-1] + spins[1, N-1])
    elif x == N-1 and y == N-1: # Bottom right
        sum = spinCompare * (spins[N-2,N-1] + spins[N-1, N-2])
    
    # Edge cases

    elif 0 < x < N - 1 and y==0: # Top row
        sum = spinCompare * (spins[x-1,0] + spins[x+1,0] + spins[x,1])
    elif 0 < x < N - 1 and y == N-1: # Bottom row
        sum = spinCompare * (spins[x-1, N-1] + spins[x+1, N-1] + spins[x, N-2])
    elif x == 0 and 0 < y < N-1: # Left column
        sum = spinCompare * (spins[0,y+1] + spins[0,y-1] + spins[1,y])
    elif x == N-1 and 0 < y < N-1: # Right column
        sum = spinCompare * (spins[N-1,y+1] + spins[N-1, y-1] + spins[N-2,y])
    
    return sum
    


fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

# ============================================
#   Animation
# ============================================

stepsPerFrame = 50 

spinData = ax.imshow(spins)


def animate(frame):
    for i in range(0,stepsPerFrame):
        x,y = np.random.randint(N-1, size=(2, stepsPerFrame))
        spinFlip(x[i],y[i])
    spinData.set_data(spins)
    return [spinData]

animation = FuncAnimation(fig,animate, interval=1, blit=True)




plt.show()