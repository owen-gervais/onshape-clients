/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// BtParameterGroupSpec3469 struct for BtParameterGroupSpec3469
type BtParameterGroupSpec3469 struct {
	AdditionalLocalizedStrings int32 `json:"additionalLocalizedStrings,omitempty"`
	CollapsedByDefault bool `json:"collapsedByDefault,omitempty"`
	DrivingParameterId string `json:"drivingParameterId,omitempty"`
	GroupId string `json:"groupId,omitempty"`
	GroupName string `json:"groupName,omitempty"`
	GroupOrParameterIds []string `json:"groupOrParameterIds,omitempty"`
	LocalizableName string `json:"localizableName,omitempty"`
	LocalizedName string `json:"localizedName,omitempty"`
	StringsToLocalize []string `json:"stringsToLocalize,omitempty"`
}