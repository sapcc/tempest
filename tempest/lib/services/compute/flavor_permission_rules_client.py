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

from urllib import parse as urllib

from oslo_serialization import jsonutils as json

from tempest.lib.api_schema.response.compute.v2_1 import \
    flavor_permission_rules as schema
from tempest.lib.common import rest_client
from tempest.lib import exceptions as lib_exc
from tempest.lib.services.compute import base_compute_client


class FlavorPermissionRulesClient(base_compute_client.BaseComputeClient):
    """Client for the flavor permission rules compute API extension."""

    def _get_url(self, rule_id=None, **params):
        url = 'flavor-permission-rules'
        if rule_id is not None:
            url += '/%s' % rule_id
        if params:
            url += '?%s' % urllib.urlencode(params)
        return url

    def _validated_body(self, response_schema, resp, body):
        # DELETE returns 204 with an empty body; only parse when present.
        if body:
            body = json.loads(body)
        self.validate_response(response_schema, resp, body)
        return rest_client.ResponseBody(resp, body)

    def list_flavor_permission_rules(self, **params):
        """List flavor permission rules."""
        resp, body = self.get(self._get_url(**params))
        return self._validated_body(
            schema.list_flavor_permission_rules, resp, body)

    def show_flavor_permission_rule(self, rule_id):
        """Show details for a flavor permission rule."""
        resp, body = self.get(self._get_url(rule_id))
        return self._validated_body(
            schema.show_update_flavor_permission_rule, resp, body)

    def create_flavor_permission_rule(self, **kwargs):
        """Create a flavor permission rule."""
        post_body = json.dumps({'flavor_permission_rule': kwargs})
        resp, body = self.post(self._get_url(), post_body)
        return self._validated_body(
            schema.create_flavor_permission_rule, resp, body)

    def update_flavor_permission_rule(self, rule_id, **kwargs):
        """Update a flavor permission rule (only `effect` is updatable)."""
        put_body = json.dumps({'flavor_permission_rule': kwargs})
        resp, body = self.put(self._get_url(rule_id), put_body)
        return self._validated_body(
            schema.show_update_flavor_permission_rule, resp, body)

    def delete_flavor_permission_rule(self, rule_id):
        """Delete the given flavor permission rule."""
        resp, body = self.delete(self._get_url(rule_id))
        return self._validated_body(
            schema.delete_flavor_permission_rule, resp, body)

    @property
    def resource_type(self):
        """Return the primary type of resource this client works with."""
        return 'flavor_permission_rule'

    def is_resource_deleted(self, id):
        try:
            self.show_flavor_permission_rule(id)
        except lib_exc.NotFound:
            return True
        return False
