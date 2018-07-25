{
    'name': 'Project Junior Manager role',
    'description': """
This module add role Junior manager and access restrictions.
    """,
    'category': 'Project',
    'depends': ['project', 'project_team'],
    'data': [
        'security/project_security.xml',
    ],
    'installable': True,
}
