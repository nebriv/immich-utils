# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UsageByUserDto(BaseModel):
    """
    UsageByUserDto
    """ # noqa: E501
    photos: StrictInt
    quota_size_in_bytes: Optional[StrictInt] = Field(alias="quotaSizeInBytes")
    usage: StrictInt
    user_id: StrictStr = Field(alias="userId")
    user_name: StrictStr = Field(alias="userName")
    videos: StrictInt
    __properties: ClassVar[List[str]] = ["photos", "quotaSizeInBytes", "usage", "userId", "userName", "videos"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UsageByUserDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if quota_size_in_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.quota_size_in_bytes is None and "quota_size_in_bytes" in self.model_fields_set:
            _dict['quotaSizeInBytes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsageByUserDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "photos": obj.get("photos"),
            "quotaSizeInBytes": obj.get("quotaSizeInBytes"),
            "usage": obj.get("usage"),
            "userId": obj.get("userId"),
            "userName": obj.get("userName"),
            "videos": obj.get("videos")
        })
        return _obj


