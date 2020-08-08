

ADMIN_ROLES = ['fifi']
MOD_ROLES = [*ADMIN_ROLES, 'fifi']

# 0xRRGGBB aka HEX
MAIN_COLOR = 0x091A4C
ERROR_COLOR = 0xD86156
OFF_COLOR_1 = 0xF2B53C
OFF_COLOR_2 = 0x5F6662
INFO_COLOR = 0x3BCCB3

NATIVE_COLOR = 0x0070BB
FLUENT_COLOR = 0x765A9F
LEARNING_COLOR = 0xC54b8C
YELLOW_ROLE_COLOR = 0xFFC40C
ORANGE_ROLE_COLOR = 0xFF7518
BLACK_ROLE_COLOR = 0x000001

LANGUAGE_ROLES = [NATIVE_COLOR, FLUENT_COLOR, LEARNING_COLOR]
ASSIGNABLE_ROLE_COLORS = [*LANGUAGE_ROLES, YELLOW_ROLE_COLOR, ORANGE_ROLE_COLOR, BLACK_ROLE_COLOR]

YES_EMOJI = '✅'
NO_EMOJI = '❌'

text_lines = {
    ##############  IMPORTANT  ###############
    # Hierarchy: Cog (Class) -> Method -> Line
   

    'server_info': {
        'titles': {
            'id': 'Id',
            'owner': 'Owner',
            'region': 'Region',
            'roles': 'Roles: {}',  # Amount of roles
            'features': 'Features',
            'default_channel': 'Default channel',
            'channels': 'Channels: {}',  # Amount of channels
            'created_at': 'Created at',
            'members': 'Members: {}',  # Amount of members
            'emojis': 'Emojis: {}'  # Amount of emojis
        },
        'members_line': '{} tagged, {} normies',  # In total, Without roles
        'roles': '{} language, {} other',  # Amount of language roles, Amount of other roles
        'channel_line': '{} text, {} voice'  # Text channels, Voice channels
    },

  

   
}