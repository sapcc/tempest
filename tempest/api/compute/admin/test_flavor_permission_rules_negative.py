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
from tempest import config
from tempest.lib.common.utils import data_utils
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc

CONF = config.CONF


class FlavorPermissionRulesNegativeTest(base.BaseV2ComputeAdminTest):
    """
    Negative tests for the flavor permission rules API with admin privileges
    """

    @classmethod
    def resource_setup(cls):
        super(FlavorPermissionRulesNegativeTest, cls).resource_setup()
        cls.client = cls.admin_flavor_permission_rules_client

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('51973116-514d-4e0a-a96c-9ce1212bd5c0')
    def test_create_duplicate_rule(self):
        """Creating duplicate rules raises conflict"""
        domain_id = data_utils.rand_uuid()
        self.create_flavor_permission_rule(domain_id=domain_id, effect='deny')
        self.assertRaises(
            lib_exc.Conflict, self.client.create_flavor_permission_rule,
            domain_id=domain_id, effect='deny')

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('3f7ad1e1-77c5-4b55-a349-aeaad40cffa2')
    def test_create_with_nonexistent_flavor(self):
        """Creating rules for non-existent flavors raises not found"""
        self.assertRaises(
            lib_exc.NotFound, self.client.create_flavor_permission_rule,
            domain_id=data_utils.rand_uuid(), effect='allow',
            flavor_id=data_utils.rand_uuid())

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('95d87ee7-4370-4aa7-a727-ea9779ed28e6')
    def test_create_rule_for_non_public_flavor(self):
        """Creating rules for private flavors raises bad request"""
        flavor = self.create_flavor(ram=512, vcpus=1, disk=1,
                                    is_public='False')
        self.assertRaises(
            lib_exc.BadRequest, self.client.create_flavor_permission_rule,
            domain_id=data_utils.rand_uuid(), effect='allow',
            flavor_id=flavor['id'])

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('124deaa1-8178-47b2-9e29-940b6ececd6e')
    def test_create_missing_domain_id(self):
        """Creating rules without domain_id raises bad request"""
        self.assertRaises(
            lib_exc.BadRequest, self.client.create_flavor_permission_rule,
            effect='deny')

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('fd263ad5-c671-4783-b00e-c748e22e89cf')
    def test_create_missing_effect(self):
        """Creating rules without effect raises bad request."""
        self.assertRaises(
            lib_exc.BadRequest, self.client.create_flavor_permission_rule,
            domain_id=data_utils.rand_uuid())

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('49adf92b-28f9-4af1-8b38-239ca2096993')
    def test_create_invalid_effect(self):
        """Creating rules with invalid effect raises bad request"""
        self.assertRaises(
            lib_exc.BadRequest, self.client.create_flavor_permission_rule,
            domain_id=data_utils.rand_uuid(), effect='unsupported')

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('918c52e9-86d7-4a15-8765-06c741c35d37')
    def test_create_additional_property(self):
        """Creating rules with unsupported properties raises bad request"""
        self.assertRaises(
            lib_exc.BadRequest, self.client.create_flavor_permission_rule,
            domain_id=data_utils.rand_uuid(), effect='deny', unsupported='x')

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('ed625fb4-642e-43d4-9dcd-47b0f780db45')
    def test_show_update_delete_nonexistent_rule(self):
        """Show/update/delete of non-existing rules raises not found"""
        rule_id = data_utils.rand_uuid()
        self.assertRaises(lib_exc.NotFound,
                          self.client.show_flavor_permission_rule, rule_id)
        self.assertRaises(lib_exc.NotFound,
                          self.client.update_flavor_permission_rule,
                          rule_id, effect='allow')
        self.assertRaises(lib_exc.NotFound,
                          self.client.delete_flavor_permission_rule, rule_id)

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('e6a295b5-3942-41e5-af14-65bb6071e035')
    def test_update_invalid_effect(self):
        """Updating a rule with an invalid effect raises bad request"""
        rule = self.create_flavor_permission_rule(
            domain_id=data_utils.rand_uuid(), effect='deny')
        self.assertRaises(
            lib_exc.BadRequest, self.client.update_flavor_permission_rule,
            rule['id'], effect='unsupported')

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('e0856298-bc49-4cc8-b36c-69377613d1b1')
    def test_update_missing_effect(self):
        """Updating a rule without an effect raises bad request"""
        rule = self.create_flavor_permission_rule(
            domain_id=data_utils.rand_uuid(), effect='deny')
        self.assertRaises(
            lib_exc.BadRequest, self.client.update_flavor_permission_rule,
            rule['id'])

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('930edc2d-c834-464a-828d-bf07bedbdfc5')
    def test_list_flavor_id_and_has_flavor_mutually_exclusive(self):
        """Listing with both flavor_id and has_flavor raises bad request"""
        self.assertRaises(
            lib_exc.BadRequest, self.client.list_flavor_permission_rules,
            flavor_id=CONF.compute.flavor_ref, has_flavor=True)

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('529a41b5-0417-49d7-b1e3-01318e0444f3')
    def test_list_with_unknown_marker(self):
        """Listing with unknown marker raises bad request"""
        self.assertRaises(
            lib_exc.BadRequest, self.client.list_flavor_permission_rules,
            marker=data_utils.rand_uuid())

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('a9924860-e5d0-4db4-a61e-759c363428a0')
    def test_list_with_nonexistent_flavor(self):
        """Listing with a non-existent flavor raises not found"""
        self.assertRaises(
            lib_exc.NotFound, self.client.list_flavor_permission_rules,
            flavor_id=data_utils.rand_uuid())

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('9fb1910c-83cf-47e1-9b77-613dcfe6a05f')
    def test_list_with_invalid_scope(self):
        """Listing with an invalid scope filter raises bad request"""
        self.assertRaises(
            lib_exc.BadRequest, self.client.list_flavor_permission_rules,
            scope='unsupported')

    @decorators.attr(type=['negative'])
    @decorators.idempotent_id('eb7bb63e-7e6d-4087-8bf8-e50ee4938030')
    def test_list_with_invalid_has_flavor(self):
        """Listing with a non-boolean has_flavor value raises bad request"""
        self.assertRaises(
            lib_exc.BadRequest, self.client.list_flavor_permission_rules,
            has_flavor='maybe')
