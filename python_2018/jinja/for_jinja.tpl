{# コメント行 呼び出されたpythonのshopの値を反映 #}
ようこそ、{{ shop }}です。

{# コメント行  python側のfoodの値をforする #}
{% for food in foods %}
{# コメント行
loop.indexは整数を振っていく
food.nameはfoodリスト内のnameの値
food.priceはfoodリスト内のpriceの値 #}
{{ loop.index }}: {{ food.name }} － {{ food.price }}円
{% endfor %}
