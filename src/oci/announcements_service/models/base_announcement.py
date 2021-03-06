# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BaseAnnouncement(object):
    """
    Incident information that forms the basis of an announcement. Avoid entering confidential information.
    """

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "ACTION_RECOMMENDED"
    ANNOUNCEMENT_TYPE_ACTION_RECOMMENDED = "ACTION_RECOMMENDED"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "ACTION_REQUIRED"
    ANNOUNCEMENT_TYPE_ACTION_REQUIRED = "ACTION_REQUIRED"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "EMERGENCY_CHANGE"
    ANNOUNCEMENT_TYPE_EMERGENCY_CHANGE = "EMERGENCY_CHANGE"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "EMERGENCY_MAINTENANCE"
    ANNOUNCEMENT_TYPE_EMERGENCY_MAINTENANCE = "EMERGENCY_MAINTENANCE"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "EMERGENCY_MAINTENANCE_COMPLETE"
    ANNOUNCEMENT_TYPE_EMERGENCY_MAINTENANCE_COMPLETE = "EMERGENCY_MAINTENANCE_COMPLETE"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "EMERGENCY_MAINTENANCE_EXTENDED"
    ANNOUNCEMENT_TYPE_EMERGENCY_MAINTENANCE_EXTENDED = "EMERGENCY_MAINTENANCE_EXTENDED"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "EMERGENCY_MAINTENANCE_RESCHEDULED"
    ANNOUNCEMENT_TYPE_EMERGENCY_MAINTENANCE_RESCHEDULED = "EMERGENCY_MAINTENANCE_RESCHEDULED"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "INFORMATION"
    ANNOUNCEMENT_TYPE_INFORMATION = "INFORMATION"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "PLANNED_CHANGE"
    ANNOUNCEMENT_TYPE_PLANNED_CHANGE = "PLANNED_CHANGE"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "PLANNED_CHANGE_COMPLETE"
    ANNOUNCEMENT_TYPE_PLANNED_CHANGE_COMPLETE = "PLANNED_CHANGE_COMPLETE"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "PLANNED_CHANGE_EXTENDED"
    ANNOUNCEMENT_TYPE_PLANNED_CHANGE_EXTENDED = "PLANNED_CHANGE_EXTENDED"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "PLANNED_CHANGE_RESCHEDULED"
    ANNOUNCEMENT_TYPE_PLANNED_CHANGE_RESCHEDULED = "PLANNED_CHANGE_RESCHEDULED"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "PRODUCTION_EVENT_NOTIFICATION"
    ANNOUNCEMENT_TYPE_PRODUCTION_EVENT_NOTIFICATION = "PRODUCTION_EVENT_NOTIFICATION"

    #: A constant which can be used with the announcement_type property of a BaseAnnouncement.
    #: This constant has a value of "SCHEDULED_MAINTENANCE"
    ANNOUNCEMENT_TYPE_SCHEDULED_MAINTENANCE = "SCHEDULED_MAINTENANCE"

    #: A constant which can be used with the lifecycle_state property of a BaseAnnouncement.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BaseAnnouncement.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new BaseAnnouncement object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.announcements_service.models.AnnouncementSummary`
        * :class:`~oci.announcements_service.models.Announcement`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BaseAnnouncement.
        :type id: str

        :param type:
            The value to assign to the type property of this BaseAnnouncement.
        :type type: str

        :param reference_ticket_number:
            The value to assign to the reference_ticket_number property of this BaseAnnouncement.
        :type reference_ticket_number: str

        :param summary:
            The value to assign to the summary property of this BaseAnnouncement.
        :type summary: str

        :param time_one_title:
            The value to assign to the time_one_title property of this BaseAnnouncement.
        :type time_one_title: str

        :param time_one_value:
            The value to assign to the time_one_value property of this BaseAnnouncement.
        :type time_one_value: datetime

        :param time_two_title:
            The value to assign to the time_two_title property of this BaseAnnouncement.
        :type time_two_title: str

        :param time_two_value:
            The value to assign to the time_two_value property of this BaseAnnouncement.
        :type time_two_value: datetime

        :param services:
            The value to assign to the services property of this BaseAnnouncement.
        :type services: list[str]

        :param affected_regions:
            The value to assign to the affected_regions property of this BaseAnnouncement.
        :type affected_regions: list[str]

        :param announcement_type:
            The value to assign to the announcement_type property of this BaseAnnouncement.
            Allowed values for this property are: "ACTION_RECOMMENDED", "ACTION_REQUIRED", "EMERGENCY_CHANGE", "EMERGENCY_MAINTENANCE", "EMERGENCY_MAINTENANCE_COMPLETE", "EMERGENCY_MAINTENANCE_EXTENDED", "EMERGENCY_MAINTENANCE_RESCHEDULED", "INFORMATION", "PLANNED_CHANGE", "PLANNED_CHANGE_COMPLETE", "PLANNED_CHANGE_EXTENDED", "PLANNED_CHANGE_RESCHEDULED", "PRODUCTION_EVENT_NOTIFICATION", "SCHEDULED_MAINTENANCE"
        :type announcement_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BaseAnnouncement.
            Allowed values for this property are: "ACTIVE", "INACTIVE"
        :type lifecycle_state: str

        :param is_banner:
            The value to assign to the is_banner property of this BaseAnnouncement.
        :type is_banner: bool

        :param time_created:
            The value to assign to the time_created property of this BaseAnnouncement.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BaseAnnouncement.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'reference_ticket_number': 'str',
            'summary': 'str',
            'time_one_title': 'str',
            'time_one_value': 'datetime',
            'time_two_title': 'str',
            'time_two_value': 'datetime',
            'services': 'list[str]',
            'affected_regions': 'list[str]',
            'announcement_type': 'str',
            'lifecycle_state': 'str',
            'is_banner': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'reference_ticket_number': 'referenceTicketNumber',
            'summary': 'summary',
            'time_one_title': 'timeOneTitle',
            'time_one_value': 'timeOneValue',
            'time_two_title': 'timeTwoTitle',
            'time_two_value': 'timeTwoValue',
            'services': 'services',
            'affected_regions': 'affectedRegions',
            'announcement_type': 'announcementType',
            'lifecycle_state': 'lifecycleState',
            'is_banner': 'isBanner',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._type = None
        self._reference_ticket_number = None
        self._summary = None
        self._time_one_title = None
        self._time_one_value = None
        self._time_two_title = None
        self._time_two_value = None
        self._services = None
        self._affected_regions = None
        self._announcement_type = None
        self._lifecycle_state = None
        self._is_banner = None
        self._time_created = None
        self._time_updated = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'AnnouncementSummary':
            return 'AnnouncementSummary'

        if type == 'Announcement':
            return 'Announcement'
        else:
            return 'BaseAnnouncement'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BaseAnnouncement.
        The OCID of the announcement.


        :return: The id of this BaseAnnouncement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BaseAnnouncement.
        The OCID of the announcement.


        :param id: The id of this BaseAnnouncement.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this BaseAnnouncement.
        The entity type.


        :return: The type of this BaseAnnouncement.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BaseAnnouncement.
        The entity type.


        :param type: The type of this BaseAnnouncement.
        :type: str
        """
        self._type = type

    @property
    def reference_ticket_number(self):
        """
        **[Required]** Gets the reference_ticket_number of this BaseAnnouncement.
        The reference Jira ticket number.


        :return: The reference_ticket_number of this BaseAnnouncement.
        :rtype: str
        """
        return self._reference_ticket_number

    @reference_ticket_number.setter
    def reference_ticket_number(self, reference_ticket_number):
        """
        Sets the reference_ticket_number of this BaseAnnouncement.
        The reference Jira ticket number.


        :param reference_ticket_number: The reference_ticket_number of this BaseAnnouncement.
        :type: str
        """
        self._reference_ticket_number = reference_ticket_number

    @property
    def summary(self):
        """
        **[Required]** Gets the summary of this BaseAnnouncement.
        A summary of the issue. A summary might appear in the console banner view of the announcement or in
        an email subject line. Avoid entering confidential information.


        :return: The summary of this BaseAnnouncement.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this BaseAnnouncement.
        A summary of the issue. A summary might appear in the console banner view of the announcement or in
        an email subject line. Avoid entering confidential information.


        :param summary: The summary of this BaseAnnouncement.
        :type: str
        """
        self._summary = summary

    @property
    def time_one_title(self):
        """
        Gets the time_one_title of this BaseAnnouncement.
        The label associated with an initial time value.
        Example: `Time Started`


        :return: The time_one_title of this BaseAnnouncement.
        :rtype: str
        """
        return self._time_one_title

    @time_one_title.setter
    def time_one_title(self, time_one_title):
        """
        Sets the time_one_title of this BaseAnnouncement.
        The label associated with an initial time value.
        Example: `Time Started`


        :param time_one_title: The time_one_title of this BaseAnnouncement.
        :type: str
        """
        self._time_one_title = time_one_title

    @property
    def time_one_value(self):
        """
        Gets the time_one_value of this BaseAnnouncement.
        The actual value of the first time value for the event. Typically, this is the time an event started, but the meaning
        can vary, depending on the announcement type.


        :return: The time_one_value of this BaseAnnouncement.
        :rtype: datetime
        """
        return self._time_one_value

    @time_one_value.setter
    def time_one_value(self, time_one_value):
        """
        Sets the time_one_value of this BaseAnnouncement.
        The actual value of the first time value for the event. Typically, this is the time an event started, but the meaning
        can vary, depending on the announcement type.


        :param time_one_value: The time_one_value of this BaseAnnouncement.
        :type: datetime
        """
        self._time_one_value = time_one_value

    @property
    def time_two_title(self):
        """
        Gets the time_two_title of this BaseAnnouncement.
        The label associated with a second time value.
        Example: `Time Ended`


        :return: The time_two_title of this BaseAnnouncement.
        :rtype: str
        """
        return self._time_two_title

    @time_two_title.setter
    def time_two_title(self, time_two_title):
        """
        Sets the time_two_title of this BaseAnnouncement.
        The label associated with a second time value.
        Example: `Time Ended`


        :param time_two_title: The time_two_title of this BaseAnnouncement.
        :type: str
        """
        self._time_two_title = time_two_title

    @property
    def time_two_value(self):
        """
        Gets the time_two_value of this BaseAnnouncement.
        The actual value of the second time value. Typically, this is the time an event ended, but the meaning
        can vary, depending on the announcement type.


        :return: The time_two_value of this BaseAnnouncement.
        :rtype: datetime
        """
        return self._time_two_value

    @time_two_value.setter
    def time_two_value(self, time_two_value):
        """
        Sets the time_two_value of this BaseAnnouncement.
        The actual value of the second time value. Typically, this is the time an event ended, but the meaning
        can vary, depending on the announcement type.


        :param time_two_value: The time_two_value of this BaseAnnouncement.
        :type: datetime
        """
        self._time_two_value = time_two_value

    @property
    def services(self):
        """
        **[Required]** Gets the services of this BaseAnnouncement.
        Impacted Oracle Cloud Infrastructure services.


        :return: The services of this BaseAnnouncement.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this BaseAnnouncement.
        Impacted Oracle Cloud Infrastructure services.


        :param services: The services of this BaseAnnouncement.
        :type: list[str]
        """
        self._services = services

    @property
    def affected_regions(self):
        """
        **[Required]** Gets the affected_regions of this BaseAnnouncement.
        Impacted regions.


        :return: The affected_regions of this BaseAnnouncement.
        :rtype: list[str]
        """
        return self._affected_regions

    @affected_regions.setter
    def affected_regions(self, affected_regions):
        """
        Sets the affected_regions of this BaseAnnouncement.
        Impacted regions.


        :param affected_regions: The affected_regions of this BaseAnnouncement.
        :type: list[str]
        """
        self._affected_regions = affected_regions

    @property
    def announcement_type(self):
        """
        **[Required]** Gets the announcement_type of this BaseAnnouncement.
        The type of announcement. An announcement's type signals its severity.

        Allowed values for this property are: "ACTION_RECOMMENDED", "ACTION_REQUIRED", "EMERGENCY_CHANGE", "EMERGENCY_MAINTENANCE", "EMERGENCY_MAINTENANCE_COMPLETE", "EMERGENCY_MAINTENANCE_EXTENDED", "EMERGENCY_MAINTENANCE_RESCHEDULED", "INFORMATION", "PLANNED_CHANGE", "PLANNED_CHANGE_COMPLETE", "PLANNED_CHANGE_EXTENDED", "PLANNED_CHANGE_RESCHEDULED", "PRODUCTION_EVENT_NOTIFICATION", "SCHEDULED_MAINTENANCE"


        :return: The announcement_type of this BaseAnnouncement.
        :rtype: str
        """
        return self._announcement_type

    @announcement_type.setter
    def announcement_type(self, announcement_type):
        """
        Sets the announcement_type of this BaseAnnouncement.
        The type of announcement. An announcement's type signals its severity.


        :param announcement_type: The announcement_type of this BaseAnnouncement.
        :type: str
        """
        allowed_values = ["ACTION_RECOMMENDED", "ACTION_REQUIRED", "EMERGENCY_CHANGE", "EMERGENCY_MAINTENANCE", "EMERGENCY_MAINTENANCE_COMPLETE", "EMERGENCY_MAINTENANCE_EXTENDED", "EMERGENCY_MAINTENANCE_RESCHEDULED", "INFORMATION", "PLANNED_CHANGE", "PLANNED_CHANGE_COMPLETE", "PLANNED_CHANGE_EXTENDED", "PLANNED_CHANGE_RESCHEDULED", "PRODUCTION_EVENT_NOTIFICATION", "SCHEDULED_MAINTENANCE"]
        if not value_allowed_none_or_none_sentinel(announcement_type, allowed_values):
            raise ValueError(
                "Invalid value for `announcement_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._announcement_type = announcement_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BaseAnnouncement.
        The current lifecycle state of the announcement.

        Allowed values for this property are: "ACTIVE", "INACTIVE"


        :return: The lifecycle_state of this BaseAnnouncement.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BaseAnnouncement.
        The current lifecycle state of the announcement.


        :param lifecycle_state: The lifecycle_state of this BaseAnnouncement.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def is_banner(self):
        """
        **[Required]** Gets the is_banner of this BaseAnnouncement.
        Whether the announcement is displayed as a banner in the console.


        :return: The is_banner of this BaseAnnouncement.
        :rtype: bool
        """
        return self._is_banner

    @is_banner.setter
    def is_banner(self, is_banner):
        """
        Sets the is_banner of this BaseAnnouncement.
        Whether the announcement is displayed as a banner in the console.


        :param is_banner: The is_banner of this BaseAnnouncement.
        :type: bool
        """
        self._is_banner = is_banner

    @property
    def time_created(self):
        """
        Gets the time_created of this BaseAnnouncement.
        The date and time the announcement was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-01-01T17:43:01.389+0000`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this BaseAnnouncement.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BaseAnnouncement.
        The date and time the announcement was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-01-01T17:43:01.389+0000`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this BaseAnnouncement.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BaseAnnouncement.
        The date and time the announcement was last updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-01-01T17:43:01.389+0000`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this BaseAnnouncement.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BaseAnnouncement.
        The date and time the announcement was last updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2019-01-01T17:43:01.389+0000`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this BaseAnnouncement.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
