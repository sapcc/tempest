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

from tempest.api.compute import base
from tempest.lib.common.utils import data_utils
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc


class FlavorPermissionRulesNegativeTest(base.BaseV2ComputeTest):

    min_microversion = '2.100'

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('aa09f353-33f4-44b4-912e-f4fc1d8d95f9')
    def test_unauthorized(self):
        """Requests raise Forbidden or NotFound"""
        rule_id = data_utils.rand_uuid()
        nc = self.flavor_permission_rules_client
        self.assertRaises(lib_exc.Forbidden,
                          nc.list_flavor_permission_rules)
        self.assertRaises(lib_exc.Forbidden,
                          nc.create_flavor_permission_rule,
                          domain_id=data_utils.rand_uuid(), effect='deny')
        self.assertRaises(lib_exc.NotFound,
                          nc.show_flavor_permission_rule, rule_id)
        self.assertRaises(lib_exc.NotFound,
                          nc.update_flavor_permission_rule, rule_id,
                          effect='allow')
        self.assertRaises(lib_exc.NotFound,
                          nc.delete_flavor_permission_rule, rule_id)
