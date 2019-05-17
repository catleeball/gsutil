# -*- coding: utf-8 -*-
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Additional help about types of credentials and authentication."""

from __future__ import absolute_import
from __future__ import unicode_literals

from gslib.help_provider import HelpProvider

_DETAILED_HELP_TEXT = 'detailed_help/security.md'

class CommandOptions(HelpProvider):
  """Additional help about security and privacy considerations using gsutil."""

  # Help specification. See help_provider.py for documentation.
  help_spec = HelpProvider.HelpSpec(
      help_name='security',
      help_name_aliases=[
        'hmac',
        'https',
        'oauth',
        'protection',
        'privacy',
        'proxies',
        'proxy,',
        'signing',
        'telemetry',
        'tls',
      ],
      help_type='additional_help',
      help_one_line_summary='Security and Privacy Considerations',
      help_text=_DETAILED_HELP_TEXT,
      subcommand_help_text={},
  )
