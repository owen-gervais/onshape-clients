/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export class BTSeatsParams {
    'lightSeats'?: number;
    'userId'?: string;
    'seats'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "lightSeats",
            "baseName": "lightSeats",
            "type": "number"
        },
        {
            "name": "userId",
            "baseName": "userId",
            "type": "string"
        },
        {
            "name": "seats",
            "baseName": "seats",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return BTSeatsParams.attributeTypeMap;
    }
}

