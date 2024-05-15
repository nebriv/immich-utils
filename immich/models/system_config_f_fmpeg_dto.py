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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from immich.models.audio_codec import AudioCodec
from immich.models.cq_mode import CQMode
from immich.models.tone_mapping import ToneMapping
from immich.models.transcode_hw_accel import TranscodeHWAccel
from immich.models.transcode_policy import TranscodePolicy
from immich.models.video_codec import VideoCodec
from typing import Optional, Set
from typing_extensions import Self

class SystemConfigFFmpegDto(BaseModel):
    """
    SystemConfigFFmpegDto
    """ # noqa: E501
    accel: TranscodeHWAccel
    accepted_audio_codecs: List[AudioCodec] = Field(alias="acceptedAudioCodecs")
    accepted_video_codecs: List[VideoCodec] = Field(alias="acceptedVideoCodecs")
    bframes: Annotated[int, Field(le=16, strict=True, ge=-1)]
    cq_mode: CQMode = Field(alias="cqMode")
    crf: Annotated[int, Field(le=51, strict=True, ge=0)]
    gop_size: Annotated[int, Field(strict=True, ge=0)] = Field(alias="gopSize")
    max_bitrate: StrictStr = Field(alias="maxBitrate")
    npl: Annotated[int, Field(strict=True, ge=0)]
    preferred_hw_device: StrictStr = Field(alias="preferredHwDevice")
    preset: StrictStr
    refs: Annotated[int, Field(le=6, strict=True, ge=0)]
    target_audio_codec: AudioCodec = Field(alias="targetAudioCodec")
    target_resolution: StrictStr = Field(alias="targetResolution")
    target_video_codec: VideoCodec = Field(alias="targetVideoCodec")
    temporal_aq: StrictBool = Field(alias="temporalAQ")
    threads: Annotated[int, Field(strict=True, ge=0)]
    tonemap: ToneMapping
    transcode: TranscodePolicy
    two_pass: StrictBool = Field(alias="twoPass")
    __properties: ClassVar[List[str]] = ["accel", "acceptedAudioCodecs", "acceptedVideoCodecs", "bframes", "cqMode", "crf", "gopSize", "maxBitrate", "npl", "preferredHwDevice", "preset", "refs", "targetAudioCodec", "targetResolution", "targetVideoCodec", "temporalAQ", "threads", "tonemap", "transcode", "twoPass"]

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
        """Create an instance of SystemConfigFFmpegDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemConfigFFmpegDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accel": obj.get("accel"),
            "acceptedAudioCodecs": obj.get("acceptedAudioCodecs"),
            "acceptedVideoCodecs": obj.get("acceptedVideoCodecs"),
            "bframes": obj.get("bframes"),
            "cqMode": obj.get("cqMode"),
            "crf": obj.get("crf"),
            "gopSize": obj.get("gopSize"),
            "maxBitrate": obj.get("maxBitrate"),
            "npl": obj.get("npl"),
            "preferredHwDevice": obj.get("preferredHwDevice"),
            "preset": obj.get("preset"),
            "refs": obj.get("refs"),
            "targetAudioCodec": obj.get("targetAudioCodec"),
            "targetResolution": obj.get("targetResolution"),
            "targetVideoCodec": obj.get("targetVideoCodec"),
            "temporalAQ": obj.get("temporalAQ"),
            "threads": obj.get("threads"),
            "tonemap": obj.get("tonemap"),
            "transcode": obj.get("transcode"),
            "twoPass": obj.get("twoPass")
        })
        return _obj

