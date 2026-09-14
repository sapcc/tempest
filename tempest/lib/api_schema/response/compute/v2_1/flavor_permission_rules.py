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
        'created_at': parameter_types.date_time,
        'domain_id': {'type': 'string'},
        'effect': {'type': 'string', 'enum': ['allow', 'deny']},
        'flavor_id': {'type': ['string', 'null']},
        'id': {'type': 'string'},
        'links': parameter_types.links,
        'project_id': {'type': ['string', 'null']},
        'scope': {'type': 'string', 'enum': ['domain', 'project']},
        'updated_at': parameter_types.date_time_or_null,
    },
    'additionalProperties': False,
    'required': ['domain_id', 'effect', 'flavor_id', 'id', 'links',
                 'project_id', 'scope'],
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
