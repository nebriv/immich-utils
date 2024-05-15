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

from datetime import datetime
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from immich.models.user_dto import UserDto
from typing import Optional, Set
from typing_extensions import Self

class ActivityResponseDto(BaseModel):
    """
    ActivityResponseDto
    """ # noqa: E501
    asset_id: Optional[StrictStr] = Field(alias="assetId")
    comment: Optional[StrictStr] = None
    created_at: datetime = Field(alias="createdAt")
    id: StrictStr
    type: StrictStr
    user: UserDto
    __properties: ClassVar[List[str]] = ["assetId", "comment", "createdAt", "id", "type", "user"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['comment', 'like']):
            raise ValueError("must be one of enum values ('comment', 'like')")
        return value

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
        """Create an instance of ActivityResponseDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if asset_id (nullable) is None
        # and model_fields_set contains the field
        if self.asset_id is None and "asset_id" in self.model_fields_set:
            _dict['assetId'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActivityResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assetId": obj.get("assetId"),
            "comment": obj.get("comment"),
            "createdAt": obj.get("createdAt"),
            "id": obj.get("id"),
            "type": obj.get("type"),
            "user": UserDto.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


