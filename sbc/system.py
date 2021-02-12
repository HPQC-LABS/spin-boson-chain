#!/usr/bin/env python
r"""Contains class definition for the model parameters of the system.

``sbc`` is a library for simulating the dynamics of a generalized
one-dimensional spin-boson model, where both the :math:`z`- and 
:math:`y`-components of the spins are coupled to bosonic baths, rather than 
only the :math:`z`-components. The Hamiltonian of this model can be broken down
into the following components:

.. math ::
    \hat{H}(t) = \hat{H}^{(A)}(t) + \hat{H}^{(B)} + \hat{H}^{(AB)}(t),
    :label: system_total_Hamiltonian

where :math:`\hat{H}^{(A)}(t)` is the system Hamiltonian, which encodes all
information regarding energies associated exclusively with the spins; 
:math:`\hat{H}^{(B)}` is the bath Hamiltonian, which encodes all information
regarding energies associated with the components of the bosonic environment; 
and :math:`\hat{H}^{(AB)}(t)` is the system-bath coupling Hamiltonian, which 
describes all energies associated with the coupling between the system and the 
environment.

The system Hamiltonian :math:`\hat{H}^{(A)}(t)` is simply the Hamiltonian
of the one-dimensional transverse-field Ising model:

.. math ::
    \hat{H}^{(A)}(t) = \sum_{r=0}^{L-1} \left\{h_{z; r}(t) \hat{\sigma}_{z; r}
    + h_{x; r}(t) \hat{\sigma}_{x; r}\right\} + \sum_{r=0}^{L-2} 
    J_{z, z; r, r+1}(t) \hat{\sigma}_{z; r} \hat{\sigma}_{z; r+1},
    :label: system_TFIM

with :math:`\sigma_{\nu; r}` being the :math:`\nu^{\mathrm{th}}` Pauli operator
acting on site :math:`r`, :math:`h_{z; r}(t)` being the longitudinal field
energy scale for site :math:`r` at time :math:`t`, :math:`h_{x; r}(t)` being the
transverse field energy scale for site :math:`r` at time :math:`t`, 
:math:`J_{z, z; r, r+1}(t)` being the longitudinal coupling energy scale
between sites :math:`r` and :math:`r+1` at time :math:`t`, and :math:`L` being
the number of sites.

This module defines a class for specifying all the model parameters of the 
system, namely the :math:`h_{z; r}(t)`, :math:`h_{x; r}(t)`, and 
:math:`J_{z, z; r, r+1}(t)`.
"""



#####################################
## Load libraries/packages/modules ##
#####################################

# Import class representing time-dependent scalar model parameters.
from sbc.scalar import Scalar



############################
## Authorship information ##
############################

__author__ = "Matthew Fitzpatrick"
__copyright__ = "Copyright 2021"
__credits__ = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__ = "mfitzpatrick@dwavesys.com"
__status__ = "Non-Production"



##################################
## Define classes and functions ##
##################################

# List of public objects in objects.
__all__ = ["Model"]



