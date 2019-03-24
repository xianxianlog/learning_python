# 挑选一部分种类来分析
read_file_list=['乳类','干豆类','水果类','油脂类','肉类','蔬菜类']

d={
'乳类': ['牛乳(美国牛)',' 牛乳(西德牛) ', ' 鲜羊乳 ', ' 人乳 ', ' 酸奶(均值) ', ' 酸奶(中脂) ', ' 中脂软酪 ', ' 奶油 ', ' 奶油(焦克) ', ' 奶油(食品工业) ',
         ' 黄油 '],
'干豆类':[' 黄豆[大豆] ', ' 黑豆[黑大豆] ', ' 青豆[青大豆] ', ' 绿豆 ', ' 赤小豆[小豆，红小豆] ', ' 花豆(红) ', ' 花豆(紫) ', ' 芸豆(白) ', ' 芸豆(红) ',
         ' 芸豆(虎皮) ', ' 芸豆(杂，带皮) ', ' 蚕豆 ', ' 蚕豆(带皮) ', ' 蚕豆(去皮) ', ' 马牙大豆 ', ' 脑豆 ', ' 扁豆(白) ', ' 眉豆[饭豇豆] ', ' 豇豆 ',
         ' 豇豆(紫) ', ' 豌豆 ', ' 豌豆(花) ', ' 荆豆 ', ' 木豆[扭豆，豆蓉] ', ' 扁豆 '],
'水果类':[' 伏苹果 ', ' 国光苹果 ', ' 旱苹果 ', ' 红富士苹果 ', ' 红香蕉苹果 ', ' 红星苹果 ', ' 红玉苹果 ', ' 红元帅苹果 ', ' 黄香蕉苹果 ', ' 黄元帅苹果 ',
          ' 金元帅苹果 ', ' 青香蕉苹果 ', ' 秋里蒙苹果 ', ' 香玉苹果 ', ' 印度苹果 ', ' 祝光苹果 ', ' 倭锦苹果 ', ' 巴梨 ', ' 鹅黄梨 ', ' 红肖梨 ', ' 长把梨 ',
          ' 冬果梨 ', ' 锦丰梨 ', ' 京白梨 ', ' 莱阳梨 ', ' 库尔勒梨 ', ' 马蹄黄梨 ', ' 木梨 ', ' 明月梨 ', ' 苹果梨 ', ' 软梨 ', ' 苏梅梨 ', ' 苏木梨 ',
          ' 酥梨 ', ' 酸梨 ', ' 香梨 ', ' 雪花梨 ', ' 雪梨 ', ' 鸭广梨 ', ' 鸭梨 ', ' 早酥梨 ', ' 紫酥梨 ', ' 鳄梨 ', ' 红果[山里红，大山楂] ',
          ' 红果(干) ', ' 海棠果[楸子] ', ' 吊蛋 ', ' 沙果 ', ' 面蛋 ', ' 酸刺 ', ' 白粉桃 ', ' 高山白桃 ', ' 旱久保桃 ', ' 黄桃 ', ' 金红桃 ', ' 久保桃 ',
          ' 蜜桃 ', ' 蒲桃 ', ' 庆丰桃 ', ' 晚桃(黄) ', ' 五月鲜桃 ', ' 早桃(黄) ', ' 李子 ', ' 李子杏 ', ' 梅[青梅] ', ' 杏 ', ' 枣(鲜) ',
          ' 金丝小枣 ', ' 乐陵枣 ', ' 密云小枣 ', ' 黑枣(无核)[乌枣] ', ' 黑枣(有核) ', ' 酒枣 ', ' 蜜枣 ', ' 酸枣 ', ' 樱桃(野，白刺) ', ' 樱桃 ',
          ' 红玫瑰葡萄 ', ' 巨峰葡萄 ', ' 马奶子葡萄 ', ' 玫瑰香葡萄 ', ' 紫葡萄 ', ' 红粉皮石榴 ', ' 玛瑙石榴 ', ' 青皮石榴 ', ' 柿 ', ' 荷柿 ', ' 磨盘柿 ',
          ' 桑葚(白) ', ' 桑葚(红) ', ' 醋栗[灯笼果] ', ' 黑醋栗[黑加仑] ', ' 沙棘 ', ' 无花果 ', ' 中华猕猴桃[毛叶猕猴桃] ', ' 草莓[洋莓，凤阳草莓] ', ' 橙 ',
          ' 福桔 ', ' 桔柑子[宽皮桂] ', ' 金桔[金枣] ', ' 芦柑 ', ' 蜜桔 ', ' 四川红桔 ', ' 三湖红桔 ', ' 小叶桔 ', ' 早桔 ', ' 桔饼 ', ' 柠檬 ',
          ' 芭蕉[甘蕉，板蕉，牙蕉] ', ' 柚[文旦] ', ' 菠萝[凤梨，地菠萝] ', ' 菠萝蜜[木菠萝] ', ' 刺梨[茨梨，木梨子] ', ' 番石榴[鸡矢果，番桃] ', ' 桂圆 ', ' 黄皮果 ',
          ' 荔枝 ', ' 芒果[抹猛果，望果] ', ' 木瓜[番木瓜] ', ' 人参果 ', ' 香蕉[甘蕉] ', ' 杨梅[树梅，山杨梅] ', ' 杨桃 ', ' 椰子 ', ' 枇杷 ', ' 橄榄(白榄) ',
          ' 白金瓜 ', ' 白兰瓜 ', ' 余柑子[油柑子] ', ' 哈蜜瓜 ', ' 黄河蜜瓜 ', ' 金塔寺瓜 ', ' 灵蜜瓜 ', ' 麻醉瓜 ', ' 甜瓜[香瓜] ', ' 西瓜(均值) ',
          ' 西瓜(京欣一号) ', ' 西瓜(郑州三号) ', ' 西瓜(忠于6号，黑皮) ', ' 籽瓜 '],
'油脂类':[' 牛油 ', ' 羊油 ', ' 猪油(板油) ', ' 菜籽油[青油] ', ' 大麻油 ', ' 茶油 ', ' 豆油 ', ' 红花油 ', ' 胡麻油 ', ' 花生油 ', ' 葵花籽油 ', ' 辣椒油 ',
       ' 麻子籽 ', ' 麦芽油 ', ' 棉籽油 ', ' 色拉油 ', ' 椰子油 ', ' 玉米油 ', ' 芝麻油[香油] ', ' 棕榈油 ', ' 橄榄油 '],
'肉类':[' 猪肉(肥瘦)(均值) ', ' 牛肉(肥瘦)(均值) ', '羊肉(肥瘦)(均值) ', ' 羊肉(青羊) ', ' 山羊肉(冻) ', ' 驴肉(瘦) ', ' 马肉 ', ' 狗肉 ', ' 兔肉 ',
        ' 兔肉(野) ', ' 鸡(土鸡，家养) ', ' 母鸡(一年内) ', ' 肉鸡(肥) ', ' 沙鸡 ', ' 乌骨鸡 ', ' 华青鸡 ', ' 公麻鸭 ', ' 母麻鸭 ', ' 鹅 ', ' 鸽 ',
        ' 鹌鹑 '],
'蔬菜类':[' 白萝卜[莱菔] ', ' 变萝卜[红皮萝卜] ', ' 红旦旦萝卜 ', ' 红萝卜 ', ' 红心萝卜 ', ' 花叶萝卜 ', ' 青萝卜 ', ' 水萝卜[脆萝卜] ',
              ' 小水萝卜[算盘子，红皮萝卜] ', ' 心里美萝卜 ', ' 胡萝卜(红)[金笋，丁香萝卜] ', ' 胡萝卜(黄) ', ' 芥菜头[大头菜，水芥] ', ' 苤蓝[玉蔓菁，球茎甘蓝] ',
              ' 甜菜根[甜菜头，糖萝卜] ', ' 黄豆芽 ', ' 豌豆苗 ', ' 绿豆芽 ', ' 茄子(绿皮) ', ' 茄子(圆) ', ' 茄子(紫皮，长) ', ' 番茄[西红柿] ',
              ' 奶柿子[西红柿] ', ' 辣椒(红，小) ', ' 辣椒(青，尖) ', ' 甜椒[灯笼椒，柿子椒] ', ' 葫子 ', ' 秋葵[黄秋葵，羊角豆] ', ' 白瓜 ', ' 菜瓜[生瓜，白瓜] ',
              ' 冬瓜 ', ' 方瓜 ', ' 佛手瓜[棒瓜，菜肴梨] ', ' 葫芦[长瓜，蒲瓜，瓠瓜] ', ' 黄瓜[胡瓜] ', ' 节瓜[毛瓜] ', ' 金瓜 ', ' 金丝瓜[裸瓣瓜] ',
              ' 苦瓜[凉瓜，癞瓜] ', ' 南瓜[倭瓜，番瓜] ', ' 蛇瓜[蛇豆，大豆角] ', ' 丝瓜 ', ' 笋瓜[生瓜] ', ' 西葫芦 ', ' 面西胡瓜 ', ' 小西胡瓜 ', ' 大蒜[蒜头] ',
              ' 大蒜(紫皮) ', ' 青蒜 ', ' 蒜苗 ', ' 蒜黄 ', ' 蒜苔 ', ' 大葱 ', ' 大葱(红皮) ', ' 分葱[四季葱，菜葱] ', ' 细香葱[香葱，四季葱] ', ' 小葱 ',
              ' 洋葱(紫皮，脱水) ', ' 韭菜 ', ' 韭黄[韭芽] ', ' 韭苔 ', ' 薤白[小根蒜，山蒜，团蒜] ', ' 大白菜(青白口) ', ' 大白菜(白梗)[黄芽白] ',
              ' 大白菜(小白口) ', ' 小白菜 ', ' 白菜薹[菜薹，菜心] ', ' 红菜薹[紫菜薹] ', ' 瓢儿白[瓢儿菜] ', ' 油菜 ', ' 乌菜[乌塌菜，塌棵菜] ', ' 油菜(黑) ',
              ' 油菜(小) ', ' 油菜薹[菜薹] ', ' 甘蓝[圆白菜，卷心菜] ', ' 菜花[花椰菜] ', ' 西兰花[绿菜花] ', ' 芥菜[雪里红，雪菜] ', ' 芥菜(大叶)[盖菜] ',
              ' 芥菜(茎用)[青头菜] ', ' 菠菜[赤根菜] ', ' 芥蓝[甘蓝菜，盖蓝菜] ', ' 冬寒菜[冬苋菜，冬葵] ', ' 观达菜[根达菜，牛皮菜] ', ' 胡萝卜缨(红) ',
              ' 苦菜[节节花，拒马菜] ', ' 芥菜(小叶)[小芥菜] ', ' 萝卜缨(白) ', ' 萝卜缨(青) ', ' 萝卜缨(小萝卜) ', ' 落葵[木耳菜，软浆菜] ',
              ' 芹菜(白茎)[旱芹，药芹] ', ' 芹菜叶 ', ' 生菜(牛俐)[油麦菜] ', ' 芹菜茎 ', ' 生菜(叶用莴苣) ', ' 甜菜叶 ', ' 香菜[芫荽] ', ' 苋菜(紫)[红苋] ',
              ' 苋菜(绿) ', ' 茼蒿[蓬蒿菜，艾菜] ', ' 荠菜[蓟菜，菱角菜] ', ' 莴笋叶[莴苣叶] ', ' 莴笋[莴苣] ', ' 蕹菜[空心菜，藤藤菜] ', ' 竹笋 ', ' 春笋 ',
              ' 鞭笋[马鞭笋] ', ' 冬笋 ', ' 毛笋[毛竹笋] ', ' 玉兰片 ', ' 百合 ', ' 金针菜[黄花菜] ', ' 菊苣 ', ' 芦笋[石刁柏，龙须菜] ',
              ' 豆瓣菜[西洋菜，水田芥] ', ' 藕[莲藕] ', ' 菱角(老)[龙角] ', ' 蒲菜[香蒲，甘蒲，野茭白] ', ' 水芹菜 ', ' 茭白[茭笋，茭粑] ', ' 荸荠[马蹄，地栗] ',
              ' 莼菜(瓶装)[花案菜] ', ' 大薯[参薯] ', ' 豆薯[凉薯，地瓜，沙葛] ', ' 葛[葛署，粉葛] ', ' 山药[薯蓣，大薯] ', ' 芋头[芋艿，毛芋] ', ' 槟榔芋 ',
              ' 姜[黄姜] ', ' 姜(子姜)[嫩姜] ', ' 洋姜[菊芋，鬼子姜] ', ' 艾蒿 ', ' 白花菜 ', ' 白花桔梗 ', ' 白沙蒿[沙蒿] ', ' 白薯叶[甘薯叶] ', ' 百里香 ',
              ' 败酱[胭脂麻] ', ' 扁蓄菜[竹节草] ', ' 朝鲜蓟 ', ' 刺楸 ', ' 刺儿菜[小蓟，蓟蓟菜] ', ' 大玻璃草叶[大车前] ', ' 大巢菜[野苕子，野豌豆] ',
              ' 大蓟叶[飞廉叶] ', ' 地肤[益明，扫帚苗] ', ' 独行菜 ', ' 独行菜(宽) ', ' 番杏[夏菠菜，新西兰菠菜] ', ' 胡枝子[山豆子] ']
}

