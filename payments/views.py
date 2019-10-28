from django.shortcuts import render, redirect
import requests
from decouple import config


KEY = config('KAKAO_API_KEY')
API_HOST = 'https://kapi.kakao.com'
headers = {'Authorization': f'KakaoAK {KEY}'}


def req(path, query, data={}):
    url = API_HOST + path

    print('Request URL: %s' % url)
    print('Headers: %s' % headers)
    print('QueryString: %s' % query)

    return requests.post(url, headers=headers, data=data).json()


# Create your views here.
# 주문 정보 확인
def index(request):
    return render(request, 'payments/index.html')


# 결제 로직
def pay(request):
    # order example
    params = {
        'cid': 'TC0ONETIME',
        'partner_order_id': '1111',
        'partner_user_id': '2222',
        'item_name': '초코파이',
        'quantity': 1,
        'total_amount': 2200,
        'vat_amount': 200,
        'tax_free_amount': 0,
        'approval_url': 'https://developers.kakao.com/success',
        'fail_url': 'https://developers.kakao.com/fail',
        'cancel_url': 'https://developers.kakao.com/cancel',
    }
    data = req('/v1/payment/ready', '', params)

    return redirect(data['next_redirect_pc_url'])


# 환불 로직
def refund(request):
    pass