# Environment variables
NUMERICAL_FEATURES = ['account length', 'number vmail messages', 'total day minutes', 'total day calls',
                      'total day charge', 'total eve minutes', 'total eve calls', 'total eve charge',
                      'total night minutes', 'total night calls', 'total night charge',
                      'total intl minutes',
                      'total intl calls', 'total intl charge', 'number customer service calls']
CATEGORICAL_FEATURES = ['state', 'area code', 'international plan', 'voice mail plan']
FEATURES = ['account length', 'number vmail messages', 'total day minutes', 'total day calls',
            'total day charge', 'total eve minutes', 'total eve calls', 'total eve charge',
            'total night minutes', 'total night calls', 'total night charge', 'total intl minutes',
            'total intl calls', 'total intl charge', 'number customer service calls', 'state_1',
            'state_2', 'state_3', 'state_4', 'state_5', 'state_6', 'state_7', 'state_8', 'state_9',
            'state_10', 'state_11', 'state_12', 'state_13', 'state_14', 'state_15', 'state_16', 'state_17',
            'state_18', 'state_19', 'state_20', 'state_21', 'state_22', 'state_23', 'state_24', 'state_25',
            'state_26', 'state_27', 'state_28', 'state_29', 'state_30', 'state_31', 'state_32', 'state_33',
            'state_34', 'state_35', 'state_36', 'state_37', 'state_38', 'state_39', 'state_40', 'state_41',
            'state_42', 'state_43', 'state_44', 'state_45', 'state_46', 'state_47', 'state_48', 'state_49',
            'state_50', 'area code_415', 'area code_510', 'international plan_No', 'voice mail plan_No']

STATE_CATEGORIES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                    24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                    45, 46, 47, 48, 49, 50]
AREA_CATEGORIES = [408, 415, 510]
INTERNATIONAL_PLAN_CATEGORIES = ['Si', 'No']
VOICE_MAIL_CATEGORIES = ['Si', 'No']
TARGET = 'target'
MAP = {1: 'Si', 0: 'No'}