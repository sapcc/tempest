# Copyright 2014 NEC Corporation.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.lib.api_schema.response.compute.v2_1 import parameter_types

# SAP flavor permission rules annotation, emitted on flavor detail/show for
# callers holding the os-flavor-permission-rules index:domain / index:project
# policy. The key is present (possibly empty) for such callers, absent
# otherwise, so it is optional here.
flavor_permissions = {
    'type': 'object',
    'properties': {
        'domain': {'type': 'string', 'enum': ['allow', 'deny']},
        'project': {'type': 'string', 'enum': ['allow', 'deny']},
    },
    'additionalProperties': False,
}

list_flavors = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'flavors': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'},
                        'links': parameter_types.links,
                        'id': {'type': 'string'}
                    },
                    'additionalProperties': False,
                    'required': ['name', 'links', 'id']
                }
            },
            'flavors_links': parameter_types.links
        },
        'additionalProperties': False,
        # NOTE(gmann): flavors_links attribute is not necessary
        # to be present always So it is not 'required'.
        'required': ['flavors']
    }
}

common_flavor_info = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'links': parameter_types.links,
        'ram': {'type': 'integer'},
        'vcpus': {'type': 'integer'},
        # 'swap' attributes comes as integer value but if it is empty
        # it comes as "". So defining type of as string and integer.
        'swap': {'type': ['integer', 'string']},
        'disk': {'type': 'integer'},
        'id': {'type': 'string'},
        'OS-FLV-DISABLED:disabled': {'type': 'boolean'},
        'os-flavor-access:is_public': {'type': 'boolean'},
        'rxtx_factor': {'type': 'number'},
        'OS-FLV-EXT-DATA:ephemeral': {'type': 'integer'},
    },
    'additionalProperties': False,
    # 'OS-FLV-DISABLED', 'os-flavor-access', 'rxtx_factor' and
    # 'OS-FLV-EXT-DATA' are API extensions, so they are not 'required'.
    'required': ['name', 'links', 'ram', 'vcpus', 'swap', 'disk', 'id']
}

list_flavors_details = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'flavors': {
                'type': 'array',
                'items': common_flavor_info
            },
            # NOTE(gmann): flavors_links attribute is not necessary
            # to be present always so it is not 'required'.
            'flavors_links': parameter_types.links
        },
        'additionalProperties': False,
        'required': ['flavors']
    }
}

create_update_flavor_details = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'flavor': common_flavor_info
        },
        'additionalProperties': False,
        'required': ['flavor']
    }
}

show_flavor_details = create_update_flavor_details

delete_flavor = {
    'status_code': [202]
}
