# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'AccessListAddress',
    'AccessListAddressRequest',
    'GetAccessListResultResult',
    'GetAstraDatabasesResultResult',
    'GetAvailableRegionsResultResult',
    'GetKeyspacesResultResult',
    'GetPrivateLinkEndpointsResultResult',
    'GetPrivateLinksResultResult',
    'GetRolesResultResult',
]

@pulumi.output_type
class AccessListAddress(dict):
    def __init__(__self__, *,
                 requests: Sequence['outputs.AccessListAddressRequest']):
        pulumi.set(__self__, "requests", requests)

    @property
    @pulumi.getter
    def requests(self) -> Sequence['outputs.AccessListAddressRequest']:
        return pulumi.get(self, "requests")


@pulumi.output_type
class AccessListAddressRequest(dict):
    def __init__(__self__, *,
                 address: str,
                 enabled: bool,
                 description: Optional[str] = None):
        pulumi.set(__self__, "address", address)
        pulumi.set(__self__, "enabled", enabled)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def address(self) -> str:
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class GetAccessListResultResult(dict):
    def __init__(__self__, *,
                 addresses: Sequence[str],
                 datacenter_id: str,
                 enabled: str,
                 organization_id: str):
        pulumi.set(__self__, "addresses", addresses)
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "organization_id", organization_id)

    @property
    @pulumi.getter
    def addresses(self) -> Sequence[str]:
        return pulumi.get(self, "addresses")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def enabled(self) -> str:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        return pulumi.get(self, "organization_id")


@pulumi.output_type
class GetAstraDatabasesResultResult(dict):
    def __init__(__self__, *,
                 additional_keyspaces: Sequence[str],
                 cloud_provider: str,
                 cqlsh_url: str,
                 data_endpoint_url: str,
                 grafana_url: str,
                 graphql_url: str,
                 id: str,
                 keyspace: str,
                 name: str,
                 node_count: int,
                 organization_id: str,
                 owner_id: str,
                 regions: Sequence[str],
                 replication_factor: int,
                 status: str,
                 total_storage: int):
        pulumi.set(__self__, "additional_keyspaces", additional_keyspaces)
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        pulumi.set(__self__, "cqlsh_url", cqlsh_url)
        pulumi.set(__self__, "data_endpoint_url", data_endpoint_url)
        pulumi.set(__self__, "grafana_url", grafana_url)
        pulumi.set(__self__, "graphql_url", graphql_url)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "keyspace", keyspace)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "node_count", node_count)
        pulumi.set(__self__, "organization_id", organization_id)
        pulumi.set(__self__, "owner_id", owner_id)
        pulumi.set(__self__, "regions", regions)
        pulumi.set(__self__, "replication_factor", replication_factor)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "total_storage", total_storage)

    @property
    @pulumi.getter(name="additionalKeyspaces")
    def additional_keyspaces(self) -> Sequence[str]:
        return pulumi.get(self, "additional_keyspaces")

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> str:
        return pulumi.get(self, "cloud_provider")

    @property
    @pulumi.getter(name="cqlshUrl")
    def cqlsh_url(self) -> str:
        return pulumi.get(self, "cqlsh_url")

    @property
    @pulumi.getter(name="dataEndpointUrl")
    def data_endpoint_url(self) -> str:
        return pulumi.get(self, "data_endpoint_url")

    @property
    @pulumi.getter(name="grafanaUrl")
    def grafana_url(self) -> str:
        return pulumi.get(self, "grafana_url")

    @property
    @pulumi.getter(name="graphqlUrl")
    def graphql_url(self) -> str:
        return pulumi.get(self, "graphql_url")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def keyspace(self) -> str:
        return pulumi.get(self, "keyspace")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> int:
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> str:
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter
    def regions(self) -> Sequence[str]:
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> int:
        return pulumi.get(self, "replication_factor")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="totalStorage")
    def total_storage(self) -> int:
        return pulumi.get(self, "total_storage")


@pulumi.output_type
class GetAvailableRegionsResultResult(dict):
    def __init__(__self__, *,
                 cloud_provider: str,
                 display_name: str,
                 region: str,
                 zone: str):
        pulumi.set(__self__, "cloud_provider", cloud_provider)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="cloudProvider")
    def cloud_provider(self) -> str:
        return pulumi.get(self, "cloud_provider")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")


@pulumi.output_type
class GetKeyspacesResultResult(dict):
    def __init__(__self__, *,
                 name: str):
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


@pulumi.output_type
class GetPrivateLinkEndpointsResultResult(dict):
    def __init__(__self__, *,
                 create_time: str,
                 description: str,
                 endpoint_id: str,
                 status: str):
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "endpoint_id", endpoint_id)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> str:
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")


@pulumi.output_type
class GetPrivateLinksResultResult(dict):
    def __init__(__self__, *,
                 allowed_principals: Sequence[str],
                 datacenter_id: str,
                 endpoints: Sequence[str],
                 service_name: str):
        pulumi.set(__self__, "allowed_principals", allowed_principals)
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "endpoints", endpoints)
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="allowedPrincipals")
    def allowed_principals(self) -> Sequence[str]:
        return pulumi.get(self, "allowed_principals")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence[str]:
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")


@pulumi.output_type
class GetRolesResultResult(dict):
    def __init__(__self__, *,
                 description: str,
                 effect: str,
                 policies: Sequence[str],
                 resources: Sequence[str],
                 role_name: str):
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "effect", effect)
        pulumi.set(__self__, "policies", policies)
        pulumi.set(__self__, "resources", resources)
        pulumi.set(__self__, "role_name", role_name)

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def effect(self) -> str:
        return pulumi.get(self, "effect")

    @property
    @pulumi.getter
    def policies(self) -> Sequence[str]:
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter
    def resources(self) -> Sequence[str]:
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> str:
        return pulumi.get(self, "role_name")

