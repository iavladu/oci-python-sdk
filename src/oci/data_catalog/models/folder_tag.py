# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FolderTag(object):
    """
    Represents an association of a folder to a term.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FolderTag object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param folder_key:
            The value to assign to the folder_key property of this FolderTag.
        :type folder_key: str

        :param key:
            The value to assign to the key property of this FolderTag.
        :type key: str

        :param name:
            The value to assign to the name property of this FolderTag.
        :type name: str

        :param term_key:
            The value to assign to the term_key property of this FolderTag.
        :type term_key: str

        :param term_path:
            The value to assign to the term_path property of this FolderTag.
        :type term_path: str

        :param term_description:
            The value to assign to the term_description property of this FolderTag.
        :type term_description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FolderTag.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this FolderTag.
        :type time_created: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this FolderTag.
        :type created_by_id: str

        :param uri:
            The value to assign to the uri property of this FolderTag.
        :type uri: str

        """
        self.swagger_types = {
            'folder_key': 'str',
            'key': 'str',
            'name': 'str',
            'term_key': 'str',
            'term_path': 'str',
            'term_description': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'created_by_id': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'folder_key': 'folderKey',
            'key': 'key',
            'name': 'name',
            'term_key': 'termKey',
            'term_path': 'termPath',
            'term_description': 'termDescription',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'created_by_id': 'createdById',
            'uri': 'uri'
        }

        self._folder_key = None
        self._key = None
        self._name = None
        self._term_key = None
        self._term_path = None
        self._term_description = None
        self._lifecycle_state = None
        self._time_created = None
        self._created_by_id = None
        self._uri = None

    @property
    def folder_key(self):
        """
        Gets the folder_key of this FolderTag.
        The unique key of the folder associated with this tag.


        :return: The folder_key of this FolderTag.
        :rtype: str
        """
        return self._folder_key

    @folder_key.setter
    def folder_key(self, folder_key):
        """
        Sets the folder_key of this FolderTag.
        The unique key of the folder associated with this tag.


        :param folder_key: The folder_key of this FolderTag.
        :type: str
        """
        self._folder_key = folder_key

    @property
    def key(self):
        """
        **[Required]** Gets the key of this FolderTag.
        Unique tag key that is immutable.


        :return: The key of this FolderTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FolderTag.
        Unique tag key that is immutable.


        :param key: The key of this FolderTag.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this FolderTag.
        Name of the tag which matches the term name.


        :return: The name of this FolderTag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FolderTag.
        Name of the tag which matches the term name.


        :param name: The name of this FolderTag.
        :type: str
        """
        self._name = name

    @property
    def term_key(self):
        """
        Gets the term_key of this FolderTag.
        Unique key of the related term.


        :return: The term_key of this FolderTag.
        :rtype: str
        """
        return self._term_key

    @term_key.setter
    def term_key(self, term_key):
        """
        Sets the term_key of this FolderTag.
        Unique key of the related term.


        :param term_key: The term_key of this FolderTag.
        :type: str
        """
        self._term_key = term_key

    @property
    def term_path(self):
        """
        Gets the term_path of this FolderTag.
        Path of the related term.


        :return: The term_path of this FolderTag.
        :rtype: str
        """
        return self._term_path

    @term_path.setter
    def term_path(self, term_path):
        """
        Sets the term_path of this FolderTag.
        Path of the related term.


        :param term_path: The term_path of this FolderTag.
        :type: str
        """
        self._term_path = term_path

    @property
    def term_description(self):
        """
        Gets the term_description of this FolderTag.
        Description of the related term.


        :return: The term_description of this FolderTag.
        :rtype: str
        """
        return self._term_description

    @term_description.setter
    def term_description(self, term_description):
        """
        Sets the term_description of this FolderTag.
        Description of the related term.


        :param term_description: The term_description of this FolderTag.
        :type: str
        """
        self._term_description = term_description

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this FolderTag.
        The current state of the tag.


        :return: The lifecycle_state of this FolderTag.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FolderTag.
        The current state of the tag.


        :param lifecycle_state: The lifecycle_state of this FolderTag.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this FolderTag.
        The date and time the tag was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this FolderTag.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FolderTag.
        The date and time the tag was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this FolderTag.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this FolderTag.
        OCID of the user who created the tag.


        :return: The created_by_id of this FolderTag.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this FolderTag.
        OCID of the user who created the tag.


        :param created_by_id: The created_by_id of this FolderTag.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def uri(self):
        """
        Gets the uri of this FolderTag.
        URI to the tag instance in the API.


        :return: The uri of this FolderTag.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this FolderTag.
        URI to the tag instance in the API.


        :param uri: The uri of this FolderTag.
        :type: str
        """
        self._uri = uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
