import graphene

from graphene_django import DjangoObjectType
from ipam import filtersets, models
from netbox.graphql.scalars import BigInt
from netbox.graphql.types import BaseObjectType, OrganizationalObjectType, NetBoxObjectType

__all__ = (
    'ASNType',
    'AggregateType',
    'FHRPGroupType',
    'FHRPGroupAssignmentType',
    'IPAddressType',
    'IPRangeType',
    'L2VPNType',
    'L2VPNTerminationType',
    'PrefixType',
    'RIRType',
    'RoleType',
    'RouteTargetType',
    'ServiceType',
    'ServiceTemplateType',
    'VLANType',
    'VLANGroupType',
    'VRFType',
)


class ASNType(NetBoxObjectType):
    asn = graphene.Field(BigInt)

    class Meta:
        model = models.ASN
        fields = '__all__'
        filterset_class = filtersets.ASNFilterSet


class AggregateType(NetBoxObjectType):

    class Meta:
        model = models.Aggregate
        fields = '__all__'
        filterset_class = filtersets.AggregateFilterSet


class FHRPGroupType(NetBoxObjectType):

    class Meta:
        model = models.FHRPGroup
        fields = '__all__'
        filterset_class = filtersets.FHRPGroupFilterSet

    def resolve_auth_type(self, info):
        return self.auth_type or None


class FHRPGroupAssignmentType(BaseObjectType):

    class Meta:
        model = models.FHRPGroupAssignment
        fields = '__all__'
        filterset_class = filtersets.FHRPGroupAssignmentFilterSet


class IPAddressType(NetBoxObjectType):

    class Meta:
        model = models.IPAddress
        fields = '__all__'
        filterset_class = filtersets.IPAddressFilterSet

    def resolve_role(self, info):
        return self.role or None


class IPRangeType(NetBoxObjectType):

    class Meta:
        model = models.IPRange
        fields = '__all__'
        filterset_class = filtersets.IPRangeFilterSet

    def resolve_role(self, info):
        return self.role or None


class PrefixType(NetBoxObjectType):

    class Meta:
        model = models.Prefix
        fields = '__all__'
        filterset_class = filtersets.PrefixFilterSet


class RIRType(OrganizationalObjectType):

    class Meta:
        model = models.RIR
        fields = '__all__'
        filterset_class = filtersets.RIRFilterSet


class RoleType(OrganizationalObjectType):

    class Meta:
        model = models.Role
        fields = '__all__'
        filterset_class = filtersets.RoleFilterSet


class RouteTargetType(NetBoxObjectType):

    class Meta:
        model = models.RouteTarget
        fields = '__all__'
        filterset_class = filtersets.RouteTargetFilterSet


class ServiceType(NetBoxObjectType):

    class Meta:
        model = models.Service
        fields = '__all__'
        filterset_class = filtersets.ServiceFilterSet


class ServiceTemplateType(NetBoxObjectType):

    class Meta:
        model = models.ServiceTemplate
        fields = '__all__'
        filterset_class = filtersets.ServiceTemplateFilterSet


class VLANType(NetBoxObjectType):

    class Meta:
        model = models.VLAN
        fields = '__all__'
        filterset_class = filtersets.VLANFilterSet


class VLANGroupType(OrganizationalObjectType):

    class Meta:
        model = models.VLANGroup
        fields = '__all__'
        filterset_class = filtersets.VLANGroupFilterSet


class VRFType(NetBoxObjectType):

    class Meta:
        model = models.VRF
        fields = '__all__'
        filterset_class = filtersets.VRFFilterSet


class L2VPNType(NetBoxObjectType):
    class Meta:
        model = models.L2VPN
        fields = '__all__'
        filtersets_class = filtersets.L2VPNFilterSet


class L2VPNTerminationType(NetBoxObjectType):
    assigned_object = graphene.Field('ipam.graphql.gfk_mixins.L2VPNAssignmentType')

    class Meta:
        model = models.L2VPNTermination
        exclude = ('assigned_object_type', 'assigned_object_id')
        filtersets_class = filtersets.L2VPNTerminationFilterSet
