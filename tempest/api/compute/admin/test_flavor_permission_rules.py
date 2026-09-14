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

from oslo_utils import uuidutils

from tempest.api.compute import base
from tempest import config
from tempest.lib.common.utils import data_utils
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc

CONF = config.CONF


class FlavorPermissionRulesAdminTest(base.BaseV2ComputeAdminTest):
    """Tests the flavor permission rules API with admin privileges.

    All policies default to admin, whose check_str carries no caller
    domain or project match, so the admin may manage rules for any domain_id
    and project_id. The endpoint does not validate them against keystone, so
    the management tests use synthetic random ids for isolating flavor
    permission rule testing.
    """

    min_microversion = '2.100'

    @classmethod
    def resource_setup(cls):
        super(FlavorPermissionRulesAdminTest, cls).resource_setup()
        cls.client = cls.admin_flavor_permission_rules_client
        # Shared fixtures with synthetic domain and project ids for list tests
        cls.flavor_ref = CONF.compute.flavor_ref
        cls.flavor_ref_alt = CONF.compute.flavor_ref_alt
        cls.domain_id = data_utils.rand_uuid()
        cls.domain_id_alt = data_utils.rand_uuid()
        cls.project_id = data_utils.rand_uuid()
        cls.project_id_alt = data_utils.rand_uuid()
        cls.domain_deny = cls.create_flavor_permission_rule(
            domain_id=cls.domain_id, effect='deny')
        cls.domain_allow_flavor = cls.create_flavor_permission_rule(
            domain_id=cls.domain_id, effect='allow',
            flavor_id=cls.flavor_ref)
        cls.project_allow = cls.create_flavor_permission_rule(
            domain_id=cls.domain_id, project_id=cls.project_id, effect='allow')
        cls.other_project_deny_flavor = cls.create_flavor_permission_rule(
            domain_id=cls.domain_id, project_id=cls.project_id_alt,
            effect='deny', flavor_id=cls.flavor_ref_alt)
        cls.other_domain_allow = cls.create_flavor_permission_rule(
            domain_id=cls.domain_id_alt, effect='allow')

    def _list_ids(self, **filters):
        return {r['id'] for r in self.client.list_flavor_permission_rules(
            **filters)['flavor_permission_rules']}

    def _assert_rule(self, expected, actual):
        """Assert a returned rule matches the expected values."""
        self.assertTrue(uuidutils.is_uuid_like(actual['id']),
                        f"rule id {actual['id']} is not a uuid")
        self.assertEqual(expected['domain_id'], actual['domain_id'])
        self.assertEqual(expected.get('project_id'), actual['project_id'])
        self.assertEqual(expected.get('flavor_id'), actual['flavor_id'])
        self.assertEqual(expected['effect'], actual['effect'])
        expected_scope = 'project' if expected.get('project_id') else 'domain'
        self.assertEqual(expected_scope, actual['scope'])

    @decorators.idempotent_id('2d6b935a-ec9e-437e-8a8b-0f9cefefccff')
    def test_create_show_delete_domain_rule(self):
        """Create, show and delete a domain-scoped flavor permission rule."""
        params = dict(domain_id=data_utils.rand_uuid(), effect='deny')
        rule = self.create_flavor_permission_rule(**params)
        self._assert_rule(params, rule)

        shown = self.client.show_flavor_permission_rule(
            rule['id'])['flavor_permission_rule']
        self._assert_rule(params, shown)

        self.client.delete_flavor_permission_rule(rule['id'])
        self.assertRaises(lib_exc.NotFound,
                          self.client.show_flavor_permission_rule, rule['id'])

    @decorators.idempotent_id('5abdefbd-d953-4aa8-a6c5-304b286547f2')
    def test_create_project_rule(self):
        """A rule with a project_id is project-scoped."""
        params = dict(domain_id=data_utils.rand_uuid(),
                      project_id=data_utils.rand_uuid(), effect='deny')
        rule = self.create_flavor_permission_rule(**params)
        self._assert_rule(params, rule)

    @decorators.idempotent_id('501f9c21-137e-46de-b28b-a83e5f6372c5')
    def test_create_flavor_scoped_rule(self):
        """A flavor-scoped rule echoes the public flavor ref."""
        params = dict(domain_id=data_utils.rand_uuid(), effect='allow',
                      flavor_id=self.flavor_ref)
        rule = self.create_flavor_permission_rule(**params)
        self._assert_rule(params, rule)

    @decorators.idempotent_id('e138b518-0da7-45b0-b5c0-57de59bb41a0')
    def test_update_show_rule_effect(self):
        """The effect of a rule can be updated."""
        rule = self.create_flavor_permission_rule(
            domain_id=data_utils.rand_uuid(), effect='deny')

        updated = self.client.update_flavor_permission_rule(
            rule['id'], effect='allow')['flavor_permission_rule']
        self.assertEqual('allow', updated['effect'])

        shown = self.client.show_flavor_permission_rule(
            rule['id'])['flavor_permission_rule']
        self.assertEqual('allow', shown['effect'])

    @decorators.idempotent_id('b409a77f-1d21-4fa9-9913-b623803483ab')
    def test_list_filter_by_domain_id(self):
        """Filter by domain_id"""
        self.assertEqual(
            {self.domain_deny['id'], self.domain_allow_flavor['id'],
             self.project_allow['id'], self.other_project_deny_flavor['id']},
            self._list_ids(domain_id=self.domain_id))
        self.assertEqual({self.other_domain_allow['id']},
                         self._list_ids(domain_id=self.domain_id_alt))

    @decorators.idempotent_id('90a8a227-4084-4e02-893c-b3c1b0ea768e')
    def test_list_filter_by_project_id(self):
        """Filter by project_id"""
        self.assertEqual({self.project_allow['id']},
                         self._list_ids(project_id=self.project_id))

    @decorators.idempotent_id('95668109-c57f-4565-8e4a-c4eba8465f7d')
    def test_list_filter_by_effect(self):
        """Filter by effect (allow/deny)"""
        self.assertEqual(
            {self.domain_allow_flavor['id'], self.project_allow['id']},
            self._list_ids(domain_id=self.domain_id, effect='allow'))
        self.assertEqual(
            {self.domain_deny['id'], self.other_project_deny_flavor['id']},
            self._list_ids(domain_id=self.domain_id, effect='deny'))

    @decorators.idempotent_id('3ca050ad-52d7-4d28-acaa-9f555d0db6fb')
    def test_list_filter_by_scope(self):
        """Filter by scope (domain/project)"""
        self.assertEqual(
            {self.project_allow['id'], self.other_project_deny_flavor['id']},
            self._list_ids(domain_id=self.domain_id, scope='project'))
        self.assertEqual(
            {self.domain_deny['id'], self.domain_allow_flavor['id']},
            self._list_ids(domain_id=self.domain_id, scope='domain'))

    @decorators.idempotent_id('50e0b13f-c340-4171-b96d-c917db1d106a')
    def test_list_filter_by_flavor_id(self):
        """Filter by flavor_id"""
        self.assertEqual(
            {self.domain_allow_flavor['id']},
            self._list_ids(
                domain_id=self.domain_id, flavor_id=self.flavor_ref))

    @decorators.idempotent_id('3291f21c-66e5-4b1a-8342-a8422b97c76f')
    def test_list_filter_by_has_flavor(self):
        """Filter by has_flavor (True/False)"""
        self.assertEqual(
            {self.domain_deny['id'], self.project_allow['id']},
            self._list_ids(domain_id=self.domain_id, has_flavor=False))
        self.assertEqual(
            {self.domain_allow_flavor['id'],
             self.other_project_deny_flavor['id']},
            self._list_ids(domain_id=self.domain_id, has_flavor=True))

    @decorators.idempotent_id('788b53aa-9013-487b-95e8-6ea68a8e9b69')
    def test_list_pagination(self):
        """Pagination with limit and marker"""
        resp = self.client.list_flavor_permission_rules(
            domain_id=self.domain_id, limit=2)
        page = resp['flavor_permission_rules']
        self.assertEqual(2, len(page))
        self.assertIn('flavor_permission_rules_links', resp)
        page_ids = {r['id'] for r in page}
        self.assertEqual(
            self._list_ids(domain_id=self.domain_id) - page_ids,
            self._list_ids(domain_id=self.domain_id, marker=page[-1]['id']))
