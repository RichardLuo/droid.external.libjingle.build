# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This file is meant to be included into a target to handle shim headers
# in a consistent manner. To use this the following variables need to be
# defined:
#   headers_root_path: string: path to directory containing headers
#   header_filenames: list: list of header file names

{
  'variables': {
    'shim_headers_path': '<(SHARED_INTERMEDIATE_DIR)/shim_headers/<(_target_name)/<(_toolset)',
  },
  'include_dirs+++': [
    '<(shim_headers_path)',
  ],
  'direct_dependent_settings': {
    'include_dirs++++': [
      '<(shim_headers_path)',
    ],
  },
  'actions': [
    {
      'variables': {
        'generator_path': '<(DEPTH)/tools/generate_shim_headers/generate_shim_headers.py',
        'generator_args': [
          '--headers-root', '<(headers_root_path)',
          '--output-directory', '<(shim_headers_path)',
          '<@(header_filenames)',
        ],
      },
      'action_name': 'generate_<(_target_name)_shim_headers',
      'inputs': [
        '<(generator_path)',
      ],
      'outputs': [
        '<!@pymod_do_main(generate_shim_headers <@(generator_args) --outputs)',
      ],
      'action': ['python',
                 '<(generator_path)',
                 '<@(generator_args)',
                 '--generate',
      ],
      'message': 'Generating <(_target_name) shim headers.',
    },
  ],
}
