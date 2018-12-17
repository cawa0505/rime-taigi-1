from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


def 頭字轉大寫(im):
    try:
        return im[0].upper() + im[1:]
    except Exception:
        print('im: {}'.format(im))
        raise


#
# 程式頭
#
dict_header = '''# Rime dictionary
# encoding: utf-8

---
name: taigi
version: "0.1"
sort: by_weight
use_preset_vocabulary: false
...'''

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
    # 提著傳統調號
    for im in sorted(pio):
        tiauIm = 臺灣閩南語羅馬字拼音(im).轉調符()
        if tiauIm is not None:
            # 一般
            print('{}\t{}\t10%'.format(tiauIm, im), file=f)
            # 大寫
            print('{}\t{}\t10%'.format(頭字轉大寫(tiauIm), 頭字轉大寫(im)), file=f)