import pandas as pd
import json
import numpy as np

# 提取筛选数据形成dataframe
all_food_dataframe=list()
for file_name in read_file_list:
    food_name_list=list()
    food_list=list()
    with open("data/"+file_name,"r",encoding="utf-8") as f:
        while True:
            line=f.readline()
            if line:
                food_dict={}
                line=json.loads(line)
                food_dict['种类']=file_name
                food_name_list.append(line['name'].strip())
                nutrition_dict={}
                nutrition=line['data']
                for nutrition_data in nutrition:
                    for nutrition_name,nutrition_number in nutrition_data.items():
                        try:
                            food_dict[nutrition_name.strip()]=float(nutrition_number)
                        except:
                            pass
            else:
                break

            food_list.append(food_dict)

    food_select=[i.strip() for i in d[file_name]]

    food_df=pd.DataFrame(food_list,index=food_name_list)
    food_df_select=food_df.loc[food_select,:]
    #print(food_df_select)
    all_food_dataframe.append(food_df_select)


# 合并成一个大dataframe
big_frame=pd.DataFrame([])
for food in all_food_dataframe:
    big_frame=pd.concat([big_frame,food])

big_frame=big_frame.dropna(axis=0,how="any") # 缺失值处理


# 绘图
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib as mp
import re

