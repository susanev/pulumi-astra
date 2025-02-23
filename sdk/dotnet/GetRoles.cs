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
    public static class GetRoles
    {
        /// <summary>
        /// `astra.Role` provides a datasource that lists the custom roles for an org.
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
        ///         var dev = Output.Create(Astra.GetRoles.InvokeAsync(new Astra.GetRolesArgs
        ///         {
        ///             RoleId = "role-id-here",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetRolesResult> InvokeAsync(GetRolesArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRolesResult>("astra:index/getRoles:getRoles", args ?? new GetRolesArgs(), options.WithDefaults());

        /// <summary>
        /// `astra.Role` provides a datasource that lists the custom roles for an org.
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
        ///         var dev = Output.Create(Astra.GetRoles.InvokeAsync(new Astra.GetRolesArgs
        ///         {
        ///             RoleId = "role-id-here",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetRolesResult> Invoke(GetRolesInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetRolesResult>("astra:index/getRoles:getRoles", args ?? new GetRolesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRolesArgs : Pulumi.InvokeArgs
    {
        [Input("roleId", required: true)]
        public string RoleId { get; set; } = null!;

        public GetRolesArgs()
        {
        }
    }

    public sealed class GetRolesInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("roleId", required: true)]
        public Input<string> RoleId { get; set; } = null!;

        public GetRolesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetRolesResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetRolesResultResult> Results;
        public readonly string RoleId;

        [OutputConstructor]
        private GetRolesResult(
            string id,

            ImmutableArray<Outputs.GetRolesResultResult> results,

            string roleId)
        {
            Id = id;
            Results = results;
            RoleId = roleId;
        }
    }
}
