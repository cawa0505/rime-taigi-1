from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from urllib.request import urlopen
import io
from csv import DictReader
from _cffi_backend import typeof
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


def 頭字轉大寫(im):
    try:
        return im[0].upper() + im[1:]
    except Exception:
        print('im: {}'.format(im))
        raise


def 提教典表():
    github網址 = 'https://github.com/g0v/moedict-data-twblg/raw/master/uni/'
    詞目總檔網址 = (
        github網址 + '%E8%A9%9E%E7%9B%AE%E7%B8%BD%E6%AA%94.csv'
    )
    kauTian = set()
    with urlopen(詞目總檔網址) as 檔:
        with io.StringIO(檔.read().decode()) as 資料:
            for row in DictReader(資料):
                臺羅 = row['音讀'].strip()
                if 臺羅 == '':
                    continue
                臺羅s = 臺羅.split('/')
                漢字 = row['詞目'].strip()
                for lo in 臺羅s:
                    kuBuKian = 拆文分析器.建立句物件(lo).轉音(臺灣閩南語羅馬字拼音)
                    sooJiTiau = kuBuKian.看語句()
                    if sooJiTiau is None:
                        print(lo, 漢字)
                    kauTian.add((漢字, sooJiTiau))
                    kauTian.add((lo, sooJiTiau))
        return kauTian


dict_header = '''# Rime dictionary
# encoding: utf-8

---
name: taigi
version: "0.1"
sort: by_weight
use_preset_vocabulary: false
...'''

#
# 程式頭
#
with open('taigi.dict.yaml', 'w', encoding='utf-8') as f:
    # 輸出字典踏話頭
    print(dict_header, file=f)
    pio = set()
    # 提著數字調號
    for siannBo in 臺灣閩南語羅馬字拼音.聲母表:
        for unBo in 臺灣閩南語羅馬字拼音.韻母表:
            if unBo[-1] in 'hptk':
                tiauArr = '4', '8'
            else:
                tiauArr = '1', '2', '3', '5', '6', '7', '9'
            for tiau in tiauArr:
                pio.add('{}{}{}'.format(siannBo, unBo, tiau))
    # 印傳統調號的羅馬字音節表
    for im in sorted(pio):
        tiauIm = 臺灣閩南語羅馬字拼音(im).轉調符()
        if tiauIm is not None:
            # 一般
            print('{}\t{}\t10%'.format(tiauIm, im), file=f)
            # 大寫
            print('{}\t{}\t10%'.format(頭字轉大寫(tiauIm), 頭字轉大寫(im)), file=f)
    # 印教典詞
    教典 = 提教典表()
    for ji, im in sorted(教典, key=lambda tup: (tup[1],tup[0])):
        khangPehLianIm = im.replace('-', ' ')
        print('{}\t{}'.format(ji, khangPehLianIm), file=f)
