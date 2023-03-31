from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server
import pandas as pd

field_list = ['货码', '颜色', '种水', '价格']
index_col = field_list[0]

df = pd.DataFrame(columns=field_list)

def get_price(color, zhong):
    return color * 100 +  zhong * 200


with use_scope('result', clear=True):
    put_html(df.to_html(border=0))

while True:

    data = input_group("Basic info",[
      input('货码', name='index'),
      input('色打分', name='color', type=NUMBER),
      input('种水打分', name='zhong', type=NUMBER)
    ])

    data_list = [
        data['index'],
        data['color'],
        data['zhong'],
        get_price(data['color'], data['zhong'])
    ]

    try:
        index = df.index[df[index_col] == data['index']][0]
        df.loc[index] = data_list
    except Exception as e:
        df = pd.concat([df, pd.DataFrame([data_list], columns=field_list)], ignore_index=True)


    with use_scope('result', clear=True):
        put_html(df.to_html(border=0))
