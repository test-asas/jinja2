#�g�ݍ��܂ꂽ������p�^�[��
import jinja2

#test���镶����
test = '�����{{ test }}�ł�'

#template�Ƃ��Ĉ���
temp = jinja2.Template(test)
#template���̕ϐ��l�̒�`
data = {'test': 'pen'}

disp_text = temp.render(data)

print(disp_text)