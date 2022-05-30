// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Astra
{
    public static class GetKeyspace
    {
        /// <summary>
        /// `astra.Keyspace` provides a datasource for a particular keyspace. See `astra.getKeyspaces` if you're looking to fetch all the keyspaces for a particular database.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Astra = Pulumi.Astra;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var dev = Output.Create(Astra.GetKeyspace.InvokeAsync(new Astra.GetKeyspaceArgs
        ///         {
        ///             DatabaseId = "f9f4b1e0-4c05-451e-9bba-d631295a7f73",
        ///             Name = "puppies",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetKeyspaceResult> InvokeAsync(GetKeyspaceArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetKeyspaceResult>("astra:index/getKeyspace:getKeyspace", args ?? new GetKeyspaceArgs(), options.WithDefaults());

        /// <summary>
        /// `astra.Keyspace` provides a datasource for a particular keyspace. See `astra.getKeyspaces` if you're looking to fetch all the keyspaces for a particular database.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Astra = Pulumi.Astra;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var dev = Output.Create(Astra.GetKeyspace.InvokeAsync(new Astra.GetKeyspaceArgs
        ///         {
        ///             DatabaseId = "f9f4b1e0-4c05-451e-9bba-d631295a7f73",
        ///             Name = "puppies",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetKeyspaceResult> Invoke(GetKeyspaceInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetKeyspaceResult>("astra:index/getKeyspace:getKeyspace", args ?? new GetKeyspaceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetKeyspaceArgs : Pulumi.InvokeArgs
    {
        [Input("databaseId", required: true)]
        public string DatabaseId { get; set; } = null!;

        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetKeyspaceArgs()
        {
        }
    }

    public sealed class GetKeyspaceInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("databaseId", required: true)]
        public Input<string> DatabaseId { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetKeyspaceInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetKeyspaceResult
    {
        public readonly string DatabaseId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;

        [OutputConstructor]
        private GetKeyspaceResult(
            string databaseId,

            string id,

            string name)
        {
            DatabaseId = databaseId;
            Id = id;
            Name = name;
        }
    }
}