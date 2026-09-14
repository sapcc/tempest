# Copyright (c) 2026 SAP SE
# All Rights Reserved.
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

flavor_permission_rule = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string'},
        'domain_id': {'type': 'string'},
        'project_id': {'type': ['string', 'null']},
        'flavor_id': {'type': ['string', 'null']},
        'effect': {'type': 'string', 'enum': ['allow', 'deny']},
        'scope': {'type': 'string', 'enum': ['domain', 'project']},
        'links': parameter_types.links,
    },
    'additionalProperties': False,
    'required': ['id', 'domain_id', 'project_id', 'flavor_id', 'effect',
                 'scope', 'links'],
}

show_update_flavor_permission_rule = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'flavor_permission_rule': flavor_permission_rule,
        },
        'additionalProperties': False,
        'required': ['flavor_permission_rule'],
    }
}

# POST returns 201 with the same body shape as show/update.
create_flavor_permission_rule = {
    'status_code': [201],
    'response_body': show_update_flavor_permission_rule['response_body'],
}

list_flavor_permission_rules = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'flavor_permission_rules': {
                'type': 'array',
                'items': flavor_permission_rule,
            },
            # flavor_permission_rules_links is only present when the response
            # is paginated, so it is not 'required'.
            'flavor_permission_rules_links': parameter_types.links,
        },
        'additionalProperties': False,
        'required': ['flavor_permission_rules'],
    }
}

delete_flavor_permission_rule = {
    'status_code': [204],
}
