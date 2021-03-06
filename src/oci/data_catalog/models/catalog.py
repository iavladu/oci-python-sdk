# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Catalog(object):
    """
    A data catalog enables you to collect, organize, find, access, understand, enrich, and activate technical, business, and operational metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Catalog object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Catalog.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Catalog.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Catalog.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this Catalog.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Catalog.
        :type time_updated: datetime

        :param service_api_url:
            The value to assign to the service_api_url property of this Catalog.
        :type service_api_url: str

        :param service_console_url:
            The value to assign to the service_console_url property of this Catalog.
        :type service_console_url: str

        :param number_of_objects:
            The value to assign to the number_of_objects property of this Catalog.
        :type number_of_objects: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Catalog.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Catalog.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Catalog.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Catalog.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'service_api_url': 'str',
            'service_console_url': 'str',
            'number_of_objects': 'int',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'service_api_url': 'serviceApiUrl',
            'service_console_url': 'serviceConsoleUrl',
            'number_of_objects': 'numberOfObjects',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._service_api_url = None
        self._service_console_url = None
        self._number_of_objects = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Catalog.
        OCID of the data catalog instance.


        :return: The id of this Catalog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Catalog.
        OCID of the data catalog instance.


        :param id: The id of this Catalog.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Catalog.
        Data catalog identifier, which can be renamed.


        :return: The display_name of this Catalog.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Catalog.
        Data catalog identifier, which can be renamed.


        :param display_name: The display_name of this Catalog.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Catalog.
        Compartment identifier.


        :return: The compartment_id of this Catalog.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Catalog.
        Compartment identifier.


        :param compartment_id: The compartment_id of this Catalog.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Catalog.
        The time the data catalog was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Catalog.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Catalog.
        The time the data catalog was created. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Catalog.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Catalog.
        The time the data catalog was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Catalog.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Catalog.
        The time the data catalog was updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Catalog.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def service_api_url(self):
        """
        Gets the service_api_url of this Catalog.
        The REST front endpoint URL to the data catalog instance.


        :return: The service_api_url of this Catalog.
        :rtype: str
        """
        return self._service_api_url

    @service_api_url.setter
    def service_api_url(self, service_api_url):
        """
        Sets the service_api_url of this Catalog.
        The REST front endpoint URL to the data catalog instance.


        :param service_api_url: The service_api_url of this Catalog.
        :type: str
        """
        self._service_api_url = service_api_url

    @property
    def service_console_url(self):
        """
        Gets the service_console_url of this Catalog.
        The console front endpoint URL to the data catalog instance.


        :return: The service_console_url of this Catalog.
        :rtype: str
        """
        return self._service_console_url

    @service_console_url.setter
    def service_console_url(self, service_console_url):
        """
        Sets the service_console_url of this Catalog.
        The console front endpoint URL to the data catalog instance.


        :param service_console_url: The service_console_url of this Catalog.
        :type: str
        """
        self._service_console_url = service_console_url

    @property
    def number_of_objects(self):
        """
        Gets the number_of_objects of this Catalog.
        The number of data objects added to the data catalog.
        Please see the data catalog documentation for further information on how this is calculated.


        :return: The number_of_objects of this Catalog.
        :rtype: int
        """
        return self._number_of_objects

    @number_of_objects.setter
    def number_of_objects(self, number_of_objects):
        """
        Sets the number_of_objects of this Catalog.
        The number of data objects added to the data catalog.
        Please see the data catalog documentation for further information on how this is calculated.


        :param number_of_objects: The number_of_objects of this Catalog.
        :type: int
        """
        self._number_of_objects = number_of_objects

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Catalog.
        The current state of the data catalog resource.


        :return: The lifecycle_state of this Catalog.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Catalog.
        The current state of the data catalog resource.


        :param lifecycle_state: The lifecycle_state of this Catalog.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Catalog.
        An message describing the current state in more detail.
        For example, it can be used to provide actionable information for a resource in 'Failed' state.


        :return: The lifecycle_details of this Catalog.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Catalog.
        An message describing the current state in more detail.
        For example, it can be used to provide actionable information for a resource in 'Failed' state.


        :param lifecycle_details: The lifecycle_details of this Catalog.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Catalog.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Catalog.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Catalog.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Catalog.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Catalog.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Catalog.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Catalog.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Catalog.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
