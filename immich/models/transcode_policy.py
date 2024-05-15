# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TranscodePolicy(str, Enum):
    """
    TranscodePolicy
    """

    """
    allowed enum values
    """
    ALL = 'all'
    OPTIMAL = 'optimal'
    BITRATE = 'bitrate'
    REQUIRED = 'required'
    DISABLED = 'disabled'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TranscodePolicy from a JSON string"""
        return cls(json.loads(json_str))

