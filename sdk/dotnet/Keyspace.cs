// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Astra
{
    /// <summary>
    /// `astra.Keyspace` provides a keyspace resource. Keyspaces are groupings of tables for Cassandra. `astra.Keyspace` resources are associated with a database id. You can have multiple keyspaces per DB in addition to the default keyspace provided in the `astra.Database` resource.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Astra = Pulumiverse.Astra;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Astra.Keyspace("example", new Astra.KeyspaceArgs
    ///         {
    ///             DatabaseId = "48bfc13b-c1a5-48db-b70f-b6ef9709872b",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// # the import id includes the database_id and the keyspace name.
    /// 
    /// ```sh
    ///  $ pulumi import astra:index/keyspace:Keyspace example 48bfc13b-c1a5-48db-b70f-b6ef9709872b/keyspace/example
    /// ```
    /// </summary>
    [AstraResourceType("astra:index/keyspace:Keyspace")]
    public partial class Keyspace : Pulumi.CustomResource
    {
        /// <summary>
        /// Astra database to create the keyspace.
        /// </summary>
        [Output("databaseId")]
        public Output<string> DatabaseId { get; private set; } = null!;

        /// <summary>
        /// Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
        /// as the first character.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a Keyspace resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Keyspace(string name, KeyspaceArgs args, CustomResourceOptions? options = null)
            : base("astra:index/keyspace:Keyspace", name, args ?? new KeyspaceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Keyspace(string name, Input<string> id, KeyspaceState? state = null, CustomResourceOptions? options = null)
            : base("astra:index/keyspace:Keyspace", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/pulumiverse/pulumi-astra/releases/download/${VERSION}",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Keyspace resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Keyspace Get(string name, Input<string> id, KeyspaceState? state = null, CustomResourceOptions? options = null)
        {
            return new Keyspace(name, id, state, options);
        }
    }

    public sealed class KeyspaceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Astra database to create the keyspace.
        /// </summary>
        [Input("databaseId", required: true)]
        public Input<string> DatabaseId { get; set; } = null!;

        /// <summary>
        /// Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
        /// as the first character.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public KeyspaceArgs()
        {
        }
    }

    public sealed class KeyspaceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Astra database to create the keyspace.
        /// </summary>
        [Input("databaseId")]
        public Input<string>? DatabaseId { get; set; }

        /// <summary>
        /// Keyspace name can have up to 48 alpha-numeric characters and contain underscores; only letters and numbers are supported
        /// as the first character.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public KeyspaceState()
        {
        }
    }
}
