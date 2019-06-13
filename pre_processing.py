import pandas as pd
import re
import string
from pyvi import ViTokenizer

#remove special charaters
def remove_symbol(text):
     remove_list =[
                    #remove symbol and down the line
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

#replace abbreviation, wrong letter, wrong spelling, english
def replace_word(text):
     replace_list = {
                    #wrong spelling, teen code
                    'òa': 'oà', 'óa': 'oá', 'ỏa': 'oả', 'õa': 'oã', 'ọa': 'oạ', 'òe': 'oè',
                     'óe': 'oé','ỏe': 'oẻ', 'õe': 'oẽ', 'ọe': 'oẹ', 'ùy': 'uỳ', 'úy': 'uý',
                     'ủy': 'uỷ', 'ũy': 'uỹ','ụy': 'uỵ', 'uả': 'ủa', 'ả': 'ả', 'ố': 'ố',
                     'u´': 'ú','ỗ': 'ỗ', 'ồ': 'ồ', 'ổ': 'ổ', 'ấ': 'ấ', 'ẫ': 'ẫ',
                     'ẩ': 'ẩ', 'ầ': 'ầ', 'ỏ': 'ỏ', 'ê`': 'ề','ễ': 'ễ', 'ắ': 'ắ', 
                     'ủ': 'ủ', 'ế': 'ế', 'ở': 'ở', 'ỉ': 'ỉ', 'ẻ': 'ẻ', 'àk': 'à',
                     'ak`': 'à','gía': 'giá', 
                     'a`': 'à', 'iˋ': 'ì', 'ă´': 'ắ','ử': 'ử', 'e˜': 'ẽ', 'y˜': 'ỹ',
                     'a´': 'á', ' rũ ': ' rủ ',
                     #abbreviation
                     ' ùi ':' rồi ', ' rùi ': ' rồi ', ' ròi ': ' rồi ', ' roài ':' rồi ', ' km ': ' khuyến mãi ',
                     ' hnai': ' hôm nay ', ' hnay': ' hôm nay ', '0k ': ' giá cả ','1k ': ' giá cả ',
                     '2k ': ' giá cả ','3k ': ' giá cả ','4k ': ' giá cả ','5k ': ' giá cả ',
                     '6k ': ' giá cả ','7k ': ' giá cả ','8k ': ' giá cả ','9k ': ' giá cả ',
                     ' k ': ' không ', ' nv ': ' nhân viên ', ' cfe ': ' cafe ', ' cphe ': ' cafe ',
                     ' caphe ': ' cafe ', ' bt ': ' bình thường ', ' ko ': ' không ',' đôg uống ':' đồ uống ',
                     ' ae ': ' anh em ', ' ce ':' chị em ', ' ace ': ' anh chị em ', ' vs ': ' với ',
                     ' nt ': ' nhắn tin ', ' mik ': ' mình ', ' cf ': ' cafe ',
                     ' như v ': ' như vậy ', ' rẻ ': ' giá cả ', ' mắc ': ' giá cả ',
                     #english
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

#remove nonsense words
def remove_nonsense_word(text):
     remove_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'hi hi', 'hì hì', 'he he', 'ha ha', 'hê hê', 'há há', 'hề hề', 'hè hè',
                    'bình thường'
                    ]
     for k in remove_list:
          text = text.replace(k,' ')
     return text

#remove redundant space
def remove_space_redundant(text):
     text = text.strip()
     text = re.sub(' +', ' ',text)
     return text


#remove stopword
def remove_stopword(text):
     # read stopword from csv
     stopword = pd.read_csv('stop_word.csv',sep=',',keep_default_na=False)
     stopword_var = list(stopword)
     for k in stopword_var:
          k = ' ' + k + ' '
          text = ' ' + text + ' '
          text = text.replace(k,' ')
     return text

#preprocessing a string
def string_preprocessing(text):
     #lowercase all string
     text = text.lower()   

     #remove symbols
     text = remove_symbol(text)

     #remove punctuation
     translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
     text = text.translate(translator)

     #remove long string (like "rất ngonnnnnnnnnnnnnnnnnnnn")
     text = re.sub(r'([A-Z])\1+', lambda m: m.group(1).lower(), text, flags=re.IGNORECASE)  

     #replace wrong spelling, wrong letter
     text = replace_word(text)

     #remove nonsense data
     text = remove_nonsense_word(text)

     #remove redundant space
     # text = remove_space_redundant(text)

     #remove stop word
     # text= remove_stopword(text)

     #Token using library of PyVi
     text = ViTokenizer.tokenize(text)

     return text

#preprocessing list of data
def data_preprocessing(list_data):
     length = len(list_data)
     for i in range(length):
          list_data[i] = string_preprocessing(list_data[i])
     return list_data





