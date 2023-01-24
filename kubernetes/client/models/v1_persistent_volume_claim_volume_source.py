# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.26
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1PersistentVolumeClaimVolumeSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'claim_name': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'claim_name': 'claimName',
        'read_only': 'readOnly'
    }

    def __init__(self, claim_name=None, read_only=None, local_vars_configuration=None):  # noqa: E501
        """V1PersistentVolumeClaimVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._claim_name = None
        self._read_only = None
        self.discriminator = None

        self.claim_name = claim_name
        if read_only is not None:
            self.read_only = read_only

    @property
    def claim_name(self):
        """Gets the claim_name of this V1PersistentVolumeClaimVolumeSource.  # noqa: E501

        claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims  # noqa: E501

        :return: The claim_name of this V1PersistentVolumeClaimVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """Sets the claim_name of this V1PersistentVolumeClaimVolumeSource.

        claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims  # noqa: E501

        :param claim_name: The claim_name of this V1PersistentVolumeClaimVolumeSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and claim_name is None:  # noqa: E501
            raise ValueError("Invalid value for `claim_name`, must not be `None`")  # noqa: E501

        self._claim_name = claim_name

    @property
    def read_only(self):
        """Gets the read_only of this V1PersistentVolumeClaimVolumeSource.  # noqa: E501

        readOnly Will force the ReadOnly setting in VolumeMounts. Default false.  # noqa: E501

        :return: The read_only of this V1PersistentVolumeClaimVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1PersistentVolumeClaimVolumeSource.

        readOnly Will force the ReadOnly setting in VolumeMounts. Default false.  # noqa: E501

        :param read_only: The read_only of this V1PersistentVolumeClaimVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, V1PersistentVolumeClaimVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PersistentVolumeClaimVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
