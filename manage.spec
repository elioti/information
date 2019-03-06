# -*- mode: python -*-

block_cipher = None


a = Analysis(['manage.py'],
             pathex=['C:\\Users\\aha_l\\PycharmProjects\\information'],
             binaries=[],
             datas=[
             ('C:\\Users\\Owner\\PycharmProjects\\information\\dists', '.\\dists'),
             ],
             hiddenimports=[
             'info.apps',
             'rest_framework.apps',
             'utils.jwt',
             'rest_framework_jwt.utils',
             'rest_framework.parsers',
             'rest_framework.negotiation',
             'rest_framework.metadata',
            'django_filters.rest_framework',
            'info.pagination',
            'rest_framework_jwt.utils',
            'rest_framework_jwt.utils',
            'utils.jwt',
            'rest_framework.schemas',
            'django.contrib.auth.migrations',
            'django.contrib.auth.migrations.0003_alter_user_email_max_length',
            'django.contrib.auth.migrations.0007_alter_validators_add_error_messages',
            'django.contrib.auth.migrations.0002_alter_permission_name_max_length',
            'django.contrib.auth.migrations.0006_require_contenttypes_0002',
            'django.contrib.auth.migrations.0008_alter_user_username_max_length',
            'django.contrib.auth.migrations.0001_initial',
            'django.contrib.auth.migrations.0005_alter_user_last_login_null',
            'django.contrib.auth.migrations.0004_alter_user_username_opts',
            'django.contrib.contenttypes.migrations',
            'django.contrib.contenttypes.migrations.0002_remove_content_type_name',
            'django.contrib.contenttypes.migrations.0001_initial',
            'django.contrib.sessions.migrations',
            'django.contrib.sessions.migrations.0001_initial',
            'django.contrib.messages.migrations',
            'django.contrib.staticfiles.migrations',
            'rest_framework.migrations',
            'django_filters.migrations',
            'django.db.models.sql.compiler',
            'information.wsgi',
            'logging.config',
            'django.middleware.clickjacking',
            'django.contrib.messages.middleware',
            'django.contrib.auth.middleware',
            'django.middleware.csrf',
            'django.middleware.common',
            'django.contrib.sessions.middleware',
            'django.contrib.sessions.backends.db',
            'django.middleware.security',
            'django.middleware.clickjacking',
            'django.contrib.messages.middleware',
            'django.contrib.auth.middleware',
            'django.middleware.csrf',
            'django.middleware.common',
            'django.contrib.sessions.middleware',
            'django.contrib.sessions.backends.db',
            'django.middleware.security',
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='manage',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='manage')
