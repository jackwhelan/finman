"""
This module is where custom exceptions for this microservice are housed.
"""
class AccountOperatorException(Exception):
    """
    This exception is for any database related errors.
    """

class CreatePersonException(Exception):
    """
    This exception is for any Person creation related errors.
    """

class CreateLiabilityException(Exception):
    """
    This exception is for any Liability creation related errors.
    """

class CreateAssetException(Exception):
    """
    This exception is for any Asset creation related errors.
    """
