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
from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from immich.models.asset_response_dto import AssetResponseDto
from immich.models.on_this_day_dto import OnThisDayDto
from typing import Optional, Set
from typing_extensions import Self

class MemoryResponseDto(BaseModel):
    """
    MemoryResponseDto
    """ # noqa: E501
    assets: List[AssetResponseDto]
    created_at: datetime = Field(alias="createdAt")
    data: OnThisDayDto
    deleted_at: Optional[datetime] = Field(default=None, alias="deletedAt")
    id: StrictStr
    is_saved: StrictBool = Field(alias="isSaved")
    memory_at: datetime = Field(alias="memoryAt")
    owner_id: StrictStr = Field(alias="ownerId")
    seen_at: Optional[datetime] = Field(default=None, alias="seenAt")
    type: StrictStr
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["assets", "createdAt", "data", "deletedAt", "id", "isSaved", "memoryAt", "ownerId", "seenAt", "type", "updatedAt"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['on_this_day']):
            raise ValueError("must be one of enum values ('on_this_day')")
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
        """Create an instance of MemoryResponseDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in assets (list)
        _items = []
        if self.assets:
            for _item in self.assets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assets'] = _items
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MemoryResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assets": [AssetResponseDto.from_dict(_item) for _item in obj["assets"]] if obj.get("assets") is not None else None,
            "createdAt": obj.get("createdAt"),
            "data": OnThisDayDto.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "deletedAt": obj.get("deletedAt"),
            "id": obj.get("id"),
            "isSaved": obj.get("isSaved"),
            "memoryAt": obj.get("memoryAt"),
            "ownerId": obj.get("ownerId"),
            "seenAt": obj.get("seenAt"),
            "type": obj.get("type"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


