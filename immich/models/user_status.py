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


class UserStatus(str, Enum):
    """
    UserStatus
    """

    """
    allowed enum values
    """
    ACTIVE = 'active'
    REMOVING = 'removing'
    DELETED = 'deleted'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserStatus from a JSON string"""
        return cls(json.loads(json_str))


