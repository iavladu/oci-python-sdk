# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDataWarehouseConsoleTokenDetails(object):
    """
    **Deprecated.** See :func:`autonomous_database_console_token_details` for reference information about the token that allows the OCI Console to access the Autonomous Data Warehouse Service Console.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDataWarehouseConsoleTokenDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param token:
            The value to assign to the token property of this AutonomousDataWarehouseConsoleTokenDetails.
        :type token: str

        :param login_url:
            The value to assign to the login_url property of this AutonomousDataWarehouseConsoleTokenDetails.
        :type login_url: str

        """
        self.swagger_types = {
            'token': 'str',
            'login_url': 'str'
        }

        self.attribute_map = {
            'token': 'token',
            'login_url': 'loginUrl'
        }

        self._token = None
        self._login_url = None

    @property
    def token(self):
        """
        Gets the token of this AutonomousDataWarehouseConsoleTokenDetails.
        The token that allows the OCI Console to access the Autonomous Data Warehouse Service Console.


        :return: The token of this AutonomousDataWarehouseConsoleTokenDetails.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this AutonomousDataWarehouseConsoleTokenDetails.
        The token that allows the OCI Console to access the Autonomous Data Warehouse Service Console.


        :param token: The token of this AutonomousDataWarehouseConsoleTokenDetails.
        :type: str
        """
        self._token = token

    @property
    def login_url(self):
        """
        Gets the login_url of this AutonomousDataWarehouseConsoleTokenDetails.
        The login URL that allows the OCI Console to access the Autonomous Data Warehouse Service Console.


        :return: The login_url of this AutonomousDataWarehouseConsoleTokenDetails.
        :rtype: str
        """
        return self._login_url

    @login_url.setter
    def login_url(self, login_url):
        """
        Sets the login_url of this AutonomousDataWarehouseConsoleTokenDetails.
        The login URL that allows the OCI Console to access the Autonomous Data Warehouse Service Console.


        :param login_url: The login_url of this AutonomousDataWarehouseConsoleTokenDetails.
        :type: str
        """
        self._login_url = login_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
