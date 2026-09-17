# Copyright 2012 OpenStack Foundation
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

import uuid

from tempest.api.compute import base
from tempest.lib.common.utils import data_utils
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc


class FlavorsAdminTestJSON(base.BaseV2ComputeAdminTest):
    """Tests Flavors API Create and Delete that require admin privileges"""

    @classmethod
    def resource_setup(cls):
        super(FlavorsAdminTestJSON, cls).resource_setup()

        cls.flavor_name_prefix = 'test_flavor_'
        cls.ram = 512
        cls.vcpus = 1
        cls.disk = 10
        cls.ephemeral = 10
        cls.swap = 1024
        cls.rxtx = 2

    @decorators.idempotent_id('8b4330e1-12c4-4554-9390-e6639971f086')
    def test_create_flavor_with_int_id(self):
        """Test creating flavor with id of type integer"""
        flavor_id = data_utils.rand_int_id(start=1000)
        new_flavor_id = self.create_flavor(ram=self.ram,
                                           vcpus=self.vcpus,
                                           disk=self.disk,
                                           id=flavor_id)['id']
        self.assertEqual(new_flavor_id, str(flavor_id))

    @decorators.idempotent_id('94c9bb4e-2c2a-4f3c-bb1f-5f0daf918e6d')
    def test_create_flavor_with_uuid_id(self):
        """Test creating flavor with id of type uuid"""
        flavor_id = data_utils.rand_uuid()
        new_flavor_id = self.create_flavor(ram=self.ram,
                                           vcpus=self.vcpus,
                                           disk=self.disk,
                                           id=flavor_id)['id']
        self.assertEqual(new_flavor_id, flavor_id)

    @decorators.idempotent_id('f83fe669-6758-448a-a85e-32d351f36fe0')
    def test_create_flavor_with_none_id(self):
        """Test creating flavor without id specified

        If nova receives a request with None as flavor_id,
        nova generates flavor_id of uuid.
        """
        flavor_id = None
        new_flavor_id = self.create_flavor(ram=self.ram,
                                           vcpus=self.vcpus,
                                           disk=self.disk,
                                           id=flavor_id)['id']
        self.assertEqual(new_flavor_id, str(uuid.UUID(new_flavor_id)))

    @decorators.idempotent_id('8261d7b0-be58-43ec-a2e5-300573c3f6c5')
    def test_create_flavor_verify_entry_in_list_details(self):
        """Create a flavor and ensure its details are listed

        This operation requires the user to have 'admin' role
        """
        flavor_name = data_utils.rand_name(self.flavor_name_prefix)

        # Create the flavor
        self.create_flavor(name=flavor_name,
                           ram=self.ram, vcpus=self.vcpus,
                           disk=self.disk,
                           ephemeral=self.ephemeral,
                           swap=self.swap,
                           rxtx_factor=self.rxtx)

        # Check if flavor is present in list
        flavors_list = self.admin_flavors_client.list_flavors(
            detail=True)['flavors']
        self.assertIn(flavor_name, [f['name'] for f in flavors_list])

    @decorators.idempotent_id('63dc64e6-2e79-4fdf-868f-85500d308d66')
    def test_create_list_flavor_without_extra_data(self):
        """Create a flavor and ensure it is listed

        This operation requires the user to have 'admin' role
        """
        def verify_flavor_response_extension(flavor):
            # check some extensions for the flavor create/show/detail response
            if self.is_requested_microversion_compatible('2.74'):
                self.assertEqual(flavor['swap'], '')
            else:
                self.assertEqual(flavor['swap'], 0)
            self.assertEqual(int(flavor['rxtx_factor']), 1)
            self.assertEqual(flavor['OS-FLV-EXT-DATA:ephemeral'], 0)
            self.assertEqual(flavor['os-flavor-access:is_public'], True)

        flavor_name = data_utils.rand_name(self.flavor_name_prefix)
        new_flavor_id = data_utils.rand_int_id(start=1000)

        # Create the flavor
        flavor = self.create_flavor(name=flavor_name,
                                    ram=self.ram, vcpus=self.vcpus,
                                    disk=self.disk,
                                    id=new_flavor_id)
        self.assertEqual(flavor['name'], flavor_name)
        self.assertEqual(flavor['ram'], self.ram)
        self.assertEqual(flavor['vcpus'], self.vcpus)
        self.assertEqual(flavor['disk'], self.disk)
        self.assertEqual(int(flavor['id']), new_flavor_id)
        verify_flavor_response_extension(flavor)

        # Verify flavor is retrieved
        flavor = self.admin_flavors_client.show_flavor(new_flavor_id)['flavor']
        self.assertEqual(flavor['name'], flavor_name)
        verify_flavor_response_extension(flavor)

        # Check if flavor is present in list
        flavors_list = [
            f for f in self.flavors_client.list_flavors(detail=True)['flavors']
            if f['name'] == flavor_name
        ]
        self.assertNotEmpty(flavors_list)
        verify_flavor_response_extension(flavors_list[0])

    @decorators.idempotent_id('be6cc18c-7c5d-48c0-ac16-17eaf03c54eb')
    def test_list_non_public_flavor(self):
        """Create a flavor with os-flavor-access:is_public false.

        The flavor should not be present in list_details as the
        tenant is not automatically added access list.
        This operation requires the user to have 'admin' role
        """
        flavor_name = data_utils.rand_name(self.flavor_name_prefix)

        # Create the flavor
        self.create_flavor(name=flavor_name,
                           ram=self.ram, vcpus=self.vcpus,
                           disk=self.disk,
                           is_public="False")
        # Verify flavor is not retrieved
        flavors_list = self.admin_flavors_client.list_flavors(
            detail=True)['flavors']
        self.assertNotIn(flavor_name, [f['name'] for f in flavors_list])

        # Verify flavor is not retrieved with other user
        flavors_list = self.flavors_client.list_flavors(detail=True)['flavors']
        self.assertNotIn(flavor_name, [f['name'] for f in flavors_list])

    @decorators.idempotent_id('bcc418ef-799b-47cc-baa1-ce01368b8987')
    def test_create_server_with_non_public_flavor(self):
        """Create a flavor with os-flavor-access:is_public false"""
        flavor = self.create_flavor(ram=self.ram, vcpus=self.vcpus,
                                    disk=self.disk,
                                    is_public="False")

        # Verify flavor is not used by other user
        self.assertRaises(lib_exc.BadRequest,
                          self.os_primary.servers_client.create_server,
                          name='test', imageRef=self.image_ref,
                          flavorRef=flavor['id'])

    @decorators.idempotent_id('b345b196-bfbd-4231-8ac1-6d7fe15ff3a3')
    def test_list_public_flavor_with_other_user(self):
        """Create a Flavor with public access.

        Try to List/Get flavor with another user
        """
        flavor_name = data_utils.rand_name(self.flavor_name_prefix)

        # Create the flavor
        self.create_flavor(name=flavor_name,
                           ram=self.ram, vcpus=self.vcpus,
                           disk=self.disk,
                           is_public="True")
        # Verify flavor is retrieved with new user
        flavors_list = self.flavors_client.list_flavors(detail=True)['flavors']
        self.assertIn(flavor_name, [f['name'] for f in flavors_list])

    @decorators.idempotent_id('fb9cbde6-3a0e-41f2-a983-bdb0a823c44e')
    def test_is_public_string_variations(self):
        """Test creating public and non public flavors"""
        flavor_name_not_public = data_utils.rand_name(self.flavor_name_prefix)
        flavor_name_public = data_utils.rand_name(self.flavor_name_prefix)

        # Create a non public flavor
        self.create_flavor(name=flavor_name_not_public,
                           ram=self.ram, vcpus=self.vcpus,
                           disk=self.disk,
                           is_public="False")

        # Create a public flavor
        self.create_flavor(name=flavor_name_public,
                           ram=self.ram, vcpus=self.vcpus,
                           disk=self.disk,
                           is_public="True")

        def _test_string_variations(variations, flavor_name):
            for string in variations:
                params = {'is_public': string}
                flavors = (self.admin_flavors_client.list_flavors(detail=True,
                                                                  **params)
                           ['flavors'])
                self.assertIn(flavor_name, [f['name'] for f in flavors])

        _test_string_variations(['f', 'false', 'no', '0'],
                                flavor_name_not_public)

        _test_string_variations(['t', 'true', 'yes', '1'],
                                flavor_name_public)

    @decorators.idempotent_id('3b541a2e-2ac2-4b42-8b8d-ba6e22fcd4da')
    def test_create_flavor_using_string_ram(self):
        """Test creating flavor with ram of type string"""
        new_flavor_id = data_utils.rand_int_id(start=1000)

        ram = "1024"
        flavor = self.create_flavor(ram=ram, vcpus=self.vcpus,
                                    disk=self.disk,
                                    id=new_flavor_id)
        self.assertEqual(flavor['ram'], int(ram))
        self.assertEqual(int(flavor['id']), new_flavor_id)


