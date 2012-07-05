# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack, LLC
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

from nose.plugins.attrib import attr

from tempest import exceptions
from tempest.common.utils.data_utils import rand_name, parse_image_id
from tempest.tests.compute.base import BaseComputeTest


class ListImagesTest(BaseComputeTest):

    @classmethod
    def setUpClass(cls):
        super(ListImagesTest, cls).setUpClass()
        cls.client = cls.images_client

    @classmethod
    def tearDownClass(cls):
        super(ListImagesTest, cls).tearDownClass()

    @attr(type='smoke')
    def test_get_image(self):
        """Returns the correct details for a single image"""
        resp, image = self.client.get_image(self.image_ref)
        self.assertEqual(self.image_ref, image['id'])

    @attr(type='smoke')
    def test_list_images(self):
        """The list of all images should contain the image"""
        resp, images = self.client.list_images()
        found = any([i for i in images if i['id'] == self.image_ref])
        self.assertTrue(found)

    @attr(type='smoke')
    def test_list_images_with_detail(self):
        """Detailed list of all images should contain the expected images"""
        resp, images = self.client.list_images_with_detail()
        found = any([i for i in images if i['id'] == self.image_ref])
        self.assertTrue(found)