#设置字体
my_font=font_manager.FontProperties(fname="c:/Windows/Fonts/STXINWEI.TTF")

# 1.不同种类的食品的各种营养素的平均值的所占百分比
group_df=big_frame.groupby(by="种类").mean() # 分组计算平均值
food_kind=group_df.index
print(food_kind)
for kind in list(food_kind):
    sizes=group_df.loc[kind,:]
    sizes=sizes[sizes>0.00001] # 含量太小的不做计算
    print(sizes)
    explode=[0 for i in range(len(sizes))]
    labels=sizes.index
    plt.figure(dpi=80)
    p=plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90,radius=1)
    # 设置中文正常显示
    for front in p[1]:
        front.set_fontproperties(mp.font_manager.FontProperties(
            fname="c:/Windows/Fonts/STXINWEI.TTF"))
    plt.title(kind,fontproperties=my_font)
    plt.show()

# 2.不同营养素的top5食物
nutrition_kind_list=[i for i in big_frame.drop('种类',axis=1).iloc[0,:].index]
print(nutrition_kind_list)
for nutrition in nutrition_kind_list:
    nutrition_s=big_frame[nutrition].sort_values(ascending=False)
    plt.figure(dpi=80)
    nutrition_s_top=nutrition_s.head(5)
    _x=nutrition_s_top.index
    _y=nutrition_s_top.values
    plt.bar(range(len(_x)),_y,width=0.5,)
    plt.xticks(range(len(_x)),_x,fontproperties=my_font)
    ret=re.match(r"(.+)\((.+)\)",nutrition)# 提取标题和单位
    unit=ret.group(2)
    title=ret.group(1)
    plt.xlabel("食物名称",fontproperties=my_font)
    plt.ylabel("含量(%s)"%unit,fontproperties=my_font)
    plt.title(title+"含量最高的5种食物",fontproperties=my_font)
    plt.show()
