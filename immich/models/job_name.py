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


class JobName(str, Enum):
    """
    JobName
    """

    """
    allowed enum values
    """
    THUMBNAILGENERATION = 'thumbnailGeneration'
    METADATAEXTRACTION = 'metadataExtraction'
    VIDEOCONVERSION = 'videoConversion'
    FACEDETECTION = 'faceDetection'
    FACIALRECOGNITION = 'facialRecognition'
    SMARTSEARCH = 'smartSearch'
    BACKGROUNDTASK = 'backgroundTask'
    STORAGETEMPLATEMIGRATION = 'storageTemplateMigration'
    MIGRATION = 'migration'
    SEARCH = 'search'
    SIDECAR = 'sidecar'
    LIBRARY = 'library'
    NOTIFICATIONS = 'notifications'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobName from a JSON string"""
        return cls(json.loads(json_str))

