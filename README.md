# vn
vn is terminal tool to help people learn English

## Install

### Docker

```bash
git clone https://github.com/togatoga/vn
cd vn
docker build -t vn .

alias vn="docker run -it --rm vn python vn.py"
alias vnt="docker run -it --rm vn python vn.py translate $*"

```

### Usage

vn command automatically decide translation rule.
if you type Japanese word, vn translate word to English(Japanese -> English) and vice versa(English -> Japanese).
#### Translate

```bash
% python vn.py translate 不労所得
translate... 不労所得 from jpn to eng
Translate: unearned income
Meaning: income which is not a wage
Translate: unearned revenue

% python vn.py translate "unearned income"
translate... unearned income from eng to jpn
Translate: 不労所得
Meaning: income which is not a wage
Translate: ふろうしょとく
Meaning: (taxation) Income that is not a wage, such as interest, dividends or realized capital gains from investments, rent from land or property ownership, and any other income that does not derive from work.
Meaning: (accounting) income received but not yet earned (usually considered a current liability on a company&#39;s balance sheet)
Meaning: Income that is not a wage, such as interest, dividends or realized capital gains from investments, rent from land or property ownership, and any other income that does not derive from work.
Meaning: personal income that you did not earn (e.g., dividends or interest or rent income)

```

##### Interactive Mode
```bash
% python vn.py translate -i
:q quit
> devotion
translate... devotion from eng to jpn
Translate: 信心
Translate: 傾注
Translate: 熱愛
Translate: 献身
Translate: 篤信
Translate: 帰依
Meaning: (religious) conversion
Translate: 執心
Translate: 忠信
Translate: 忠愛
Translate: 忠義
> 修行
translate... 修行 from jpn to eng
Translate: discipline
Translate: training
Translate: ascetic practice
Translate: ascetic practise
Translate: learning
Translate: pursuit of knowledge
Translate: study
Translate: studying
Translate: ascetic practices
Translate: practice
> :q

```
