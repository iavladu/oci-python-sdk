# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntitySummary(object):
    """
    Summary of an data entity. A representation of data with a set of attributes, normally representing a single
    business entity. Synonymous with 'table' or 'view' in a database, or a single logical file structure
    that one or many files may match.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this EntitySummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this EntitySummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this EntitySummary.
        :type description: str

        :param data_asset_key:
            The value to assign to the data_asset_key property of this EntitySummary.
        :type data_asset_key: str

        :param folder_key:
            The value to assign to the folder_key property of this EntitySummary.
        :type folder_key: str

        :param external_key:
            The value to assign to the external_key property of this EntitySummary.
        :type external_key: str

        :param path:
            The value to assign to the path property of this EntitySummary.
        :type path: str

        :param time_created:
            The value to assign to the time_created property of this EntitySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EntitySummary.
        :type time_updated: datetime

        :param updated_by_id:
            The value to assign to the updated_by_id property of this EntitySummary.
        :type updated_by_id: str

        :param uri:
            The value to assign to the uri property of this EntitySummary.
        :type uri: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EntitySummary.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'data_asset_key': 'str',
            'folder_key': 'str',
            'external_key': 'str',
            'path': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'updated_by_id': 'str',
            'uri': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'data_asset_key': 'dataAssetKey',
            'folder_key': 'folderKey',
            'external_key': 'externalKey',
            'path': 'path',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'updated_by_id': 'updatedById',
            'uri': 'uri',
            'lifecycle_state': 'lifecycleState'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._data_asset_key = None
        self._folder_key = None
        self._external_key = None
        self._path = None
        self._time_created = None
        self._time_updated = None
        self._updated_by_id = None
        self._uri = None
        self._lifecycle_state = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this EntitySummary.
        Unique data entity key that is immutable.


        :return: The key of this EntitySummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this EntitySummary.
        Unique data entity key that is immutable.


        :param key: The key of this EntitySummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this EntitySummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this EntitySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EntitySummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this EntitySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this EntitySummary.
        Detailed description of a data entity.


        :return: The description of this EntitySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EntitySummary.
        Detailed description of a data entity.


        :param description: The description of this EntitySummary.
        :type: str
        """
        self._description = description

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this EntitySummary.
        Unique key of the parent data asset.


        :return: The data_asset_key of this EntitySummary.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this EntitySummary.
        Unique key of the parent data asset.


        :param data_asset_key: The data_asset_key of this EntitySummary.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def folder_key(self):
        """
        Gets the folder_key of this EntitySummary.
        Key of the associated folder.


        :return: The folder_key of this EntitySummary.
        :rtype: str
        """
        return self._folder_key

    @folder_key.setter
    def folder_key(self, folder_key):
        """
        Sets the folder_key of this EntitySummary.
        Key of the associated folder.


        :param folder_key: The folder_key of this EntitySummary.
        :type: str
        """
        self._folder_key = folder_key

    @property
    def external_key(self):
        """
        Gets the external_key of this EntitySummary.
        Unique external key of this object in the source system.


        :return: The external_key of this EntitySummary.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this EntitySummary.
        Unique external key of this object in the source system.


        :param external_key: The external_key of this EntitySummary.
        :type: str
        """
        self._external_key = external_key

    @property
    def path(self):
        """
        Gets the path of this EntitySummary.
        Full path of the data entity.


        :return: The path of this EntitySummary.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this EntitySummary.
        Full path of the data entity.


        :param path: The path of this EntitySummary.
        :type: str
        """
        self._path = path

    @property
    def time_created(self):
        """
        Gets the time_created of this EntitySummary.
        The date and time the data entity was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this EntitySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EntitySummary.
        The date and time the data entity was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this EntitySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EntitySummary.
        The last time that any change was made to the data entity. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this EntitySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EntitySummary.
        The last time that any change was made to the data entity. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this EntitySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this EntitySummary.
        OCID of the user who updated this object in the data catalog.


        :return: The updated_by_id of this EntitySummary.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this EntitySummary.
        OCID of the user who updated this object in the data catalog.


        :param updated_by_id: The updated_by_id of this EntitySummary.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def uri(self):
        """
        Gets the uri of this EntitySummary.
        URI to the data entity instance in the API.


        :return: The uri of this EntitySummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this EntitySummary.
        URI to the data entity instance in the API.


        :param uri: The uri of this EntitySummary.
        :type: str
        """
        self._uri = uri

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this EntitySummary.
        State of the data entity.


        :return: The lifecycle_state of this EntitySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EntitySummary.
        State of the data entity.


        :param lifecycle_state: The lifecycle_state of this EntitySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
