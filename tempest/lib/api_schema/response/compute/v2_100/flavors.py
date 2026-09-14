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

import copy

from tempest.lib.api_schema.response.compute.v2_61 import flavors \
    as flavorsv261


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

common_flavor_info = copy.deepcopy(flavorsv261.common_flavor_info)
common_flavor_info['properties']['permissions'] = flavor_permissions
list_flavors_details = copy.deepcopy(flavorsv261.list_flavors_details)
list_flavors_details['response_body']['properties']['flavors'][
    'items'] = common_flavor_info

create_update_flavor_details = copy.deepcopy(
    flavorsv261.create_update_flavor_details)
show_flavor_details = copy.deepcopy(create_update_flavor_details)
show_flavor_details['response_body']['properties'][
    'flavor'] = common_flavor_info

# Unchanged since 2.61
list_flavors = copy.deepcopy(flavorsv261.list_flavors)
delete_flavor = copy.deepcopy(flavorsv261.delete_flavor)