class FlavorPermissionsAdminTestJSON(base.BaseV2ComputeAdminTest):

    min_microversion = '2.100'

    def setUp(self):
        super().setUp()
        self.flavor = self.create_flavor(
            ram=512, vcpus=1, disk=10, is_public='True')

    @decorators.idempotent_id('56ca1d2d-c430-4431-a046-09368029a648')
    def test_list_flavor_permission_filter(self):
        """Test filtering flavor list by permissions"""
        domain_id = self.os_admin.credentials.project_domain_id
        project_id = self.os_admin.credentials.project_id
        # Deny flavor at project scope
        self.create_flavor_permission_rule(
            domain_id=domain_id, project_id=project_id,
            effect='deny', flavor_id=self.flavor['id'])
        # Flavor appears in the list of denied flavors
        denied = self.admin_flavors_client.list_flavors(
            detail=True, project_permission='deny')['flavors']
        self.assertIn(self.flavor['id'], {f['id'] for f in denied})
        # Flavor is not in the list of allowed flavors
        allowed = self.admin_flavors_client.list_flavors(
            detail=True, project_permission='allow')['flavors']
        self.assertNotIn(self.flavor['id'], {f['id'] for f in allowed})

    @decorators.idempotent_id('a90933ae-cfb3-4d7a-a3cc-59b89cf0f605')
    def test_show_list_flavor_permissions_annotation(self):
        """Test showing and listing permissions annotation"""
        domain_id = self.os_admin.credentials.project_domain_id
        project_id = self.os_admin.credentials.project_id
        # Show reflects default 'allow' permissions
        shown = self.admin_flavors_client.show_flavor(
            self.flavor['id'])['flavor']
        self.assertIn('permissions', shown)
        self.assertEqual('allow', shown['permissions']['project'])
        self.assertEqual('allow', shown['permissions']['domain'])
        # Show reflects project 'deny' rule
        self.create_flavor_permission_rule(
            domain_id=domain_id, project_id=project_id,
            effect='deny', flavor_id=self.flavor['id'])
        shown = self.admin_flavors_client.show_flavor(
            self.flavor['id'])['flavor']
        self.assertEqual('deny', shown['permissions']['project'])
        self.assertEqual('allow', shown['permissions']['domain'])
        # Details reflect project 'deny' rule
        detailed = self.admin_flavors_client.list_flavors(
            detail=True)['flavors']
        detailed = [f for f in detailed if f['id'] == self.flavor['id']]
        self.assertEqual(1, len(detailed))
        self.assertEqual('deny', detailed[0]['permissions']['project'])

    @decorators.idempotent_id('d4e5fa02-004e-4b3e-8705-22b65e460ab9')
    def test_show_list_denied_flavor_non_admin(self):
        """Deny rules hide flavors from list and show for regular users"""
        self.create_flavor_permission_rule(
            domain_id=self.os_primary.credentials.project_domain_id,
            project_id=self.os_primary.credentials.project_id,
            effect='deny', flavor_id=self.flavor['id'])
        flavor_ids = {f['id'] for f in self.flavors_client.list_flavors(
            detail=True)['flavors']}
        self.assertNotIn(self.flavor['id'], flavor_ids)
        self.assertRaises(lib_exc.NotFound,
                          self.flavors_client.show_flavor, self.flavor['id'])
