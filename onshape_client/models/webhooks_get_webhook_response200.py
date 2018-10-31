# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.87
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from onshape_client.models.webhooks_get_webhook_response200_options import WebhooksGetWebhookResponse200Options  # noqa: F401,E501


class WebhooksGetWebhookResponse200(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'id': 'str',
        'filter': 'str',
        'dropped_event_count': 'float',
        'options': 'WebhooksGetWebhookResponse200Options',
        'data': 'str',
        'events': 'list[str]'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'filter': 'filter',
        'dropped_event_count': 'droppedEventCount',
        'options': 'options',
        'data': 'data',
        'events': 'events'
    }

    def __init__(self, url=None, id=None, filter=None, dropped_event_count=None, options=None, data=None, events=None):  # noqa: E501
        """WebhooksGetWebhookResponse200 - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._id = None
        self._filter = None
        self._dropped_event_count = None
        self._options = None
        self._data = None
        self._events = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if filter is not None:
            self.filter = filter
        if dropped_event_count is not None:
            self.dropped_event_count = dropped_event_count
        if options is not None:
            self.options = options
        if data is not None:
            self.data = data
        if events is not None:
            self.events = events

    @property
    def url(self):
        """Gets the url of this WebhooksGetWebhookResponse200.  # noqa: E501

        URL to which notifications are sent  # noqa: E501

        :return: The url of this WebhooksGetWebhookResponse200.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhooksGetWebhookResponse200.

        URL to which notifications are sent  # noqa: E501

        :param url: The url of this WebhooksGetWebhookResponse200.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this WebhooksGetWebhookResponse200.  # noqa: E501

        ID of webhook  # noqa: E501

        :return: The id of this WebhooksGetWebhookResponse200.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhooksGetWebhookResponse200.

        ID of webhook  # noqa: E501

        :param id: The id of this WebhooksGetWebhookResponse200.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def filter(self):
        """Gets the filter of this WebhooksGetWebhookResponse200.  # noqa: E501

        Context for webhook  # noqa: E501

        :return: The filter of this WebhooksGetWebhookResponse200.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this WebhooksGetWebhookResponse200.

        Context for webhook  # noqa: E501

        :param filter: The filter of this WebhooksGetWebhookResponse200.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def dropped_event_count(self):
        """Gets the dropped_event_count of this WebhooksGetWebhookResponse200.  # noqa: E501

        Number of dropped events  # noqa: E501

        :return: The dropped_event_count of this WebhooksGetWebhookResponse200.  # noqa: E501
        :rtype: float
        """
        return self._dropped_event_count

    @dropped_event_count.setter
    def dropped_event_count(self, dropped_event_count):
        """Sets the dropped_event_count of this WebhooksGetWebhookResponse200.

        Number of dropped events  # noqa: E501

        :param dropped_event_count: The dropped_event_count of this WebhooksGetWebhookResponse200.  # noqa: E501
        :type: float
        """

        self._dropped_event_count = dropped_event_count

    @property
    def options(self):
        """Gets the options of this WebhooksGetWebhookResponse200.  # noqa: E501


        :return: The options of this WebhooksGetWebhookResponse200.  # noqa: E501
        :rtype: WebhooksGetWebhookResponse200Options
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this WebhooksGetWebhookResponse200.


        :param options: The options of this WebhooksGetWebhookResponse200.  # noqa: E501
        :type: WebhooksGetWebhookResponse200Options
        """

        self._options = options

    @property
    def data(self):
        """Gets the data of this WebhooksGetWebhookResponse200.  # noqa: E501

        Data returned from webhook  # noqa: E501

        :return: The data of this WebhooksGetWebhookResponse200.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this WebhooksGetWebhookResponse200.

        Data returned from webhook  # noqa: E501

        :param data: The data of this WebhooksGetWebhookResponse200.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def events(self):
        """Gets the events of this WebhooksGetWebhookResponse200.  # noqa: E501

        Array of events to which webhook is registered  # noqa: E501

        :return: The events of this WebhooksGetWebhookResponse200.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this WebhooksGetWebhookResponse200.

        Array of events to which webhook is registered  # noqa: E501

        :param events: The events of this WebhooksGetWebhookResponse200.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebhooksGetWebhookResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
