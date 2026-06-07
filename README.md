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

$$ H = - J_{ij} \sum_{\langle i j \rangle} \sigma_i \sigma_j + \mu \sum_i h_i \sigma_i $$

The $\langle i j \rangle$ notation is used to represent nearest neighbours, so the first sum is therefore over all nearest neighbours. And in this first sum $J_{ij}$ is the interaction strength between adjacent atoms. The second sum takes into account the effects of an external magnetic field with a component (anti)parallel to the spin axis. Therefore this gives us $\mu$ as representing the magnetic moment of the atoms, and $h_j$ being the strength of the (component of the) external magnetic field at point $j$.

If the interaction strength $J_{ij}$ is positive, then the interaction is ferromagnetic and adjacent atoms will attempt to align themselves as it's a more energetically favourable configuration. Whereas if the interaction strength is negative, the interaction is antiferromagnetic and atoms will tend to align in a checkerboard pattern.




