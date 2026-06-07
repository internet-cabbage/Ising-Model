# Ising-Model

An interactive 2D-Ising Model program written in Python.

## Theory

The Ising model is a way of mathematically behaving the phenomena of 'Ferromagnetism'. A material being ferromagnetic just means it's atoms have a non-zero magnetic moment such that it is capable of exihibiting bulk magnetic properties.

The actual reason for these atoms having a magnetic moment is due to the electrons in the atom orbitting the nucleus (such a motion of a charged particle is close to the ideal case), as well as the spin's of the electrons themselves. However the specifics of how these electron motions contributes to the magnetic moment is irrelevant to the actual model itself, which concerns bulk properties.

## Background

The Ising model is a simple model which makes several assumptions about the behaviour of the material:

  -  The material is a square lattice without any impurities or irregularities
  -  Each site on the lattice (representing an atom or molecule) can only have a spin value of -1 or +1. Whilst this is good at modelling ferromagnetism, it is unable to model ferrimagnetism.
  -  Each site on the lattice can only interact with its direct nearest neighbours (i.e. those directly touching it excluding diagonals)

The Hamiltonian for the system is:

$$ H = - j $$
