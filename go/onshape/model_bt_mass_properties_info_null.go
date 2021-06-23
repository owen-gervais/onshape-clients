/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.133.27428.63074130d61b
 * Contact: api-support@onshape.zendesk.com
 */

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package onshape

import (
	"encoding/json"
)

// BTMassPropertiesInfoNull struct for BTMassPropertiesInfoNull
type BTMassPropertiesInfoNull struct {
	PrincipalInertia *[]float64       `json:"principalInertia,omitempty"`
	PrincipalAxes    *[]BTVector3d389 `json:"principalAxes,omitempty"`
	HasMass_         *bool            `json:"hasMass,omitempty"`
	Mass             *[]float64       `json:"mass,omitempty"`
	Volume           *[]float64       `json:"volume,omitempty"`
	Periphery        *[]float64       `json:"periphery,omitempty"`
	Centroid         *[]float64       `json:"centroid,omitempty"`
	Inertia          *[]float64       `json:"inertia,omitempty"`
	MassMissingCount *int32           `json:"massMissingCount,omitempty"`
}

// NewBTMassPropertiesInfoNull instantiates a new BTMassPropertiesInfoNull object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewBTMassPropertiesInfoNull() *BTMassPropertiesInfoNull {
	this := BTMassPropertiesInfoNull{}
	return &this
}

// NewBTMassPropertiesInfoNullWithDefaults instantiates a new BTMassPropertiesInfoNull object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewBTMassPropertiesInfoNullWithDefaults() *BTMassPropertiesInfoNull {
	this := BTMassPropertiesInfoNull{}
	return &this
}

// GetPrincipalInertia returns the PrincipalInertia field value if set, zero value otherwise.
func (o *BTMassPropertiesInfoNull) GetPrincipalInertia() []float64 {
	if o == nil || o.PrincipalInertia == nil {
		var ret []float64
		return ret
	}
	return *o.PrincipalInertia
}

// GetPrincipalInertiaOk returns a tuple with the PrincipalInertia field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMassPropertiesInfoNull) GetPrincipalInertiaOk() (*[]float64, bool) {
	if o == nil || o.PrincipalInertia == nil {
		return nil, false
	}
	return o.PrincipalInertia, true
}

// HasPrincipalInertia returns a boolean if a field has been set.
func (o *BTMassPropertiesInfoNull) HasPrincipalInertia() bool {
	if o != nil && o.PrincipalInertia != nil {
		return true
	}

	return false
}

// SetPrincipalInertia gets a reference to the given []float64 and assigns it to the PrincipalInertia field.
func (o *BTMassPropertiesInfoNull) SetPrincipalInertia(v []float64) {
	o.PrincipalInertia = &v
}

// GetPrincipalAxes returns the PrincipalAxes field value if set, zero value otherwise.
func (o *BTMassPropertiesInfoNull) GetPrincipalAxes() []BTVector3d389 {
	if o == nil || o.PrincipalAxes == nil {
		var ret []BTVector3d389
		return ret
	}
	return *o.PrincipalAxes
}

// GetPrincipalAxesOk returns a tuple with the PrincipalAxes field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMassPropertiesInfoNull) GetPrincipalAxesOk() (*[]BTVector3d389, bool) {
	if o == nil || o.PrincipalAxes == nil {
		return nil, false
	}
	return o.PrincipalAxes, true
}

// HasPrincipalAxes returns a boolean if a field has been set.
func (o *BTMassPropertiesInfoNull) HasPrincipalAxes() bool {
	if o != nil && o.PrincipalAxes != nil {
		return true
	}

	return false
}

// SetPrincipalAxes gets a reference to the given []BTVector3d389 and assigns it to the PrincipalAxes field.
func (o *BTMassPropertiesInfoNull) SetPrincipalAxes(v []BTVector3d389) {
	o.PrincipalAxes = &v
}

// GetHasMass returns the HasMass field value if set, zero value otherwise.
func (o *BTMassPropertiesInfoNull) GetHasMass() bool {
	if o == nil || o.HasMass_ == nil {
		var ret bool
		return ret
	}
	return *o.HasMass_
}

