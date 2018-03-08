# vn
vn is terminal tool to help people learn English

## Install
```bash
pip install git+https://github.com/togatoga/vn.git  # or pipsi install
```
### Docker

```bash
git clone https://github.com/togatoga/vn
cd vn
docker build -t vn .

alias vn="docker run -it --rm vn vn"
alias vni="docker run -it --rm vn vn translate --interactive"
alias vnt="docker run -it --rm vn vn translate $*"
```

### Usage

vn command automatically decide translation rule.
if you type Japanese word, vn translate word to English(Japanese -> English) and vice versa(English -> Japanese).
#### Translate

```bash
% vn translate 不労所得
translate... 不労所得 from jpn to eng
Translation:
         - unearned income
         - unearned revenue
Example:
        ENG - また 、 明治 政府 の 財政 難 の 原因 と な る 不労 所得 者 で あ る 士族 の 特権 ( 秩禄 、 賞典 禄 ) を 削減 し たり ( 秩禄 処分 ) 、 廃刀 令 を 出 し たり し た 。
        JPN - Okubo , additionally implemented Chitsuroku-shobun ( Abolition Measure of Hereditary Stipend ) reducing special privileges ( such as Chiroku ( hereditary stipend ) and Shotenroku ( bonus ) ) of the warrior class who received unearned income and contributed to economic difficulties for the Meiji Government , and issued a decree banning the wearing of swords .

        ENG - だ が 、 日本 で は 法律 上 は 不労 所得 だ が 、 欧米 で は 所得 で あ る こと が 多 い 。
        JPN - However , in Japan this is regarded as unearned income , while in the West it is often regarded as ordinary income .

        ENG - ちなみ に 日本 で は 株式 市場 の 証券 取引 も 賭け事 と さ れ て い る 為 不労 所得 で あ る 。
        JPN - In Japan , since the trading of stocks on the stock exchange is considered gambling , income from trading is regarded as unearned income .
```

