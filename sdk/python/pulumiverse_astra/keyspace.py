# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['KeyspaceArgs', 'Keyspace']

@pulumi.input_type
class KeyspaceArgs:
    def __init__(__self__, *,
                 database_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Keyspace resource.
        :param pulumi.Input[str] database_id: Astra database to create the keyspace.
        :param pulumi.Input[str] name: Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
               as the first character.
        """
        pulumi.set(__self__, "database_id", database_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Input[str]:
        """
        Astra database to create the keyspace.
        """
        return pulumi.get(self, "database_id")

    @database_id.setter
    def database_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
        as the first character.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _KeyspaceState:
    def __init__(__self__, *,
                 database_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Keyspace resources.
        :param pulumi.Input[str] database_id: Astra database to create the keyspace.
        :param pulumi.Input[str] name: Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
               as the first character.
        """
        if database_id is not None:
            pulumi.set(__self__, "database_id", database_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> Optional[pulumi.Input[str]]:
        """
        Astra database to create the keyspace.
        """
        return pulumi.get(self, "database_id")

    @database_id.setter
    def database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
        as the first character.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Keyspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        `Keyspace` provides a keyspace resource. Keyspaces are groupings of tables for Cassandra. `Keyspace` resources are associated with a database id. You can have multiple keyspaces per DB in addition to the default keyspace provided in the `Database` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_astra as astra

        example = astra.Keyspace("example", database_id="48bfc13b-c1a5-48db-b70f-b6ef9709872b")
        ```

        ## Import

        # the import id includes the database_id and the keyspace name.

        ```sh
         $ pulumi import astra:index/keyspace:Keyspace example 48bfc13b-c1a5-48db-b70f-b6ef9709872b/keyspace/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_id: Astra database to create the keyspace.
        :param pulumi.Input[str] name: Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
               as the first character.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KeyspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `Keyspace` provides a keyspace resource. Keyspaces are groupings of tables for Cassandra. `Keyspace` resources are associated with a database id. You can have multiple keyspaces per DB in addition to the default keyspace provided in the `Database` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_astra as astra

        example = astra.Keyspace("example", database_id="48bfc13b-c1a5-48db-b70f-b6ef9709872b")
        ```

        ## Import

        # the import id includes the database_id and the keyspace name.

        ```sh
         $ pulumi import astra:index/keyspace:Keyspace example 48bfc13b-c1a5-48db-b70f-b6ef9709872b/keyspace/example
        ```

        :param str resource_name: The name of the resource.
        :param KeyspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KeyspaceArgs.__new__(KeyspaceArgs)

            if database_id is None and not opts.urn:
                raise TypeError("Missing required property 'database_id'")
            __props__.__dict__["database_id"] = database_id
            __props__.__dict__["name"] = name
        super(Keyspace, __self__).__init__(
            'astra:index/keyspace:Keyspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            database_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'Keyspace':
        """
        Get an existing Keyspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_id: Astra database to create the keyspace.
        :param pulumi.Input[str] name: Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
               as the first character.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KeyspaceState.__new__(_KeyspaceState)

        __props__.__dict__["database_id"] = database_id
        __props__.__dict__["name"] = name
        return Keyspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Output[str]:
        """
        Astra database to create the keyspace.
        """
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
        as the first character.
        """
        return pulumi.get(self, "name")

