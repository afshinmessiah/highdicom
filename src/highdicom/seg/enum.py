"""Enumerate values specific to Segmentation IODs."""
from enum import Enum


class SegmentAlgorithmTypes(Enum):

    """Enumerated values for attribute Segment Algorithm Type."""

    AUTOMATIC = 'AUTOMATIC'
    SEMIAUTOMATIC = 'SEMIAUTOMATIC'
    MANUAL = 'MANUAL'


class SegmentationTypes(Enum):

    """Enumerated values for attribute Segmentation Type."""

    BINARY = 'BINARY'
    FRACTIONAL = 'FRACTIONAL'


class SegmentationFractionalTypes(Enum):

    """Enumerated values for attribute Segmentation Fractional Type."""

    PROBABILITY = 'PROBABILITY'
    OCCUPANCY = 'OCCUPANCY'


class SpatialLocationsPreserved(Enum):

    """Enumerated values for attribute Spatial Locations Preserved."""

    YES = 'YES'
    NO = 'NO'
    REORIENTED_ONLY = 'REORIENTED_ONLY'
