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
// BtSplineDescription2118 struct for BtSplineDescription2118
type BtSplineDescription2118 struct {
	BtType string `json:"btType,omitempty"`
	ControlPoints []float64 `json:"controlPoints,omitempty"`
	Degree int32 `json:"degree,omitempty"`
	IsPeriodic bool `json:"isPeriodic,omitempty"`
	IsRational bool `json:"isRational,omitempty"`
	Knots []float64 `json:"knots,omitempty"`
	Type string `json:"type,omitempty"`
}