import pandas as pd
from pandas import DataFrame
import csv
import re
import string
from pyvi import ViTokenizer

#đọc dữ liệu từ csv
train_data = pd.read_csv('data_first100.csv',sep=',',keep_default_na=False)
# stopword = pd.read_csv('stop_word.csv',sep=',',keep_default_na=False)

# chuyển sang list để có thể thay đổi gía trị
comment_var = list(train_data.comment)
# stopword_var = list(stopword.title)

#loại bỏ các kí tự đặc biệt, dấu câu
#không cần remove khoảng trắng, vì khi dùng CountVectorizer, sklearn k tính khoảng trắng
def remove_symbol(text):
     remove_list =[
                    #remove các biểu tượng và kí tự xuống dòng
                    '👹', '👻', '💃','🤙', '👍','💄', '💎', '💩','😕', '😱',
                    '😸','😾', '🚫',  '🤬','🧚', '🧡','🐶','👎', '😣','✨', '❣','☀',
                    '♥', '🤩', '💌','🤣', '🖤', '🤤', ':(', '😢',
                    '❤', '😍', '😘', '😪', '😊','?', '😁', '💖', '😟', '😭',
                    '💯', '💗', '♡', '💜', '🤗','^^', '😨', '☺', '💋', '👌',
                    '😖', '😀', ':((', '😡', '😠','😒', '🙂', '😏', '😝', '😄',
                    '😙', '😤', '😎', '😆', '💚','✌', '💕', '😞', '😓', '️🆗️',
                    '😉', '😂', ':v', '=))', '😋','💓', '😐', ':3', '😫', '😥',
                    '😃', '😬' ,' 😬 ', '😌', ' 😌 ', '💛', '🤝', '🎈',
                    '😗', '🤔', '😑', '🔥', '🙏','🆗', '😻', '💙', '💟',
                    '😚', '❌', '👏', ';)', '<3','🌝',  '🌷', '🌸', '🌺',
                    '🌼', '🍓', '🐅', '🐾', '👉','💐', '💞', '💥', '💪',
                    '💰',  '😇', '😛', '😜','🙃', '🤑', '🤪','☹',  '💀',
                    '😔', '😧', '😩', '😰', '😳','😵', '😶', '🙁','🍰','🍹','🏨','🎪','☕',
                    '🌲','⛅','🌞','🍑','🍐','🌻','😅', '🏻','🎉️','\n']
     for k in remove_list:
          text = text.replace(k,' ')
     return text

#thay thế các từ viết tắt, viết sai, tiếng anh
def replace_word(text):
     replace_list = {
                    #các vần viết sai chính tả, các dấu câu viết bằng kí hiệu
                    'òa': 'oà', 'óa': 'oá', 'ỏa': 'oả', 'õa': 'oã', 'ọa': 'oạ', 'òe': 'oè',
                     'óe': 'oé','ỏe': 'oẻ', 'õe': 'oẽ', 'ọe': 'oẹ', 'ùy': 'uỳ', 'úy': 'uý',
                     'ủy': 'uỷ', 'ũy': 'uỹ','ụy': 'uỵ', 'uả': 'ủa', 'ả': 'ả', 'ố': 'ố',
                     'u´': 'ú','ỗ': 'ỗ', 'ồ': 'ồ', 'ổ': 'ổ', 'ấ': 'ấ', 'ẫ': 'ẫ',
                     'ẩ': 'ẩ', 'ầ': 'ầ', 'ỏ': 'ỏ', 'ê`': 'ề','ễ': 'ễ', 'ắ': 'ắ', 
                     'ủ': 'ủ', 'ế': 'ế', 'ở': 'ở', 'ỉ': 'ỉ', 'ẻ': 'ẻ', 'àk': 'à',
                     'ak`': 'à','gía': 'giá', 
                     'a`': 'à', 'iˋ': 'ì', 'ă´': 'ắ','ử': 'ử', 'e˜': 'ẽ', 'y˜': 'ỹ',
                     'a´': 'á', ' rũ ': ' rủ ',
                     #các từ được viết tắt
                     ' ùi ':' rồi ', ' rùi ': ' rồi ', ' ròi ': ' rồi ', ' roài ':' rồi ', ' km ': ' khuyến mãi ',
                     ' hnai': ' hôm nay ', ' hnay': ' hôm nay ', '0k ': ' giá cả ','1k ': ' giá cả ',
                     '2k ': ' giá cả ','3k ': ' giá cả ','4k ': ' giá cả ','5k ': ' giá cả ',
                     '6k ': ' giá cả ','7k ': ' giá cả ','8k ': ' giá cả ','9k ': ' giá cả ',
                     ' k ': ' không ', ' nv ': ' nhân viên ', ' cfe ': ' cafe ', ' cphe ': ' cafe ',
                     ' caphe ': ' cafe ', ' bt ': ' bình thường ', ' ko ': ' không ',' đôg uống ':' đồ uống ',
                     ' ae ': ' anh em ', ' ce ':' chị em ', ' ace ': ' anh chị em ', ' vs ': ' với ',
                     ' bt ': ' bình thường ', ' nt ': ' nhắn tin ', ' mik ': ' mình ', ' cf ': ' cafe ',
                     ' như v ': ' như vậy ',
                     #các từ tiếng anh
                     'boardgame': 'trò chơi trên bàn', 'dilivery': 'giao hàng',
                     'fre': 'miễn phí', 'free': 'miễn phí', 'order': 'đặt hàng',
                     'sandwich': 'bánh mì', 'hamburger': 'bánh mì', 'matcha': 'nước uống',
                     ' decor ': ' trang trí ', ' ok': ' ổn ', ' take away': ' mang đi ', 'smothies': 'nước uống',
                     'americano': 'nước uống',  ' ice blended ': ' nước uống ', ' cokie cream ': ' nước uống ',   
                     ' milk tea ': ' nước uống ', ' cocktail': ' nước uống ', ' puding ': ' bánh ', ' flan ': ' bánh ',

                     }
     for k, v in replace_list.items():
          text = text.replace(k, v)
     return text