// GetHasMassOk returns a tuple with the HasMass field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMassPropertiesInfoNull) GetHasMassOk() (*bool, bool) {
	if o == nil || o.HasMass_ == nil {
		return nil, false
	}
	return o.HasMass_, true
}

// HasHasMass returns a boolean if a field has been set.
func (o *BTMassPropertiesInfoNull) HasHasMass() bool {
	if o != nil && o.HasMass_ != nil {
		return true
	}

	return false
}

// SetHasMass gets a reference to the given bool and assigns it to the HasMass field.
func (o *BTMassPropertiesInfoNull) SetHasMass(v bool) {
	o.HasMass_ = &v
}

// GetMass returns the Mass field value if set, zero value otherwise.
func (o *BTMassPropertiesInfoNull) GetMass() []float64 {
	if o == nil || o.Mass == nil {
		var ret []float64
		return ret
	}
	return *o.Mass
}

// GetMassOk returns a tuple with the Mass field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMassPropertiesInfoNull) GetMassOk() (*[]float64, bool) {
	if o == nil || o.Mass == nil {
		return nil, false
	}
	return o.Mass, true
}

// HasMass returns a boolean if a field has been set.
func (o *BTMassPropertiesInfoNull) HasMass() bool {
	if o != nil && o.Mass != nil {
		return true
	}

	return false
}

// SetMass gets a reference to the given []float64 and assigns it to the Mass field.
func (o *BTMassPropertiesInfoNull) SetMass(v []float64) {
	o.Mass = &v
}

// GetVolume returns the Volume field value if set, zero value otherwise.
func (o *BTMassPropertiesInfoNull) GetVolume() []float64 {
	if o == nil || o.Volume == nil {
		var ret []float64
		return ret
	}
	return *o.Volume
}

// GetVolumeOk returns a tuple with the Volume field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMassPropertiesInfoNull) GetVolumeOk() (*[]float64, bool) {
	if o == nil || o.Volume == nil {
		return nil, false
	}
	return o.Volume, true
}

// HasVolume returns a boolean if a field has been set.
func (o *BTMassPropertiesInfoNull) HasVolume() bool {
	if o != nil && o.Volume != nil {
		return true
	}

	return false
}

// SetVolume gets a reference to the given []float64 and assigns it to the Volume field.
func (o *BTMassPropertiesInfoNull) SetVolume(v []float64) {
	o.Volume = &v
}

// GetPeriphery returns the Periphery field value if set, zero value otherwise.
func (o *BTMassPropertiesInfoNull) GetPeriphery() []float64 {
	if o == nil || o.Periphery == nil {
		var ret []float64
		return ret
	}
	return *o.Periphery
}

// GetPeripheryOk returns a tuple with the Periphery field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMassPropertiesInfoNull) GetPeripheryOk() (*[]float64, bool) {
	if o == nil || o.Periphery == nil {
		return nil, false
	}
	return o.Periphery, true
}

// HasPeriphery returns a boolean if a field has been set.
func (o *BTMassPropertiesInfoNull) HasPeriphery() bool {
	if o != nil && o.Periphery != nil {
		return true
	}

	return false
}

// SetPeriphery gets a reference to the given []float64 and assigns it to the Periphery field.
func (o *BTMassPropertiesInfoNull) SetPeriphery(v []float64) {
	o.Periphery = &v
}

// GetCentroid returns the Centroid field value if set, zero value otherwise.
func (o *BTMassPropertiesInfoNull) GetCentroid() []float64 {
	if o == nil || o.Centroid == nil {
		var ret []float64
		return ret
	}
	return *o.Centroid
}

// GetCentroidOk returns a tuple with the Centroid field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMassPropertiesInfoNull) GetCentroidOk() (*[]float64, bool) {
	if o == nil || o.Centroid == nil {
		return nil, false
	}
	return o.Centroid, true
}

// HasCentroid returns a boolean if a field has been set.
func (o *BTMassPropertiesInfoNull) HasCentroid() bool {
	if o != nil && o.Centroid != nil {
		return true
	}

	return false
}

