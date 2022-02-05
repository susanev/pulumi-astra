// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package astra

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupPrivateLinks(ctx *pulumi.Context, args *LookupPrivateLinksArgs, opts ...pulumi.InvokeOption) (*LookupPrivateLinksResult, error) {
	var rv LookupPrivateLinksResult
	err := ctx.Invoke("index:astra/getPrivateLinks:getPrivateLinks", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPrivateLinks.
type LookupPrivateLinksArgs struct {
	DatabaseId   string `pulumi:"databaseId"`
	DatacenterId string `pulumi:"datacenterId"`
}

// A collection of values returned by getPrivateLinks.
type LookupPrivateLinksResult struct {
	DatabaseId   string `pulumi:"databaseId"`
	DatacenterId string `pulumi:"datacenterId"`
	// The provider-assigned unique ID for this managed resource.
	Id      string                  `pulumi:"id"`
	Results []GetPrivateLinksResult `pulumi:"results"`
}

func LookupPrivateLinksOutput(ctx *pulumi.Context, args LookupPrivateLinksOutputArgs, opts ...pulumi.InvokeOption) LookupPrivateLinksResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPrivateLinksResult, error) {
			args := v.(LookupPrivateLinksArgs)
			r, err := LookupPrivateLinks(ctx, &args, opts...)
			return *r, err
		}).(LookupPrivateLinksResultOutput)
}

// A collection of arguments for invoking getPrivateLinks.
type LookupPrivateLinksOutputArgs struct {
	DatabaseId   pulumi.StringInput `pulumi:"databaseId"`
	DatacenterId pulumi.StringInput `pulumi:"datacenterId"`
}

func (LookupPrivateLinksOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPrivateLinksArgs)(nil)).Elem()
}

// A collection of values returned by getPrivateLinks.
type LookupPrivateLinksResultOutput struct{ *pulumi.OutputState }

func (LookupPrivateLinksResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPrivateLinksResult)(nil)).Elem()
}

func (o LookupPrivateLinksResultOutput) ToLookupPrivateLinksResultOutput() LookupPrivateLinksResultOutput {
	return o
}

func (o LookupPrivateLinksResultOutput) ToLookupPrivateLinksResultOutputWithContext(ctx context.Context) LookupPrivateLinksResultOutput {
	return o
}

func (o LookupPrivateLinksResultOutput) DatabaseId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPrivateLinksResult) string { return v.DatabaseId }).(pulumi.StringOutput)
}

func (o LookupPrivateLinksResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPrivateLinksResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupPrivateLinksResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPrivateLinksResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupPrivateLinksResultOutput) Results() GetPrivateLinksResultArrayOutput {
	return o.ApplyT(func(v LookupPrivateLinksResult) []GetPrivateLinksResult { return v.Results }).(GetPrivateLinksResultArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPrivateLinksResultOutput{})
}