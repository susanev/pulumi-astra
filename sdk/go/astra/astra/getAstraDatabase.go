// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package astra

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetAstraDatabase(ctx *pulumi.Context, args *GetAstraDatabaseArgs, opts ...pulumi.InvokeOption) (*GetAstraDatabaseResult, error) {
	var rv GetAstraDatabaseResult
	err := ctx.Invoke("index:astra/getAstraDatabase:getAstraDatabase", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAstraDatabase.
type GetAstraDatabaseArgs struct {
	DatabaseId string `pulumi:"databaseId"`
}

// A collection of values returned by getAstraDatabase.
type GetAstraDatabaseResult struct {
	AdditionalKeyspaces []string `pulumi:"additionalKeyspaces"`
	CloudProvider       string   `pulumi:"cloudProvider"`
	CqlshUrl            string   `pulumi:"cqlshUrl"`
	DataEndpointUrl     string   `pulumi:"dataEndpointUrl"`
	DatabaseId          string   `pulumi:"databaseId"`
	GrafanaUrl          string   `pulumi:"grafanaUrl"`
	GraphqlUrl          string   `pulumi:"graphqlUrl"`
	// The provider-assigned unique ID for this managed resource.
	Id                string   `pulumi:"id"`
	Keyspace          string   `pulumi:"keyspace"`
	Name              string   `pulumi:"name"`
	NodeCount         int      `pulumi:"nodeCount"`
	OrganizationId    string   `pulumi:"organizationId"`
	OwnerId           string   `pulumi:"ownerId"`
	Regions           []string `pulumi:"regions"`
	ReplicationFactor int      `pulumi:"replicationFactor"`
	Status            string   `pulumi:"status"`
	TotalStorage      int      `pulumi:"totalStorage"`
}

func GetAstraDatabaseOutput(ctx *pulumi.Context, args GetAstraDatabaseOutputArgs, opts ...pulumi.InvokeOption) GetAstraDatabaseResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetAstraDatabaseResult, error) {
			args := v.(GetAstraDatabaseArgs)
			r, err := GetAstraDatabase(ctx, &args, opts...)
			return *r, err
		}).(GetAstraDatabaseResultOutput)
}

// A collection of arguments for invoking getAstraDatabase.
type GetAstraDatabaseOutputArgs struct {
	DatabaseId pulumi.StringInput `pulumi:"databaseId"`
}

func (GetAstraDatabaseOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAstraDatabaseArgs)(nil)).Elem()
}

// A collection of values returned by getAstraDatabase.
type GetAstraDatabaseResultOutput struct{ *pulumi.OutputState }

func (GetAstraDatabaseResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAstraDatabaseResult)(nil)).Elem()
}

func (o GetAstraDatabaseResultOutput) ToGetAstraDatabaseResultOutput() GetAstraDatabaseResultOutput {
	return o
}

func (o GetAstraDatabaseResultOutput) ToGetAstraDatabaseResultOutputWithContext(ctx context.Context) GetAstraDatabaseResultOutput {
	return o
}

func (o GetAstraDatabaseResultOutput) AdditionalKeyspaces() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) []string { return v.AdditionalKeyspaces }).(pulumi.StringArrayOutput)
}

func (o GetAstraDatabaseResultOutput) CloudProvider() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.CloudProvider }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) CqlshUrl() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.CqlshUrl }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) DataEndpointUrl() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.DataEndpointUrl }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) DatabaseId() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.DatabaseId }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) GrafanaUrl() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.GrafanaUrl }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) GraphqlUrl() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.GraphqlUrl }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetAstraDatabaseResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) Keyspace() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.Keyspace }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) NodeCount() pulumi.IntOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) int { return v.NodeCount }).(pulumi.IntOutput)
}

func (o GetAstraDatabaseResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) OwnerId() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.OwnerId }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) Regions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) []string { return v.Regions }).(pulumi.StringArrayOutput)
}

func (o GetAstraDatabaseResultOutput) ReplicationFactor() pulumi.IntOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) int { return v.ReplicationFactor }).(pulumi.IntOutput)
}

func (o GetAstraDatabaseResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) string { return v.Status }).(pulumi.StringOutput)
}

func (o GetAstraDatabaseResultOutput) TotalStorage() pulumi.IntOutput {
	return o.ApplyT(func(v GetAstraDatabaseResult) int { return v.TotalStorage }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAstraDatabaseResultOutput{})
}