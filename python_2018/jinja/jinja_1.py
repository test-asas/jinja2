#組み込まれた文字列パターン
import jinja2

#testする文字列
test = 'これは{{ test }}です'

#templateとして扱う
temp = jinja2.Template(test)
#template内の変数値の定義
data = {'test': 'pen'}

disp_text = temp.render(data)

print(disp_text)
