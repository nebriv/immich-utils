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


class TimeBucketSize(str, Enum):
    """
    TimeBucketSize
    """

    """
    allowed enum values
    """
    DAY = 'DAY'
    MONTH = 'MONTH'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TimeBucketSize from a JSON string"""
        return cls(json.loads(json_str))


