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

get_limit = {
    'status_code': [200],
    'response_body': {
        'type': 'object',
        'properties': {
            'limits': {
                'type': 'object',
                'properties': {
                    'absolute': {
                        'type': 'object',
                        'properties': {
                            'maxTotalRAMSize': {'type': 'integer'},
                            'totalCoresUsed': {'type': 'integer'},
                            'maxTotalInstances': {'type': 'integer'},
                            'maxTotalFloatingIps': {'type': 'integer'},
                            'totalSecurityGroupsUsed': {'type': 'integer'},
                            'maxTotalCores': {'type': 'integer'},
                            'totalFloatingIpsUsed': {'type': 'integer'},
                            'maxSecurityGroups': {'type': 'integer'},
                            'maxServerMeta': {'type': 'integer'},
                            'maxPersonality': {'type': 'integer'},
                            'maxImageMeta': {'type': 'integer'},
                            'maxPersonalitySize': {'type': 'integer'},
                            'maxSecurityGroupRules': {'type': 'integer'},
                            'maxTotalKeypairs': {'type': 'integer'},
                            'totalRAMUsed': {'type': 'integer'},
                            'totalInstancesUsed': {'type': 'integer'},
                            'maxServerGroupMembers': {'type': 'integer'},
                            'maxServerGroups': {'type': 'integer'},
                            'totalServerGroupsUsed': {'type': 'integer'}
                        },
                        'additionalProperties': False,
                        # NOTE(gmann): maxServerGroupMembers,  maxServerGroups
                        # and totalServerGroupsUsed are API extension,
                        # and some environments return a response without these
                        # attributes.So they are not 'required'.
                        'required': ['maxImageMeta',
                                     'maxPersonality',
                                     'maxPersonalitySize',
                                     'maxSecurityGroupRules',
                                     'maxSecurityGroups',
                                     'maxServerMeta',
                                     'maxTotalCores',
                                     'maxTotalFloatingIps',
                                     'maxTotalInstances',
                                     'maxTotalKeypairs',
                                     'maxTotalRAMSize',
                                     'totalCoresUsed',
                                     'totalFloatingIpsUsed',
                                     'totalInstancesUsed',
                                     'totalRAMUsed',
                                     'totalSecurityGroupsUsed']
                    },
                    'absolutePerFlavor': {
                        'baremetal': {
                            'maxTotalInstances': {
                                'type': 'integer'
                            },
                            'totalInstancesUsed': {
                                'type': 'integer'}
                        },
                        'bm091': {
                            'maxTotalInstances': {'type': 'integer'
                                                  },
                            'totalInstancesUsed': {
                                'type': 'integer'
                            }
                        },
                        'hv_s2_c14_m256': {'maxTotalInstances': {'type': 'integer'},
                                           'totalInstancesUsed': {'type': 'integer'}},
                        'hv_s2_c20_m384': {'maxTotalInstances': {'type': 'integer'},
                                           'totalInstancesUsed': {'type': 'integer'}},
                        'hv_s2_c26_m384': {'maxTotalInstances': {'type': 'integer'},
                                           'totalInstancesUsed': {'type': 'integer'}},
                        'hv_s2_c26_m768': {'maxTotalInstances': {'type': 'integer'},
                                           'totalInstancesUsed': {'type': 'integer'}},
                        'hv_s2_c4_m128': {'maxTotalInstances': {'type': 'integer'},
                                          'totalInstancesUsed': {'type': 'integer'}},
                        'hv_s4_c24_m3072': {'maxTotalInstances': {'type': 'integer'},
                                            'totalInstancesUsed': {'type': 'integer'}},
                        'hv_s8_c24_m6144': {'maxTotalInstances': {'type': 'integer'},
                                            'totalInstancesUsed': {'type': 'integer'}},
                        'inspection_test': {'maxTotalInstances': {'type': 'integer'},
                                            'totalInstancesUsed': {'type': 'integer'}},
                        'lol': {'maxTotalInstances': {'type': 'integer'},
                                'totalInstancesUsed': {'type': 'integer'}},
                        'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest': {
                                              'maxTotalInstances': {'type': 'integer'},
                                              'totalInstancesUsed': {'type': 'integer'}},
                        'zg1bcm1.1medium': {'maxTotalInstances': {'type': 'integer'},
                                            'totalInstancesUsed': {'type': 'integer'}},
                        'zg1bcm1.medium': {'maxTotalInstances': {'type': 'integer'},
                                           'totalInstancesUsed': {'type': 'integer'}},
                        'zg1int1.medium': {'maxTotalInstances': {'type': 'integer'},
                                           'totalInstancesUsed': {'type': 'integer'}},
                        'zg1mlx1.medium': {'maxTotalInstances': {'type': 'integer'},
                                           'totalInstancesUsed': {'type': 'integer'}},
                        'zh2mlx1.2xlarge': {'maxTotalInstances': {'type': 'integer'},
                                            'totalInstancesUsed': {'type': 'integer'}},
                        'zh2mlx1.3xlarge': {'maxTotalInstances': {'type': 'integer'},
                                            'totalInstancesUsed': {'type': 'integer'}},
                        'zh2mlx1.large': {'maxTotalInstances': {'type': 'integer'},
                                          'totalInstancesUsed': {'type': 'integer'}},
                        'zh2mlx1.large.pg': {'maxTotalInstances': {'type': 'integer'},
                                             'totalInstancesUsed': {'type': 'integer'}},
                        'zh2mlx1.xlarge': {'maxTotalInstances': {'type': 'integer'},
                                           'totalInstancesUsed': {'type': 'integer'}}},
                    'rate': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'limit': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'next-available':
                                                {'type': 'string'},
                                            'remaining':
                                                {'type': 'integer'},
                                            'unit':
                                                {'type': 'string'},
                                            'value':
                                                {'type': 'integer'},
                                            'verb':
                                                {'type': 'string'}
                                        },
                                        'additionalProperties': False,
                                    }
                                },
                                'regex': {'type': 'string'},
                                'uri': {'type': 'string'}
                            },
                            'additionalProperties': False,
                        }
                    }
                },
                'additionalProperties': False,
                'required': ['absolute', 'rate']
            }
        },
        'additionalProperties': False,
        'required': ['limits']
    }
}