// SetCentroid gets a reference to the given []float64 and assigns it to the Centroid field.
func (o *BTMassPropertiesInfoNull) SetCentroid(v []float64) {
	o.Centroid = &v
}

// GetInertia returns the Inertia field value if set, zero value otherwise.
func (o *BTMassPropertiesInfoNull) GetInertia() []float64 {
	if o == nil || o.Inertia == nil {
		var ret []float64
		return ret
	}
	return *o.Inertia
}

// GetInertiaOk returns a tuple with the Inertia field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMassPropertiesInfoNull) GetInertiaOk() (*[]float64, bool) {
	if o == nil || o.Inertia == nil {
		return nil, false
	}
	return o.Inertia, true
}

// HasInertia returns a boolean if a field has been set.
func (o *BTMassPropertiesInfoNull) HasInertia() bool {
	if o != nil && o.Inertia != nil {
		return true
	}

	return false
}

// SetInertia gets a reference to the given []float64 and assigns it to the Inertia field.
func (o *BTMassPropertiesInfoNull) SetInertia(v []float64) {
	o.Inertia = &v
}

// GetMassMissingCount returns the MassMissingCount field value if set, zero value otherwise.
func (o *BTMassPropertiesInfoNull) GetMassMissingCount() int32 {
	if o == nil || o.MassMissingCount == nil {
		var ret int32
		return ret
	}
	return *o.MassMissingCount
}

// GetMassMissingCountOk returns a tuple with the MassMissingCount field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *BTMassPropertiesInfoNull) GetMassMissingCountOk() (*int32, bool) {
	if o == nil || o.MassMissingCount == nil {
		return nil, false
	}
	return o.MassMissingCount, true
}

// HasMassMissingCount returns a boolean if a field has been set.
func (o *BTMassPropertiesInfoNull) HasMassMissingCount() bool {
	if o != nil && o.MassMissingCount != nil {
		return true
	}

	return false
}

// SetMassMissingCount gets a reference to the given int32 and assigns it to the MassMissingCount field.
func (o *BTMassPropertiesInfoNull) SetMassMissingCount(v int32) {
	o.MassMissingCount = &v
}

func (o BTMassPropertiesInfoNull) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if o.PrincipalInertia != nil {
		toSerialize["principalInertia"] = o.PrincipalInertia
	}
	if o.PrincipalAxes != nil {
		toSerialize["principalAxes"] = o.PrincipalAxes
	}
	if o.HasMass_ != nil {
		toSerialize["hasMass"] = o.HasMass_
	}
	if o.Mass != nil {
		toSerialize["mass"] = o.Mass
	}
	if o.Volume != nil {
		toSerialize["volume"] = o.Volume
	}
	if o.Periphery != nil {
		toSerialize["periphery"] = o.Periphery
	}
	if o.Centroid != nil {
		toSerialize["centroid"] = o.Centroid
	}
	if o.Inertia != nil {
		toSerialize["inertia"] = o.Inertia
	}
	if o.MassMissingCount != nil {
		toSerialize["massMissingCount"] = o.MassMissingCount
	}
	return json.Marshal(toSerialize)
}

type NullableBTMassPropertiesInfoNull struct {
	value *BTMassPropertiesInfoNull
	isSet bool
}

func (v NullableBTMassPropertiesInfoNull) Get() *BTMassPropertiesInfoNull {
	return v.value
}

func (v *NullableBTMassPropertiesInfoNull) Set(val *BTMassPropertiesInfoNull) {
	v.value = val
	v.isSet = true
}

func (v NullableBTMassPropertiesInfoNull) IsSet() bool {
	return v.isSet
}

func (v *NullableBTMassPropertiesInfoNull) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableBTMassPropertiesInfoNull(val *BTMassPropertiesInfoNull) *NullableBTMassPropertiesInfoNull {
	return &NullableBTMassPropertiesInfoNull{value: val, isSet: true}
}

func (v NullableBTMassPropertiesInfoNull) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableBTMassPropertiesInfoNull) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}
