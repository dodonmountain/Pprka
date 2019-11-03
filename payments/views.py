from django.shortcuts import render, redirect
import requests
from decouple import config
from .models import Payment


KEY = config('KAKAO_API_KEY')
API_HOST = 'https://kapi.kakao.com'
headers = {'Authorization': f'KakaoAK {KEY}'}
tid = 0

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


# 결제 요청
def pay(request):
    # order example
    global tid

    params = {
        'cid': 'TC0ONETIME',
        'partner_order_id': '19283432',
        'partner_user_id': '4211',
        'item_name': 'Paprika Hotel Single Room',
        'item_code': 'a123',
        'quantity': 1,
        'total_amount': 323900,
        'vat_amount': 32390,
        'tax_free_amount': 0,
        'approval_url': 'http://127.0.0.1:8000/payments/success/',
        'fail_url': 'http://127.0.0.1:8000/payments/fail/',
        'cancel_url': 'http://127.0.0.1:8000/payments/cancel/',
    }
    data = req('/v1/payment/ready', '', params)
    print(data)
    tid = data['tid']

    return redirect(data['next_redirect_pc_url'])


# 결제 성공(승인)
def success(request):
    global tid

    params = {
        'cid': 'TC0ONETIME',
        'tid': tid,
        'partner_order_id': '19283432',
        'partner_user_id': '4211',
        'pg_token': request.GET.get('pg_token'),
    }
    print(params)
    data = req('/v1/payment/approve', '', params)

    payment = Payment(aid=data['aid'], tid=data['tid'], payment_method_type=data['payment_method_type'],
                item_name=data['item_name'], item_code=['item_code'], amount=data['amount']['total'],
                created_at=data['created_at'], approved_at=data['approved_at'])
    payment.save()

    context = {
        'item_name': payment.item_name,
        'amount': payment.amount,
    }

    return render(request, 'payments/success.html', context)


# 결제 취소 : 사용자가 결제 도중 취소하는 경우
def cancel(request):
    return render(request, 'payments/cancel.html')


# 결제 실패 : 결제 요청이 받아들여지지 않음
def fail(request):
    return render(request, 'payments/fail.html')


# 환불 로직
def refund(request):
    pass