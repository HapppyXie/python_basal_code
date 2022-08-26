# Athour:Mr Xie
# 开发时间:2022/3/8 21:46
cookies = [{'domain': '.jd.com', 'expiry': 1673082263, 'httpOnly': False, 'name': '3AB9D23F7A4B3C9B', 'path': '/',
            'secure': False,
            'value': 'L53IM7MTMLHI5EFJ4YHAC3UBMMFONMAI2Z7NIDEHLCNWINO4ECFYK5J6DIK2LPMODRCVQREWHN4HGXCJNFWFYFVYR4'},
           {'domain': '.jd.com', 'expiry': 1662714262, 'httpOnly': False, 'name': '__jda', 'path': '/', 'secure': False,
            'value': '122270672.16471622606431272528372.1647162261.1647162261.1647162261.1'},
           {'domain': '.jd.com', 'expiry': 1648026261, 'httpOnly': False, 'name': 'areaId', 'path': '/',
            'secure': False, 'value': '19'},
           {'domain': '.jd.com', 'expiry': 1647164062, 'httpOnly': False, 'name': 'shshshsID', 'path': '/',
            'secure': False, 'value': 'ea4dd705a2068ec03766463bd6886287_1_1647162262177'},
           {'domain': '.jd.com', 'expiry': 2511162262, 'httpOnly': False, 'name': 'shshshfpb', 'path': '/',
            'secure': False, 'value': 'jnl1YRkYh-A-yyKfg7oWGzw'},
           {'domain': '.jd.com', 'expiry': 2511162262, 'httpOnly': False, 'name': 'shshshfpa', 'path': '/',
            'secure': False, 'value': '830a68e2-106a-63d9-7a33-6e39051a6a0f-1647162262'},
           {'domain': '.jd.com', 'httpOnly': False, 'name': '__jdc', 'path': '/', 'secure': False,
            'value': '122270672'},
           {'domain': '.jd.com', 'expiry': 1647767061, 'httpOnly': False, 'name': 'PCSYCityID', 'path': '/',
            'secure': False, 'value': 'CN_440000_440100_0'},
           {'domain': '.jd.com', 'expiry': 1648026261, 'httpOnly': False, 'name': 'ipLoc-djd', 'path': '/',
            'secure': False, 'value': '19-1601-0-0'},
           {'domain': 'passport.jd.com', 'httpOnly': False, 'name': '_t', 'path': '/', 'sameSite': 'None',
            'secure': True, 'value': 'tXs4HAzNliW2BDgpgyrCaAG9kJ4rlNsa31iysjopoaw='},
           {'domain': '.jd.com', 'expiry': 2511162262, 'httpOnly': False, 'name': 'shshshfp', 'path': '/',
            'secure': False, 'value': 'b821c3f63261cf769679275970b3ed54'},
           {'domain': '.jd.com', 'httpOnly': False, 'name': 'wlfstk_smdl', 'path': '/', 'secure': False,
            'value': 'mg4gpe5c0lh4w0rj4ciezpfhqcb9phib'},
           {'domain': '.jd.com', 'expiry': 1647164062, 'httpOnly': False, 'name': '__jdb', 'path': '/', 'secure': False,
            'value': '122270672.3.16471622606431272528372|1.1647162261'},
           {'domain': '.jd.com', 'expiry': 1662714265, 'httpOnly': False, 'name': '__jdu', 'path': '/', 'secure': False,
            'value': '16471622606431272528372'},
           {'domain': 'passport.jd.com', 'httpOnly': True, 'name': 'alc', 'path': '/', 'sameSite': 'None',
            'secure': True, 'value': 'fAkRFbN3TLHA2+Z0tjSTCA=='},
           {'domain': '.jd.com', 'expiry': 1648458260, 'httpOnly': False, 'name': '__jdv', 'path': '/', 'secure': False,
            'value': '76161171|direct|-|none|-|1647162260644'}]
#
# result = []
# for cookie in cookies:
# # expiry有效期 - 时间戳  'expiry': 1673082263
#     temp={}
#     for key in cookie.keys():
#         if key == 'expiry':
#             pass
#         else:
#             temp[key] = cookie[key]
#     result.append(temp)
# print(result)
# import time
# now = int(time.time()+10000)
# print(now)



cookie = [{'domain': '.jd.com', 'expiry': 1673082263, 'httpOnly': False, 'name': '3AB9D23F7A4B3C9B', 'path': '/',
            'secure': False,
            'value': 'L53IM7MTMLHI5EFJ4YHAC3UBMMFONMAI2Z7NIDEHLCNWINO4ECFYK5J6DIK2LPMODRCVQREWHN4HGXCJNFWFYFVYR4'}]

result = []
for cookie in cookies:
    temp = {}
    for item in cookie.items():
        print(item)
        temp[item[0]]=str(item[0])+'='+str(item[1])
        result.append(temp)
print(result)
