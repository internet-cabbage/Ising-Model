# Ising-Model



An interactive 2D Ising model simulation written in python, featuring real-time visualisation, data graphing, and parameters which are configurable during runtime.

[INSERT GIF HERE]

## Features

  -  Configurable temperature, interaction strength (and sign), and external magnetic field strength and direction
  -  Real-time visualisation of spin states of the atoms on the lattice
  -  Implementation of the Metropolis-Hastings algorithm

## Installation

```
git clone https://github.com/internet-cabbage/Ising-Model.git
cd ising-model
pip install -r requirements.txt
```

## Usage

```
python 2DIsingModel.py
```

Simulation parameters are configured during runtime using sliders and buttons present on the GUI.

# Requirements

  - Python 3.10+
  - NumPy
  - Numba
  - MatPlotLib

## Theory

The Ising model is a way of mathematically modelling the phenomena of 'Ferromagnetism'. A material being ferromagnetic just means it's atoms have a non-zero magnetic moment such that it is capable of exhibiting bulk magnetic properties.

The actual reason for these atoms having a magnetic moment is due to the electrons in the atom orbiting the nucleus (such a motion of a charged particle is close to the ideal case), as well as the spin's of the electrons themselves. However the specifics of how these electron motions contributes to the magnetic moment is irrelevant to the actual model itself, which concerns bulk properties.

## Background

The Ising model is a simple model which makes several assumptions about the behaviour of the material:

  -  The material is a square lattice without any impurities or irregularities
  -  Each site on the lattice (representing an atom or molecule) can only have a spin value of -1 or +1. Whilst this is good at modelling ferromagnetism, it is unable to model ferrimagnetism.
  -  Each site on the lattice can only interact with its direct nearest neighbours (i.e. those directly touching it excluding diagonals)
  -  All of the nearest neighbours have the same interaction strength (i.e. all atoms are the same element)

The Hamiltonian for the system is:

$$ H = - J_{ij} \sum_{\langle i j \rangle} \sigma_i \sigma_j + \mu \sum_i h_i \sigma_i $$

The $\langle i j \rangle$ notation is used to represent nearest neighbours, so the first sum is therefore over all nearest neighbours. And in this first sum $J_{ij}$ is the interaction strength between adjacent atoms. The second sum takes into account the effects of an external magnetic field with a component (anti)parallel to the spin axis. Therefore this gives us $\mu$ as representing the magnetic moment of the atoms, and $h_j$ being the strength of the (component of the) external magnetic field at point $j$.

If the interaction strength $J_{ij}$ is positive, then the interaction is ferromagnetic and adjacent atoms will attempt to align themselves as it's a more energetically favourable configuration. Whereas if the interaction strength is negative, the interaction is antiferromagnetic and atoms will tend to align in a checkerboard pattern.

When the model has no external magnetic field, it exhibits a phase transition between ordered and unordered states at a temperature:

$$T_C = \frac{2J}{k (\ln{1 + \sqrt{2}})} \approx 2.269 \left( \frac{J}{k} \right)$$

Above the Curie temperature $T_C$ the system will be in an unordered state, and below $T_C$ it will converge to a fully aligned state for $J>0$ and a fully anti-aligned state for $J<0$.

Currently this program only supports the Metropolis-Hastings algorithm.


### Metropolis-Hastings algorithm

The Metropolis-Hastings algorithm is a stochastic algorithm which works by randomly selecting a site on the lattice, and examining the change in energy if that specific site had its spin flipped. If the flip results in the energy decreasing, then it will be accepted. For the case of increasing energy, it will be accepted with probability $e^{- \frac{\Delta E}{T} }$ given by the Boltzmann probability.

## Planned Features

  -  [ ] Wolff cluster algorithm
  -  [ ] Ability to change what the graph displays (etc. energy)
  -  [ ] Export of simulation data


