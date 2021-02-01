# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 17:02
# @Author  : play4fun
# @File    : 导购-链接转换1.py
# @Software: PyCharm

"""
没有权限
导购-链接转换1.py:

领券网址!!

优惠券
http://item.taobao.com/item.htm?id=561743770998

这个很重要
"""

from top.api import TbkCouponConvertRequest
from top import appinfo

from testCase.config import appkey, secret,pid

req = TbkCouponConvertRequest()
req.set_app_info(appinfo(appkey, secret))

req.item_id = 566569778934#526231351170
req.adzone_id = pid
req.platform = 2  # 链接形式：1：PC，2：无线，默认：１
# req.me = "dsdfsdadgsa" #me参数不合法

try:
    resp = req.getResponse()
    print(resp)

    it = resp['tbk_coupon_convert_response']['result']['results']
    print(it)
    coupon_remain_count=it['coupon_remain_count']
    print('优惠券剩余数:',coupon_remain_count)

    # import json
    # ds = json.dumps(resp)
    # print(ds)
except Exception as e:
    print(e)
    '''
{
    "result": {
        "results": {
            "campaign_type": 0,
            "category_id": 16,
            "coupon_click_url": "https://uland.taobao.com/coupon/edetail?e=JBuZPm5JWqEGQASttHIRqZL3pImL%2FJh1HZ6yD2Py5i%2Fg4lUqifPvH9x2%2FlD7wOdrVxl2CHuUpj1uWNE2q%2FyjycWKxy1EFPIVsSKwS%2F%2FvFcFma4VUO7VGBlZrtTOLgXkcjDppvlX%2Bob%2BBtHA6T8TZnVBPfopb7LXvu8n6e%2B0RLoCEsG9BMdsVqA%3D%3D&traceId=0bb6999515405448411741149e&union_lens=lensId:0b0ad4b4_0bf5_166afa0c5f0_c4b9",
            "coupon_end_time": "2018-10-31",
            "coupon_info": "满20元减3元",
            "coupon_remain_count": 97713,
            "coupon_start_time": "2018-10-11",
            "coupon_total_count": 100000,
            "item_id": 577221455881,
            "item_url": "https://s.click.taobao.com/t?e=m%3D2%26s%3Dgy4sKsJMmeJw4vFB6t2Z2ueEDrYVVa64LKpWJ%2Bin0XLLWlSKdGSYDiqSD1piiUwDRitN3%2FurF3yUZR70%2BlK9qVurOGJDe30Mi4iGkEp3vhY1bHXFwOOwIjqdUmXHECnnQlDOBn9aemSpQ9xdsBJHs%2F1SarTXhIOTjr5I55N9ec%2BxG0GudCypDaAFWUUKjwsKxg5p7bh%2BFbQ%3D&union_lens=lensId:0b0ad4b4_0bf5_166afa0c5f0_c4b9",
            "max_commission_rate": "10.00"
        }
    },
    "request_id": "bdxe9dpr4mq4"
}    



{'tbk_coupon_convert_response': 
{'request_id': '160qpdxniso3o',
  'result': {
  'results': {
  'campaign_type': 4,
    'category_id': 16,
    'coupon_click_url': 'https://uland.taobao.com/coupon/edetail?e=tpxBWdYyN7UGQASttHIRqe7Q9lqRIc6yStCkgxbJMujg4lUqifPvH9x2%2FlD7wOdrVxl2CHuUpj1uWNE2q%2FyjycWKxy1EFPIVsSKwS%2F%2FvFcFma4VUO7VGBlZrtTOLgXkcjDppvlX%2Bob%2F%2BTosbFmliBzQxd0%2F7s8Sy8%2B1UQ0U%2BCWuQzbQRBC%2Bhrg5I0cA7%2BNubPXF9dzoYDyA%3D&traceId=0bb3982d15535841148015810e&union_lens=lensId:0b0f79e2_0b63_169b8d44c8a_d0c3&xId=mJlE7rOlBXtwb8FDPDlVczPJLuG5NUZecwUiTcFsqdTYNmFsZ5e0IjNGs9OWuuXWfKSGBg0vDGdI22JW9HAHgc',
    'item_id': 526231351170,
    'item_url': 'https://s.click.taobao.com/t?e=m%3D2%26s%3D1OsBhN3TNUZw4vFB6t2Z2ueEDrYVVa64K7Vc7tFgwiHLWlSKdGSYDgcFMCLIwgbNxq3IhSJN6GSUZR70%2BlK9qVurOGJDe30Mi4iGkEp3vhY1bHXFwOOwIjqdUmXHECnnELxOuEw6aQXUTBxNyFgQ2uVMGbqY6G9PL95d7k%2B037XXtfkmARvbGIWLhXkoGmYybYZdV5DRMGazXVKh7aYSJMYOae24fhW0&union_lens=lensId:0b0f79e2_0b63_169b8d44c8a_d0c3&xId=mJlE7rOlBXtwb8FDPDlVczPJLuG5NUZecwUiTcFsqdTYNmFsZ5e0IjNGs9OWuuXWfKSGBg0vDGdI22JW9HAHgc',
    'max_commission_rate': '30.00'}}}}
    '''
