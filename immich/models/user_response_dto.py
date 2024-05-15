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
from immich.models.user_avatar_color import UserAvatarColor
from immich.models.user_status import UserStatus
from typing import Optional, Set
from typing_extensions import Self

class UserResponseDto(BaseModel):
    """
    UserResponseDto
    """ # noqa: E501
    avatar_color: UserAvatarColor = Field(alias="avatarColor")
    created_at: datetime = Field(alias="createdAt")
    deleted_at: Optional[datetime] = Field(alias="deletedAt")
    email: StrictStr
    id: StrictStr
    is_admin: StrictBool = Field(alias="isAdmin")
    memories_enabled: Optional[StrictBool] = Field(default=None, alias="memoriesEnabled")
    name: StrictStr
    oauth_id: StrictStr = Field(alias="oauthId")
    profile_image_path: StrictStr = Field(alias="profileImagePath")
    quota_size_in_bytes: Optional[StrictInt] = Field(alias="quotaSizeInBytes")
    quota_usage_in_bytes: Optional[StrictInt] = Field(alias="quotaUsageInBytes")
    should_change_password: StrictBool = Field(alias="shouldChangePassword")
    status: UserStatus
    storage_label: Optional[StrictStr] = Field(alias="storageLabel")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["avatarColor", "createdAt", "deletedAt", "email", "id", "isAdmin", "memoriesEnabled", "name", "oauthId", "profileImagePath", "quotaSizeInBytes", "quotaUsageInBytes", "shouldChangePassword", "status", "storageLabel", "updatedAt"]

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
        """Create an instance of UserResponseDto from a JSON string"""
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
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deletedAt'] = None

        # set to None if quota_size_in_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.quota_size_in_bytes is None and "quota_size_in_bytes" in self.model_fields_set:
            _dict['quotaSizeInBytes'] = None

        # set to None if quota_usage_in_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.quota_usage_in_bytes is None and "quota_usage_in_bytes" in self.model_fields_set:
            _dict['quotaUsageInBytes'] = None

        # set to None if storage_label (nullable) is None
        # and model_fields_set contains the field
        if self.storage_label is None and "storage_label" in self.model_fields_set:
            _dict['storageLabel'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avatarColor": obj.get("avatarColor"),
            "createdAt": obj.get("createdAt"),
            "deletedAt": obj.get("deletedAt"),
            "email": obj.get("email"),
            "id": obj.get("id"),
            "isAdmin": obj.get("isAdmin"),
            "memoriesEnabled": obj.get("memoriesEnabled"),
            "name": obj.get("name"),
            "oauthId": obj.get("oauthId"),
            "profileImagePath": obj.get("profileImagePath"),
            "quotaSizeInBytes": obj.get("quotaSizeInBytes"),
            "quotaUsageInBytes": obj.get("quotaUsageInBytes"),
            "shouldChangePassword": obj.get("shouldChangePassword"),
            "status": obj.get("status"),
            "storageLabel": obj.get("storageLabel"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj

