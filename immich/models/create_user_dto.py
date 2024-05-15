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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateUserDto(BaseModel):
    """
    CreateUserDto
    """ # noqa: E501
    email: StrictStr
    memories_enabled: Optional[StrictBool] = Field(default=None, alias="memoriesEnabled")
    name: StrictStr
    notify: Optional[StrictBool] = None
    password: StrictStr
    quota_size_in_bytes: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, alias="quotaSizeInBytes")
    should_change_password: Optional[StrictBool] = Field(default=None, alias="shouldChangePassword")
    storage_label: Optional[StrictStr] = Field(default=None, alias="storageLabel")
    __properties: ClassVar[List[str]] = ["email", "memoriesEnabled", "name", "notify", "password", "quotaSizeInBytes", "shouldChangePassword", "storageLabel"]

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
        """Create an instance of CreateUserDto from a JSON string"""
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

        # set to None if storage_label (nullable) is None
        # and model_fields_set contains the field
        if self.storage_label is None and "storage_label" in self.model_fields_set:
            _dict['storageLabel'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateUserDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "memoriesEnabled": obj.get("memoriesEnabled"),
            "name": obj.get("name"),
            "notify": obj.get("notify"),
            "password": obj.get("password"),
            "quotaSizeInBytes": obj.get("quotaSizeInBytes"),
            "shouldChangePassword": obj.get("shouldChangePassword"),
            "storageLabel": obj.get("storageLabel")
        })
        return _obj

