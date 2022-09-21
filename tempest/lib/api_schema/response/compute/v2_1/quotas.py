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
                    'instances_0f0ee73a-db11-41ba-8b17-0ee6af20e54d': {'type': 'integer'},
                    'instances_059c7ae5-6e3e-45f8-a403-cfba75935bc4': {'type': 'integer'},
                    'instances_3ae8e30e-e29e-4d20-bc88-bf7a53d23141': {'type': 'integer'},
                    'instances_5e2108d7-0822-447e-be98-d7d79cc94089': {'type': 'integer'},
                    'instances_6afdb65c-0a4c-4f06-bfc4-5a5813c3979f': {'type': 'integer'},
                    'instances_081e43b1-078e-420a-b6b3-eb0a976ed03d': {'type': 'integer'},
                    'instances_91718adb-4ac1-4357-ac37-32668f31b208': {'type': 'integer'},
                    'instances_f1667564-9bb9-469a-9c74-157a613c5097': {'type': 'integer'},
                    'instances_b13def96-22e1-4fbd-905d-f0c93758d064': {'type': 'integer'},
                    'instances_dfd6159e-29ae-4316-adca-20206307444b': {'type': 'integer'},
                    'instances_02dcd4ee-7467-4029-b8b1-473869d73086': {'type': 'integer'},
                    'instances_3fd59b42-56fa-4dc3-82fa-20e7ab257568': {'type': 'integer'},
                    'instances_0ba299f1-b283-4419-8bc8-23976ce867da': {'type': 'integer'},
                    'instances_3ae8e30e-e29e-4d20-bc88-bf7a53d23141alt': {'type': 'integer'},
                    'instances_7827f180-9064-4b0b-a800-460cb66812a7': {'type': 'integer'},
                    'instances_d043fa78-b849-435b-83a0-383655dd8746': {'type': 'integer'},
                    'instances_1fbc0b2a-3a92-4deb-ae8f-ea6035a54830': {'type': 'integer'},
                    'instances_43c5c4d2-c87d-47c3-8a2d-46be38859692': {'type': 'integer'},
                    'instances_198868d8-8ad9-4ccc-aa5b-f2831c5267f7': {'type': 'integer'},
                    'instances_3dce86de-fecc-4467-ad5d-abc9a03a43aa': {'type': 'integer'},
                    'instances_7f09d7d5-e2a8-4bf1-9106-eeccd4d280d4': {'type': 'integer'},
                    'instances_a170a28f-f753-4a0e-9c3d-0ab9293df4a4': {'type': 'integer'},
                    'instances_1ea91da7-4e04-4ffb-a68a-dddcaeb8e88a': {'type': 'integer'},
                    'instances_22be8bbf-a9bc-4767-b804-5d972d9414af': {'type': 'integer'},
                    'instances_8566ff01-2345-473e-b04f-20b0eb948170': {'type': 'integer'},
                    'instances_f4a826a5-6b59-4618-9da3-b197a8d0215dalt': {'type': 'integer'},
                    'instances_db47fd19-2924-46ca-b992-1383dfa7e3c4': {'type': 'integer'},
                    'instances_edfd3e87-a796-4422-8340-a68345a41d31': {'type': 'integer'},
                    'instances_f4a826a5-6b59-4618-9da3-b197a8d0215d': {'type': 'integer'},
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