class Model():
    r"""The system's model parameter set.

    The system Hamiltonian :math:`\hat{H}^{(A)}(t)` is simply the Hamiltonian
    of the one-dimensional transverse-field Ising model:

    .. math ::
        \hat{H}^{(A)}(t) = \sum_{r=0}^{L-1} 
        \left\{h_{z; r}(t) \hat{\sigma}_{z; r}
        + h_{x; r}(t) \hat{\sigma}_{x; r}\right\} + \sum_{r=0}^{L-2} 
        J_{z, z; r, r+1}(t) \hat{\sigma}_{z; r} \hat{\sigma}_{z; r+1},
        :label: system_Model_TFIM

    with :math:`\sigma_{\nu; r}` being the :math:`\nu^{\mathrm{th}}` Pauli 
    operator acting on site :math:`r`, :math:`h_{z; r}(t)` being the 
    longitudinal field energy scale for site :math:`r` at time :math:`t`, 
    :math:`h_{x; r}(t)` being the transverse field energy scale for site 
    :math:`r` at time :math:`t`, :math:`J_{z, z; r, r+1}(t)` being the 
    longitudinal coupling energy scale between sites :math:`r` and :math:`r+1` 
    at time :math:`t`, and :math:`L` being the number of sites. The system
    model parameters refer to the :math:`h_{z; r}(t)`, :math:`h_{x; r}(t)`, and
    :math:`J_{z, z; r, r+1}(t)`.

    Parameters
    ----------
    z_fields : `array_like` (`float` | :class:`sbc.scalar.Scalar`, shape=(``L``,)) | `None`, optional
        The longitudinal field energy scales for a spin chain of size ``L``. If
        ``z_fields`` is an array, then ``z_fields[r]`` is the field energy 
        scale for site ``r``. Note that the field energy scales can be either 
        time-dependent or independent. All time-independent field energy scales 
        are converted to trivial instances of :class:`sbc.scalar.Scalar`. If
        ``z_fields`` is set to `None` (i.e. the default value), then no
        longitudinal fields are applied to the spins.
    x_fields : `array_like` (`float` | :class:`sbc.scalar.Scalar`, shape=(``L``,)) | `None`, optional
        The transverse field energy scales for a spin chain of size ``L``. If
        ``x_fields`` is an array, then ``x_fields[r]`` is the field energy 
        scale for site ``r``. Note that the field energy scales can be either 
        time-dependent or independent. All time-independent field energy scales 
        are converted to trivial instances of :class:`sbc.scalar.Scalar`. If
        ``x_fields`` is set to `None` (i.e. the default value), then no
        transverse fields are applied to the spins.
    zz_couplers : `array_like` (`float` | :class:`sbc.scalar.Scalar`, shape=(``L-1``,)) | `None`, optional
        The longitudinal coupling energy scales for a spin chain of size ``L``.
        If ``zz_couplers[r]`` is an array, then ``zz_couplers[r]`` is the 
        coupling energy scale for sites ``r`` and ``r+1``. Note that the 
        coupling energy scales can be either time-dependent or independent. All 
        time-independent coupling strengths are converted to trivial instances 
        of :class:`sbc.scalar.Scalar`. If ``zz_couplers`` is set to `None`
        (i.e. the default value), then no longitudinal couplers are applied to
        the spins.

    Attributes
    ----------
    z_fields : `array_like` (:class:`sbc.scalar.Scalar`, shape=(``L``,)), read-only
        The longitudinal field energy scales for a spin chain of size ``L``.
        ``z_fields[r]`` is the field energy scale for site ``r``. Note that the 
        field energy scales can be either time-dependent or independent. 
    x_fields : `array_like` (:class:`sbc.scalar.Scalar`, shape=(``L``,)), read-only
        The transverse field energy scales for a spin chain of size ``L``.
        ``x_fields[r]`` is the field energy scale for site ``r``. Note that the 
        field energy scales can be either time-dependent or independent. 
    zz_couplers : `array_like` (:class:`sbc.scalar.Scalar`, shape=(``L-1``,)), read-only
        The longitudinal coupling energy scales for a spin chain of size ``L``.
        ``zz_couplers[r]`` is the coupling energy scales for sites ``r`` and 
        ``r+1``. Note that the coupling energy scales can be either 
        time-dependent or independent. 
    L : `int`, read-only
        The number of sites. This is calculated automatically from ``z_fields``,
        ``x_fields``, and ``zz_couplers``.
    """
    def __init__(self, z_fields=None, x_fields=None, zz_couplers=None):
        self.L = self._determine_L(z_fields, x_fields, zz_couplers)
        self.x_fields = self._construct_attribute(x_fields, self.L)
        self.z_fields = self._construct_attribute(z_fields, self.L)
        self.zz_couplers = self._construct_attribute(zz_couplers, self.L-1)

        self._map_btwn_site_indices_and_unique_x_fields = \
            self._calc_map_btwn_site_indices_and_unique_x_fields()
        
        return None


    
    def _determine_L(self, z_fields, x_fields, zz_couplers):
        candidate_Ls = set()
        if z_fields != None:
            if len(z_fields) != 0:
                candidate_Ls.add(len(z_fields))
        if x_fields != None:
            if len(x_fields) != 0:
                candidate_Ls.add(len(x_fields))
        if zz_couplers != None:
            if len(zz_couplers) != 0:
                candidate_Ls.add(len(zz_couplers)+1)

        if len(candidate_Ls) == 0:
            L = 1
        elif len(candidate_Ls) != 1:
            raise IndexError("Parameters ``z_fields``, ``x_fields``, and "
                             "``zz_couplers`` are of incompatible dimensions.")
        else:
            L = candidate_Ls.pop()

        return L



    def _construct_attribute(self, ctor_param, array_size):
        if ctor_param == None:
            ctor_param = [0] * array_size
        if len(ctor_param) == 0:
            ctor_param = [0] * array_size

        attribute = ctor_param[:]
        elem_already_set = [False] * self.L
        for idx1 in range(0, array_size):
            if not isinstance(attribute[idx1], Scalar):
                attribute[idx1] = Scalar(attribute[idx1])
            for idx2 in range(idx1+1, array_size):
                if ctor_param[idx2] == ctor_param[idx1]:
                    attribute[idx2] = attribute[idx1]
                    elem_already_set[idx2] = True

        return attribute



    def _calc_map_btwn_site_indices_and_unique_x_fields(self):
        result = list(range(self.L))
        for idx1 in range(self.L):
            for idx2 in range(idx1+1, self.L):
                if self.x_fields[idx2] == self.x_fields[idx1]:
                    result[idx2] = result[idx1]

        return result
