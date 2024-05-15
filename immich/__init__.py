# coding: utf-8

# flake8: noqa

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from immich.api.api_key_api import APIKeyApi
from immich.api.activity_api import ActivityApi
from immich.api.album_api import AlbumApi
from immich.api.asset_api import AssetApi
from immich.api.audit_api import AuditApi
from immich.api.authentication_api import AuthenticationApi
from immich.api.download_api import DownloadApi
from immich.api.face_api import FaceApi
from immich.api.file_report_api import FileReportApi
from immich.api.job_api import JobApi
from immich.api.library_api import LibraryApi
from immich.api.memory_api import MemoryApi
from immich.api.o_auth_api import OAuthApi
from immich.api.partner_api import PartnerApi
from immich.api.person_api import PersonApi
from immich.api.search_api import SearchApi
from immich.api.server_info_api import ServerInfoApi
from immich.api.sessions_api import SessionsApi
from immich.api.shared_link_api import SharedLinkApi
from immich.api.sync_api import SyncApi
from immich.api.system_config_api import SystemConfigApi
from immich.api.system_metadata_api import SystemMetadataApi
from immich.api.tag_api import TagApi
from immich.api.timeline_api import TimelineApi
from immich.api.trash_api import TrashApi
from immich.api.user_api import UserApi

# import ApiClient
from immich.api_response import ApiResponse
from immich.api_client import ApiClient
from immich.configuration import Configuration
from immich.exceptions import OpenApiException
from immich.exceptions import ApiTypeError
from immich.exceptions import ApiValueError
from immich.exceptions import ApiKeyError
from immich.exceptions import ApiAttributeError
from immich.exceptions import ApiException

