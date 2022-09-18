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

import copy

update_quota_set = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'quota_set': {
                'type': 'object',
                'properties': {
                    'instances': {'type': 'integer'},
                    'cores': {'type': 'integer'},
                    'ram': {'type': 'integer'},
                    'floating_ips': {'type': 'integer'},
                    'fixed_ips': {'type': 'integer'},
                    'metadata_items': {'type': 'integer'},
                    'key_pairs': {'type': 'integer'},
                    'security_groups': {'type': 'integer'},
                    'security_group_rules': {'type': 'integer'},
                    'server_group_members': {'type': 'integer'},
                    'server_groups': {'type': 'integer'},
                    'injected_files': {'type': 'integer'},
                    'injected_file_content_bytes': {'type': 'integer'},
                    'injected_file_path_bytes': {'type': 'integer'},
                    'instances_baremetal':  {'type': 'integer'},
                    'instances_bm091':  {'type': 'integer'},
                    'instances_hv_s2_c14_m256': {'type': 'integer'},
                    'instances_hv_s2_c20_m384': {'type': 'integer'},
                    'instances_hv_s2_c26_m384': {'type': 'integer'},
                    'instances_hv_s2_c26_m768': {'type': 'integer'},
                    'instances_hv_s2_c4_m128': {'type': 'integer'},
                    'instances_hv_s4_c24_m3072': {'type': 'integer'},
                    'instances_hv_s8_c24_m6144': {'type': 'integer'},
                    'instances_inspection_test': {'type': 'integer'},
                    'instances_lol':  {'type': 'integer'},
                    'instances_testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest': {'type': 'integer'},
                    'instances_zg1bcm1.1medium': {'type': 'integer'},
                    'instances_zg1bcm1.medium': {'type': 'integer'},
                    'instances_zg1int1.medium': {'type': 'integer'},
                    'instances_zg1mlx1.medium': {'type': 'integer'},
                    'instances_zh2mlx1.2xlarge': {'type': 'integer'},
                    'instances_zh2mlx1.3xlarge': {'type': 'integer'},
                    'instances_zh2mlx1.large': {'type': 'integer'},
                    'instances_zh2mlx1.large.pg': {'type': 'integer'},
                    'instances_zh2mlx1.xlarge': {'type': 'integer'},
                    'instances_test': {'type': 'integer'},
                    'instances_1e6ba124-7afe-4216-9844-93eb702d1c9c': {'type': 'integer'},
                    'instances_ce9a0673-3b0b-4a21-9ab6-ba9317c0da84': {'type': 'integer'},
                    'instances_5f93611f-b57f-4f20-8041-4046c65a8570': {'type': 'integer'},
                    'instances_hv_s2_c20_m384_vsmp': {'type': 'integer'},
                    'instances_f8dceaca-fe74-432a-b3e7-db1e8a85eadc': {'type': 'integer'},
                    'instances_5f93611f-b57f-4f20-8041-4046c65a8570alt': {'type': 'integer'},
                    'instances_af0175f4-5e7d-4d0c-bc10-1fd467e95213': {'type': 'integer'},
                    'instances_fe857d2c-92e1-44e1-a4ab-7f5b24c8b8f8': {'type': 'integer'},
                    'instances_509ba596-9e05-4ebd-92a2-531ad0f1a862': {'type': 'integer'},
                    'instances_58f1d06c-99e8-47a6-9e4b-6fa80eaca826': {'type': 'integer'},
                    'instances_592c2630-d94f-4b14-b85c-7c4952d33989': {'type': 'integer'},
                },
                'additionalProperties': False,
                # NOTE: server_group_members and server_groups are represented
                # when enabling quota_server_group extension. So they should
                # not be required.
                'required': ['instances', 'cores', 'ram',
                             'floating_ips', 'fixed_ips',
                             'metadata_items', 'key_pairs',
                             'security_groups', 'security_group_rules',
                             'injected_files', 'injected_file_content_bytes',
                             'injected_file_path_bytes']
            }
        },
        'additionalProperties': False,
        'required': ['quota_set']
    }
}

get_quota_set = copy.deepcopy(update_quota_set)
get_quota_set['response_body']['properties']['quota_set']['properties'][
    'id'] = {'type': 'string'}
get_quota_set['response_body']['properties']['quota_set']['required'].extend([
    'id'])

get_quota_set_details = copy.deepcopy(get_quota_set)
get_quota_set_details['response_body']['properties']['quota_set'][
    'properties'] = {
    'id': {'type': 'string'},
    'instances': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'cores': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'ram': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'floating_ips': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'fixed_ips': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'metadata_items': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'key_pairs': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'security_groups': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'security_group_rules': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'server_group_members': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'server_groups': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'injected_files': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'injected_file_content_bytes': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    },
    'injected_file_path_bytes': {
        'type': 'object',
        'properties': {
            'reserved': {'type': 'integer'},
            'limit': {'type': 'integer'},
            'in_use': {'type': 'integer'}
        }
    }
}

delete_quota = {
    'status_code': [202]
}
