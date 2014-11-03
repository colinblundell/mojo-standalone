# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'mojom_base_output_dir':
      '<!(python <(DEPTH)/build/inverse_depth.py <(DEPTH))',
    'mojom_generated_outputs': [
      '<!@(python <(DEPTH)/mojo/public/tools/bindings/mojom_list_outputs.py --basedir <(mojom_base_output_dir) <@(mojom_files))',
    ],
  },
  'actions': [
    {
      'action_name': '<(_target_name)_mojom_bindings_generator',
      'variables': {
        'mojom_bindings_generator':
            '<(DEPTH)/mojo/public/tools/bindings/mojom_bindings_generator.py',
        'java_out_dir': '<(PRODUCT_DIR)/java_mojo/<(_target_name)/src',
        'mojom_import_args%': [
         '-I<(DEPTH)'
        ],
      },
      'inputs': [
        '<(mojom_bindings_generator)',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/enum_declaration.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/interface_declaration.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/interface_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/interface_macros.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/interface_proxy_declaration.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/interface_request_validator_declaration.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/interface_response_validator_declaration.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/interface_stub_declaration.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/module.cc.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/module.h.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/module-internal.h.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/params_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/struct_declaration.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/struct_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/struct_macros.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/struct_serialization_declaration.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/struct_serialization_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/wrapper_class_declaration.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/cpp_templates/wrapper_class_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/constant_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/constants.java.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/enum_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/enum.java.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/header.java.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/interface_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/interface.java.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/interface_internal.java.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/struct_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/java_templates/struct.java.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/js_templates/enum_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/js_templates/interface_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/js_templates/module_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/js_templates/module.amd.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/js_templates/module.html.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/js_templates/struct_definition.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/python_templates/module_macros.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/python_templates/module.py.tmpl',
        '<(DEPTH)/mojo/public/tools/bindings/generators/mojom_cpp_generator.py',
        '<(DEPTH)/mojo/public/tools/bindings/generators/mojom_java_generator.py',
        '<(DEPTH)/mojo/public/tools/bindings/generators/mojom_js_generator.py',
        '<(DEPTH)/mojo/public/tools/bindings/generators/mojom_python_generator.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/__init__.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/error.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/generate/__init__.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/generate/data.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/generate/generator.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/generate/module.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/generate/pack.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/generate/template_expander.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/parse/__init__.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/parse/ast.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/parse/lexer.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/parse/parser.py',
        '<(DEPTH)/mojo/public/tools/bindings/pylib/mojom/parse/translate.py',
      ],
      'outputs': [
        '<@(mojom_generated_outputs)',
      ],
      'action': [
        'python', '<@(mojom_bindings_generator)',
        '<@(mojom_files)',
        '--use_chromium_bundled_pylibs',
        '-d', '<(DEPTH)',
        '<@(mojom_import_args)',
        '-o', '<(SHARED_INTERMEDIATE_DIR)',
        '--java_output_directory=<(java_out_dir)',
      ],
      'message': 'Generating Mojo bindings from <@(mojom_files)',
    }
  ],
  'direct_dependent_settings': {
    'variables': {
      'generated_src_dirs': [
        '<(PRODUCT_DIR)/java_mojo/<(_target_name)/src',
      ],
    },
    'sources': [
      '<@(mojom_generated_outputs)',
    ],
    # Include paths needed to compile the generated sources into a library.
    'include_dirs': [
      '<(DEPTH)',
      '<(SHARED_INTERMEDIATE_DIR)',
    ],
    'direct_dependent_settings': {
      # Include paths needed to find the generated header files and their transitive
      # dependancies when using the library.
      'include_dirs': [
        '<(DEPTH)',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
    }
  },
  'hard_dependency': 1,
}
