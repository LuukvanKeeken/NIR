from dataclasses import dataclass
import typing

import numpy as np


Connectivity = typing.NewType("Connectivity", list[typing.Tuple[int, int]])


@dataclass
class NIR:
    """Neural Intermediate Representation (NIR)"""

    units: typing.List[typing.Any]  # List of units
    connectivity: Connectivity


class NIRUnit:
    """Basic Neural Intermediate Representation Unit (NIRUnit)"""

    pass


@dataclass
class LeakyIntegrator(NIRUnit):
    """Leaky integrator neuron model.

    The leaky integrator neuron model is defined by the following equation:
    $$
    \tau \dot{v} = (v_{leak} - v) + R I
    $$
    Where $\tau$ is the time constant, $v$ is the membrane potential,
    $v_{leak}$ is the leak voltage, $R$ is the resistance, and $I$ is the
    input current.
    """

    tau: np.ndarray  # Time constant
    r: np.ndarray  # Bias
    v_leak: np.ndarray  # Leak voltage


@dataclass
class Linear(NIRUnit):

    weights: np.ndarray  # Weights M * N
    bias: np.ndarray  # Bias M


@dataclass
class Conv1d(NIRUnit):
    """Convolutional layer in 1d"""

    weights: np.ndarray  # Weights C_out * C_in * X
    stride: int  # Stride
    padding: int  # Padding
    dilation: int  # Dilation
    groups: int  # Groups
    bias: np.ndarray  # Bias C_out


@dataclass
class Conv2d(NIRUnit):
    """Convolutional layer in 2d"""

    weights: np.ndarray  # Weights C_out * C_in * X * Y
    stride: int  # Stride
    padding: int  # Padding
    dilation: int  # Dilation
    groups: int  # Groups
    bias: np.ndarray  # Bias C_out