# import models into sdk package
from immich.models.api_key_create_dto import APIKeyCreateDto
from immich.models.api_key_create_response_dto import APIKeyCreateResponseDto
from immich.models.api_key_response_dto import APIKeyResponseDto
from immich.models.api_key_update_dto import APIKeyUpdateDto
from immich.models.activity_create_dto import ActivityCreateDto
from immich.models.activity_response_dto import ActivityResponseDto
from immich.models.activity_statistics_response_dto import ActivityStatisticsResponseDto
from immich.models.add_users_dto import AddUsersDto
from immich.models.admin_onboarding_update_dto import AdminOnboardingUpdateDto
from immich.models.album_count_response_dto import AlbumCountResponseDto
from immich.models.album_response_dto import AlbumResponseDto
from immich.models.album_user_add_dto import AlbumUserAddDto
from immich.models.album_user_create_dto import AlbumUserCreateDto
from immich.models.album_user_response_dto import AlbumUserResponseDto
from immich.models.album_user_role import AlbumUserRole
from immich.models.all_job_status_response_dto import AllJobStatusResponseDto
from immich.models.asset_bulk_delete_dto import AssetBulkDeleteDto
from immich.models.asset_bulk_update_dto import AssetBulkUpdateDto
from immich.models.asset_bulk_upload_check_dto import AssetBulkUploadCheckDto
from immich.models.asset_bulk_upload_check_item import AssetBulkUploadCheckItem
from immich.models.asset_bulk_upload_check_response_dto import AssetBulkUploadCheckResponseDto
from immich.models.asset_bulk_upload_check_result import AssetBulkUploadCheckResult
from immich.models.asset_delta_sync_dto import AssetDeltaSyncDto
from immich.models.asset_delta_sync_response_dto import AssetDeltaSyncResponseDto
from immich.models.asset_face_response_dto import AssetFaceResponseDto
from immich.models.asset_face_update_dto import AssetFaceUpdateDto
from immich.models.asset_face_update_item import AssetFaceUpdateItem
from immich.models.asset_face_without_person_response_dto import AssetFaceWithoutPersonResponseDto
from immich.models.asset_file_upload_response_dto import AssetFileUploadResponseDto
from immich.models.asset_full_sync_dto import AssetFullSyncDto
from immich.models.asset_ids_dto import AssetIdsDto
from immich.models.asset_ids_response_dto import AssetIdsResponseDto
from immich.models.asset_job_name import AssetJobName
from immich.models.asset_jobs_dto import AssetJobsDto
from immich.models.asset_order import AssetOrder
from immich.models.asset_response_dto import AssetResponseDto
from immich.models.asset_stats_response_dto import AssetStatsResponseDto
from immich.models.asset_type_enum import AssetTypeEnum
from immich.models.audio_codec import AudioCodec
from immich.models.audit_deletes_response_dto import AuditDeletesResponseDto
from immich.models.bulk_id_response_dto import BulkIdResponseDto
from immich.models.bulk_ids_dto import BulkIdsDto
from immich.models.clip_config import CLIPConfig
from immich.models.clip_mode import CLIPMode
from immich.models.cq_mode import CQMode
from immich.models.change_password_dto import ChangePasswordDto
from immich.models.check_existing_assets_dto import CheckExistingAssetsDto
from immich.models.check_existing_assets_response_dto import CheckExistingAssetsResponseDto
from immich.models.colorspace import Colorspace
from immich.models.create_album_dto import CreateAlbumDto
from immich.models.create_library_dto import CreateLibraryDto
from immich.models.create_profile_image_response_dto import CreateProfileImageResponseDto
from immich.models.create_tag_dto import CreateTagDto
from immich.models.create_user_dto import CreateUserDto
from immich.models.delete_user_dto import DeleteUserDto
from immich.models.download_archive_info import DownloadArchiveInfo
from immich.models.download_info_dto import DownloadInfoDto
from immich.models.download_response_dto import DownloadResponseDto
from immich.models.entity_type import EntityType
from immich.models.exif_response_dto import ExifResponseDto
from immich.models.face_dto import FaceDto
from immich.models.file_checksum_dto import FileChecksumDto
from immich.models.file_checksum_response_dto import FileChecksumResponseDto
from immich.models.file_report_dto import FileReportDto
from immich.models.file_report_fix_dto import FileReportFixDto
from immich.models.file_report_item_dto import FileReportItemDto
from immich.models.image_format import ImageFormat
from immich.models.job_command import JobCommand
from immich.models.job_command_dto import JobCommandDto
from immich.models.job_counts_dto import JobCountsDto
from immich.models.job_name import JobName
from immich.models.job_settings_dto import JobSettingsDto
from immich.models.job_status_dto import JobStatusDto
from immich.models.library_response_dto import LibraryResponseDto
from immich.models.library_stats_response_dto import LibraryStatsResponseDto
from immich.models.library_type import LibraryType
from immich.models.log_level import LogLevel
from immich.models.login_credential_dto import LoginCredentialDto
from immich.models.login_response_dto import LoginResponseDto
from immich.models.logout_response_dto import LogoutResponseDto
from immich.models.map_marker_response_dto import MapMarkerResponseDto
from immich.models.map_theme import MapTheme
from immich.models.memory_create_dto import MemoryCreateDto
from immich.models.memory_lane_response_dto import MemoryLaneResponseDto
from immich.models.memory_response_dto import MemoryResponseDto
from immich.models.memory_type import MemoryType
from immich.models.memory_update_dto import MemoryUpdateDto
from immich.models.merge_person_dto import MergePersonDto
from immich.models.metadata_search_dto import MetadataSearchDto
from immich.models.model_type import ModelType
from immich.models.o_auth_authorize_response_dto import OAuthAuthorizeResponseDto
from immich.models.o_auth_callback_dto import OAuthCallbackDto
from immich.models.o_auth_config_dto import OAuthConfigDto
from immich.models.on_this_day_dto import OnThisDayDto
from immich.models.partner_response_dto import PartnerResponseDto
from immich.models.path_entity_type import PathEntityType
from immich.models.path_type import PathType
from immich.models.people_response_dto import PeopleResponseDto
from immich.models.people_update_dto import PeopleUpdateDto
from immich.models.people_update_item import PeopleUpdateItem
from immich.models.person_create_dto import PersonCreateDto
from immich.models.person_response_dto import PersonResponseDto
from immich.models.person_statistics_response_dto import PersonStatisticsResponseDto
from immich.models.person_update_dto import PersonUpdateDto
from immich.models.person_with_faces_response_dto import PersonWithFacesResponseDto
from immich.models.places_response_dto import PlacesResponseDto
from immich.models.queue_status_dto import QueueStatusDto
from immich.models.reaction_level import ReactionLevel
from immich.models.reaction_type import ReactionType
from immich.models.recognition_config import RecognitionConfig
from immich.models.reverse_geocoding_state_response_dto import ReverseGeocodingStateResponseDto
from immich.models.scan_library_dto import ScanLibraryDto
from immich.models.search_album_response_dto import SearchAlbumResponseDto
from immich.models.search_asset_response_dto import SearchAssetResponseDto
from immich.models.search_explore_item import SearchExploreItem
from immich.models.search_explore_response_dto import SearchExploreResponseDto
from immich.models.search_facet_count_response_dto import SearchFacetCountResponseDto
from immich.models.search_facet_response_dto import SearchFacetResponseDto
from immich.models.search_response_dto import SearchResponseDto
from immich.models.search_suggestion_type import SearchSuggestionType
from immich.models.server_config_dto import ServerConfigDto
from immich.models.server_features_dto import ServerFeaturesDto
from immich.models.server_info_response_dto import ServerInfoResponseDto
from immich.models.server_media_types_response_dto import ServerMediaTypesResponseDto
from immich.models.server_ping_response import ServerPingResponse
from immich.models.server_stats_response_dto import ServerStatsResponseDto
from immich.models.server_theme_dto import ServerThemeDto
from immich.models.server_version_response_dto import ServerVersionResponseDto
from immich.models.session_response_dto import SessionResponseDto
from immich.models.shared_link_create_dto import SharedLinkCreateDto
from immich.models.shared_link_edit_dto import SharedLinkEditDto
from immich.models.shared_link_response_dto import SharedLinkResponseDto
from immich.models.shared_link_type import SharedLinkType
from immich.models.sign_up_dto import SignUpDto
from immich.models.smart_info_response_dto import SmartInfoResponseDto
from immich.models.smart_search_dto import SmartSearchDto
from immich.models.system_config_dto import SystemConfigDto
from immich.models.system_config_f_fmpeg_dto import SystemConfigFFmpegDto
from immich.models.system_config_image_dto import SystemConfigImageDto
from immich.models.system_config_job_dto import SystemConfigJobDto
from immich.models.system_config_library_dto import SystemConfigLibraryDto
from immich.models.system_config_library_scan_dto import SystemConfigLibraryScanDto
from immich.models.system_config_library_watch_dto import SystemConfigLibraryWatchDto
from immich.models.system_config_logging_dto import SystemConfigLoggingDto
from immich.models.system_config_machine_learning_dto import SystemConfigMachineLearningDto
from immich.models.system_config_map_dto import SystemConfigMapDto
from immich.models.system_config_new_version_check_dto import SystemConfigNewVersionCheckDto
from immich.models.system_config_notifications_dto import SystemConfigNotificationsDto
from immich.models.system_config_o_auth_dto import SystemConfigOAuthDto
from immich.models.system_config_password_login_dto import SystemConfigPasswordLoginDto
from immich.models.system_config_reverse_geocoding_dto import SystemConfigReverseGeocodingDto
from immich.models.system_config_server_dto import SystemConfigServerDto
from immich.models.system_config_smtp_dto import SystemConfigSmtpDto
from immich.models.system_config_smtp_transport_dto import SystemConfigSmtpTransportDto
from immich.models.system_config_storage_template_dto import SystemConfigStorageTemplateDto
from immich.models.system_config_template_storage_option_dto import SystemConfigTemplateStorageOptionDto
from immich.models.system_config_theme_dto import SystemConfigThemeDto
from immich.models.system_config_trash_dto import SystemConfigTrashDto
from immich.models.system_config_user_dto import SystemConfigUserDto
from immich.models.tag_response_dto import TagResponseDto
from immich.models.tag_type_enum import TagTypeEnum
from immich.models.thumbnail_format import ThumbnailFormat
from immich.models.time_bucket_response_dto import TimeBucketResponseDto
from immich.models.time_bucket_size import TimeBucketSize
from immich.models.tone_mapping import ToneMapping
from immich.models.transcode_hw_accel import TranscodeHWAccel
from immich.models.transcode_policy import TranscodePolicy
from immich.models.update_album_dto import UpdateAlbumDto
from immich.models.update_album_user_dto import UpdateAlbumUserDto
from immich.models.update_asset_dto import UpdateAssetDto
from immich.models.update_library_dto import UpdateLibraryDto
from immich.models.update_partner_dto import UpdatePartnerDto
from immich.models.update_stack_parent_dto import UpdateStackParentDto
from immich.models.update_tag_dto import UpdateTagDto
from immich.models.update_user_dto import UpdateUserDto
from immich.models.usage_by_user_dto import UsageByUserDto
from immich.models.user_avatar_color import UserAvatarColor
from immich.models.user_dto import UserDto
from immich.models.user_response_dto import UserResponseDto
from immich.models.user_status import UserStatus
from immich.models.validate_access_token_response_dto import ValidateAccessTokenResponseDto
from immich.models.validate_library_dto import ValidateLibraryDto
from immich.models.validate_library_import_path_response_dto import ValidateLibraryImportPathResponseDto
from immich.models.validate_library_response_dto import ValidateLibraryResponseDto
from immich.models.video_codec import VideoCodec