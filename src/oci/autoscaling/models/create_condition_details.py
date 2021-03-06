# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConditionDetails(object):
    """
    Creation details for a condition in a threshold-based autoscaling policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConditionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this CreateConditionDetails.
        :type action: Action

        :param display_name:
            The value to assign to the display_name property of this CreateConditionDetails.
        :type display_name: str

        :param metric:
            The value to assign to the metric property of this CreateConditionDetails.
        :type metric: Metric

        """
        self.swagger_types = {
            'action': 'Action',
            'display_name': 'str',
            'metric': 'Metric'
        }

        self.attribute_map = {
            'action': 'action',
            'display_name': 'displayName',
            'metric': 'metric'
        }

        self._action = None
        self._display_name = None
        self._metric = None

    @property
    def action(self):
        """
        **[Required]** Gets the action of this CreateConditionDetails.

        :return: The action of this CreateConditionDetails.
        :rtype: Action
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this CreateConditionDetails.

        :param action: The action of this CreateConditionDetails.
        :type: Action
        """
        self._action = action

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateConditionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateConditionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateConditionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateConditionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def metric(self):
        """
        **[Required]** Gets the metric of this CreateConditionDetails.

        :return: The metric of this CreateConditionDetails.
        :rtype: Metric
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this CreateConditionDetails.

        :param metric: The metric of this CreateConditionDetails.
        :type: Metric
        """
        self._metric = metric

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