#loại bỏ các dữ liệu không có ý nghĩa (không có trong bộ stop word)
def remove_nonsense_word(text):
     remove_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'hi hi', 'hì hì', 'he he', 'ha ha', 'hê hê', 'há há', 'hề hề', 'hè hè',
                    'bình thường'
                    ]
     for k in remove_list:
          text = text.replace(k,' ')
     return text

#loại bỏ các khoảng trắng dư thừa
def remove_space_redundant(text):
     text = text.strip()
     text = re.sub(' +', ' ',text)
     return text


#loại bỏ các stopword
def remove_stopword(text):
     for k in stopword_var:
          k = ' ' + k + ' '
          text = ' ' + text + ' '
          text = text.replace(k,' ')
     return text

#tiền xử lý 1 chuỗi dữ liệu
def string_preprocessing(text):
     #lowercase tất cả các string
     text = text.lower()   

     #loại bỏ các symbol
     text = remove_symbol(text)

     #loại bỏ các dấu câu
     translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
     text = text.translate(translator)

     #loại bỏ các kí tự kéo dài
     text = re.sub(r'([A-Z])\1+', lambda m: m.group(1).lower(), text, flags=re.IGNORECASE)  

     #thay thế các từ viết tắt, sai chính tả
     text = replace_word(text)

     #loại bỏ các dữ liệu dư thừa sau khi đã replace
     text = remove_nonsense_word(text)

     #bỏ các khoảng space thừa 
     # text = remove_space_redundant(text)

     #loại bỏ stopword dùng bộ từ điển stopword 
     # text= remove_stopword(text)

     #tách từ dùng bộ từ tiếng việt của pyvi 
     text = ViTokenizer.tokenize(text)

     return text

#xử lý list dữ liệu
def data_preprocessing(list_data):
     length = len(list_data)
     for i in range(length):
          list_data[i] = string_preprocessing(list_data[i])
     return list_data

#xuất dữ liệu ra csv file theo từng cột
id_var = list(train_data.id)
comment_var1 = data_preprocessing(comment_var)
food_var = list(train_data.food)
drink_var = list(train_data.drink)
price_var = list(train_data.price)
staff_var = list(train_data.staff)
service_var = list(train_data.service)
space_var = list(train_data.space)
hygiene_var = list(train_data.hygiene)

Cars = {'id': id_var,
        'comment': comment_var1,
        'food': food_var,
        'drink': drink_var,
        'price': price_var,
        'staff': staff_var,
        'service': service_var,
        'space': space_var,
        'hygiene': hygiene_var,
        }

df = DataFrame(Cars, columns= ['id', 'comment','food','drink','price','staff','service','space','hygiene'])
export_csv = df.to_csv ('data.csv', index = None, header=True)


########test
# print(data_preprocessing(comment_var))

