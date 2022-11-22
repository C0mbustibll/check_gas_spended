VIEW =0  # Если стоит 1 то вы увидите потраченный газ на каждом аккаунту
streams = 5 # Количество потоков не больше 5

ETH_API = 'NR49D3QEI7R6NH7MVVPM1XW8H71ISU1IHY'  # https://etherscan.io/myapikey
OPT_API = 'G9N5C76KBYUEBGEBFJ69FUEKHQTKNIUW6W'  # https://optimistic.etherscan.io/myapikey
ARB_API = 'C1XUXCBS7VJ4X2QF8VGTU6VV2CYPYJK852'  # https://arbiscan.io/myapikey
POLYGON_API = 'VG5YT2UFT4YAIJ8W66MRDHPTSVUKQQ9W6F' # https://polygonscan.com/myapikey








scan_url = [
    'https://api.etherscan.io/',
    'https://api-optimistic.etherscan.io/',
    'https://api.arbiscan.io/',
    'https://api.polygonscan.com/'
]

key_dict = {
    'https://api.etherscan.io/': ETH_API,
    'https://api-optimistic.etherscan.io/': OPT_API,
    'https://api.arbiscan.io/': ARB_API,
    'https://api.polygonscan.com/': POLYGON_API
}

coin_dict = {
    'https://api.etherscan.io/': 'ETH',
    'https://api-optimistic.etherscan.io/': 'ETH',
    'https://api.arbiscan.io/': 'ETH',
    'https://api.polygonscan.com/': 'MATIC'
}

chain_dict = {
    'https://api.etherscan.io/': 'ETH',
    'https://api-optimistic.etherscan.io/': 'OPTIMISM',
    'https://api.arbiscan.io/': 'ARBITRUM',
    'https://api.polygonscan.com/': 'POLYGON'
}
