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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from immich.models.album_user_response_dto import AlbumUserResponseDto
from immich.models.asset_order import AssetOrder
from immich.models.asset_response_dto import AssetResponseDto
from immich.models.user_response_dto import UserResponseDto
from typing import Optional, Set
from typing_extensions import Self

class AlbumResponseDto(BaseModel):
    """
    AlbumResponseDto
    """ # noqa: E501
    album_name: StrictStr = Field(alias="albumName")
    album_thumbnail_asset_id: Optional[StrictStr] = Field(alias="albumThumbnailAssetId")
    album_users: List[AlbumUserResponseDto] = Field(alias="albumUsers")
    asset_count: StrictInt = Field(alias="assetCount")
    assets: List[AssetResponseDto]
    created_at: datetime = Field(alias="createdAt")
    description: StrictStr
    end_date: Optional[datetime] = Field(default=None, alias="endDate")
    has_shared_link: StrictBool = Field(alias="hasSharedLink")
    id: StrictStr
    is_activity_enabled: StrictBool = Field(alias="isActivityEnabled")
    last_modified_asset_timestamp: Optional[datetime] = Field(default=None, alias="lastModifiedAssetTimestamp")
    order: Optional[AssetOrder] = None
    owner: UserResponseDto
    owner_id: StrictStr = Field(alias="ownerId")
    shared: StrictBool
    shared_users: List[UserResponseDto] = Field(description="This property was deprecated in v1.102.0", alias="sharedUsers")
    start_date: Optional[datetime] = Field(default=None, alias="startDate")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["albumName", "albumThumbnailAssetId", "albumUsers", "assetCount", "assets", "createdAt", "description", "endDate", "hasSharedLink", "id", "isActivityEnabled", "lastModifiedAssetTimestamp", "order", "owner", "ownerId", "shared", "sharedUsers", "startDate", "updatedAt"]

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
        """Create an instance of AlbumResponseDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in album_users (list)
        _items = []
        if self.album_users:
            for _item in self.album_users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['albumUsers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in assets (list)
        _items = []
        if self.assets:
            for _item in self.assets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assets'] = _items
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shared_users (list)
        _items = []
        if self.shared_users:
            for _item in self.shared_users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sharedUsers'] = _items
        # set to None if album_thumbnail_asset_id (nullable) is None
        # and model_fields_set contains the field
        if self.album_thumbnail_asset_id is None and "album_thumbnail_asset_id" in self.model_fields_set:
            _dict['albumThumbnailAssetId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlbumResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "albumName": obj.get("albumName"),
            "albumThumbnailAssetId": obj.get("albumThumbnailAssetId"),
            "albumUsers": [AlbumUserResponseDto.from_dict(_item) for _item in obj["albumUsers"]] if obj.get("albumUsers") is not None else None,
            "assetCount": obj.get("assetCount"),
            "assets": [AssetResponseDto.from_dict(_item) for _item in obj["assets"]] if obj.get("assets") is not None else None,
            "createdAt": obj.get("createdAt"),
            "description": obj.get("description"),
            "endDate": obj.get("endDate"),
            "hasSharedLink": obj.get("hasSharedLink"),
            "id": obj.get("id"),
            "isActivityEnabled": obj.get("isActivityEnabled"),
            "lastModifiedAssetTimestamp": obj.get("lastModifiedAssetTimestamp"),
            "order": obj.get("order"),
            "owner": UserResponseDto.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "ownerId": obj.get("ownerId"),
            "shared": obj.get("shared"),
            "sharedUsers": [UserResponseDto.from_dict(_item) for _item in obj["sharedUsers"]] if obj.get("sharedUsers") is not None else None,
            "startDate": obj.get("startDate"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj

