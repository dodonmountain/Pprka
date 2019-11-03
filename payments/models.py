from django.db import models

# Create your models here.
class Payment(models.Model):
    aid = models.CharField(max_length=100)
    tid = models.CharField(max_length=100)
    payment_method_type = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    amount = models.IntegerField()
    created_at = models.DateTimeField()
    approved_at = models.DateTimeField()


# aid	Request 고유 번호	String
# tid	결제 고유 번호	String
# cid	가맹점 코드	String
# sid	subscription id. 정기(배치)결제 CID로 결제요청한 경우 발급	String
# partner_order_id	가맹점 주문번호	String
# partner_user_id	가맹점 회원 id	String
# payment_method_type	결제 수단. CARD, MONEY 중 하나	String
# amount	결제 금액 정보	JSON Object
# card_info	결제 상세 정보(결제수단이 카드일 경우만 포함)	JSON Object
# item_name	상품 이름. 최대 100자	String
# item_code	상품 코드. 최대 100자	String
# quantity	상품 수량	Integer
# created_at	결제 준비 요청 시각	Datetime
# approved_at	결제 승인 시각	Datetime    