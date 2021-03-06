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

import { BTConnection } from './bTConnection';
import { BTExportTessellatedFacesFacet } from './bTExportTessellatedFacesFacet';

export class BTExportTessellatedFacesFace {
    'id'?: string;
    'errorMessage'?: string;
    'facets'?: Array<BTExportTessellatedFacesFacet>;
    'typeId'?: number;
    'exportTypeName'?: string;
    'connectionSource'?: BTConnection;
    'unknownClass'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "errorMessage",
            "baseName": "errorMessage",
            "type": "string"
        },
        {
            "name": "facets",
            "baseName": "facets",
            "type": "Array<BTExportTessellatedFacesFacet>"
        },
        {
            "name": "typeId",
            "baseName": "typeId",
            "type": "number"
        },
        {
            "name": "exportTypeName",
            "baseName": "exportTypeName",
            "type": "string"
        },
        {
            "name": "connectionSource",
            "baseName": "connectionSource",
            "type": "BTConnection"
        },
        {
            "name": "unknownClass",
            "baseName": "unknownClass",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return BTExportTessellatedFacesFace.attributeTypeMap;
    }
}