##### Interactive Mode
```bash
% vn translate -i
:q quit
[vn] > devotion
translate... devotion from eng to jpn
Translation:
         - 信心
         - 傾注
         - 熱愛
         - 献身
         - 篤信
         - 帰依
         - 執心
         - 忠信
         - 忠愛
         - 忠義
         - 真心
         - 精進
Synonyms:
         -  devotion, devotedness, idolatry, veneration, cultism
Example:
        ENG - She was inspired by the trust of the blind man and the devoted love of his friend.
        JPN - そしてその選手の信頼と,友人の献身的な愛に心を動かされました。

        ENG - Hanna says that he fell in love with jukeboxes right away and quickly decided to devote himself full-time to repairing them.
        JPN - 彼は、ジュークボックスを初めて見た時から、すぐにその虜になり修理をする仕事に就くことを決めた。

        ENG - Mabuchi rejected Confucian thought and believed that the true spirit of the ancient Japanese was to be found in the " Manyoshu " , devoting his life to researching it .
        JPN - 真淵 は 儒教 的 な 考え を 否定 し て 『 万葉 集 』 に 古 い 時代 の 日本 人 の 精神 が 含 ま れ て い る と 考え て その 研究 に 生涯 を 捧げ た 。

        ENG - Beginning with the fire of 1125 , the temple can be confirmed to have met with disaster on at least 18 separate occasions by the end of the Edo period but its importance as a place of devotion for the masses and the hub of the community meant that it was rebuilt each time .
        JPN - この 寺 は 、 1125 年 ( 天治 2 年 ) の 火災 を はじめ 、 江戸 時代 末 まで の 間 に 確認 でき る だけ で 18 回 の 災害 に あ っ た が 、 庶民 の 信仰 を 集め る 寺 で あ り 、 また 町組 の  中核 と な る 寺 と し て その 都度 復興 さ れ て き た 。

        ENG - Rather, it is a reflection of the love and devotion of godly men, women, and children throughout the earth.
        JPN - この部分には,世界中の敬虔な男女,子どもの愛と献身が反映されています。

        ENG - I am 85” (“Be Still, and Know That I Am God” [Church Educational System devotional, May 4, 2014], broadcasts.lds.org).
        JPN - 静まって,わたしこそ神であることを知れ」〔教会教育システムディボーショナル,2014年5月4日〕,broadcasts.lds.org)

        ENG - Nichioni became the 13th monzeki and had devoted herself to reestablish the Zuiryu-ji Temple until March 20 , 2002 when she died at the age of 89 .
        JPN - 13 世 門跡 と な っ た 日 鳳 尼 は 平成 14 年 ( 2002 年 ) 3 月 20 日 に 89 歳 で 遷化 する まで 瑞龍 寺 の 復興 に 寄与 し た 。
[vn] > 修行
translate... 修行 from jpn to eng
Translation:
         - discipline
         - training
         - ascetic practice
         - ascetic practise
         - learning
         - pursuit of knowledge
         - study
         - studying
         - ascetic practices
         - practice
Example:
        JPN - 菩薩 が 、 十住 位 の 終 に 仏子 た る 印可 を 得 た 後 、 更に 進 ん で 利他 の 修行 を 完う せ ん 為 に 衆生 を 済度 する こと に 努め る 位 。
        ENG - This is the rank where Bosatsu tries to relieve the living things in order to complete more altruistic training after getting a certification ( 印可 ) as a Buddhist ( 仏子 ) at the end of Juju .

        JPN - また 、 修行 時代 の 了翁 は この 神社 に スギ 苗 580 株 余り を 植え た と い う 。
        ENG - It is said that Ryoo planted five hundreds and eighty cedar seedlings during his ascetic practice period .

        JPN - 修行 場 は 「 靡 」 ( なびき ) と 呼 ば れ 、 ひと つ ひと つ に 番号 が 割り当て られ て い る 。
        ENG - Ascetic practice places are referred to as " nabiki , " and each of them is given an individual number .

        JPN - 8 歳 で 臨済 宗 聖一 派 東山 湛照 ( と うざん たんしょう ) に 師事 し て 参禅 し 、 東山 の 没後 は 規庵 祖 円 ・ 桃 渓 徳 悟ら に つ い て 修行 し た 。
        ENG - He became the disciple of Rinzai Sect Shoichi School monk Tozan Tansho at age 8 and practiced Zen before going on to practice under Kian Soen and Tokei Tokugo after Tozan 's death .

        JPN - 金王 丸 は 鎌倉 御曹司 ( 源義 平 ) も 兵衛 佐 様 ( 源 頼朝 ) も 捕らわれ て しま い 、 幼 い 弟 君 も 頼り な い こと で しょ う と い い 、 よ っ て 、 金王 丸 は 義朝 の 後世 を 弔 う 為  に 出家 する と 申し述べ て その まま 走 り 出 て い っ た と い い 、 どこ か の 寺 にて 修行 し て 諸国 七 道 を 歩 い た と い う 。
        ENG - Konomaru locked up the son of a Kamakura noble ( MINAMOTO no Yoshihira ) and also part of the watch ( MINAMOTO no Noriyori ) , and is said to have tried to have no reliance placed on his infant younger brothers , accordingly , because Konomaru mourned the passing of Yoshitomo it is said he left the family and the story goes that he just walked away and lived the life of an ascetic in temples , wandering the high roads and low roads of various provinces .

        JPN - 師匠 は 弟子 の 修行 が 十分 に 達成 さ れ た と 判断 し た 時 、 仏法 の 核心 を 伝授 し 、 その 証 と し て 祖師 伝来 の 袈裟 と 持 鉢 を 与え る 。
        ENG - In some sects , a simplified-type kesa called wagesa is used by laypersons when taking part in a Buddhist mass .

        JPN - この ため 、 乱 は 能楽師 の 修行 の 過程 に お い て 、 重要 な 階梯 で あ る と 考え られ 、 初演 を 披 き と し て 重 く 扱 う 。
        ENG - Therefore , the acquisition of the midare is considered to be important at the training , and the first performance of the midare is even considered to be the performer 's debut .
[vn] >:q

```
