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
// BtMoveElementParams struct for BtMoveElementParams
type BtMoveElementParams struct {
	AnchorElementId string `json:"anchorElementId,omitempty"`
	Description string `json:"description,omitempty"`
	ElementOriginalToNewMap map[string]string `json:"elementOriginalToNewMap,omitempty"`
	Elements []string `json:"elements,omitempty"`
	GenerateUnknownMessages bool `json:"generateUnknownMessages,omitempty"`
	ImportData []string `json:"importData,omitempty"`
	IsCopy bool `json:"isCopy,omitempty"`
	IsDeepCopy bool `json:"isDeepCopy,omitempty"`
	IsGroupAnchor bool `json:"isGroupAnchor,omitempty"`
	IsNewDocument bool `json:"isNewDocument,omitempty"`
	IsPublic bool `json:"isPublic,omitempty"`
	IsSelectivePartOut bool `json:"isSelectivePartOut,omitempty"`
	Name string `json:"name,omitempty"`
	NeedNewVersion bool `json:"needNewVersion,omitempty"`
	OwnerEmail string `json:"ownerEmail,omitempty"`
	OwnerId string `json:"ownerId,omitempty"`
	OwnerType int32 `json:"ownerType,omitempty"`
	ParentId string `json:"parentId,omitempty"`
	ProjectId string `json:"projectId,omitempty"`
	SourceDocumentId string `json:"sourceDocumentId,omitempty"`
	SourceWorkspaceId string `json:"sourceWorkspaceId,omitempty"`
	Tags []string `json:"tags,omitempty"`
	TargetDocumentId string `json:"targetDocumentId,omitempty"`
	TargetWorkspaceId string `json:"targetWorkspaceId,omitempty"`
	VersionName string `json:"versionName,omitempty"`
}