from pathlib import Path

files = [
    "前言.md",
    "序一：打开红楼大门的金钥匙.md",
    "序二.md",
    "第八十一回 惜昵近公子做良媒 讳笞罚丫鬟结恶党.md",
    "第八十二回 王熙凤病求千翼方 林黛玉闷作十独吟.md",
    "第八十三回 史太君临终念子孙 王夫人膏肓托儿女.md",
    "第八十四回 薛宝钗弥望金玉缘 史湘云喜得如意郎.md",
    "第八十五回 痴王孙传信牵奇缘 惭妙尼避情乘游槎.md",
    "第八十六回 挑正庶风月断佳偶 祭祖祠清明泣远嫁.md",
    "第八十七回 花柳质命断无情兽 绣户女自绝美韶华.md",
    "第八十八回 邢夫人执意寻舛错 王熙凤聪明误此生.md",
    "第八十九回 有情人欣遇赏心事 不良妾专煞良辰景.md",
    "第九十回 林黛玉嬉春待好音 贾元春托梦警天伦.md",
    "第九十一回 锦衣卫查抄荣宁府 御林军戒严大观园.md",
    "第九十二回 家宅乱恶子通强梁 世道艰道人连流寇.md",
    "第九十三回 山雨近阊阖笼霭晦 风云喧末世漫尘烟.md",
    "第九十四回 骨肉泯良女落风尘 贵贱失恶奴劫浮财.md",
    "第九十五回 水月庵龄官挞贾蔷 嶽神庙茜雪慰宝玉.md",
    "第九十六回 贾宝玉参无知无识 花袭人信有始有终.md",
    "第九十七回 鸳鸯女谮语泄天机 绛珠仙泪尽抛全生.md",
    "第九十八回 系新绦嗟慰失意人 拾旧帕悲悼寂寞骨.md",
    "第九十九回 林黛玉还魂证前缘 贾宝玉展裘触旧情.md",
    "第一百回 邢岫烟魂断大庾岭 赵姨娘命丧平安州.md",
    "第一百一回 呆霸王惹祸牵旧案 悍妒妇作歹设新谋.md",
    "第一百二回 冷惜春甘伴青灯佛 洁妙玉泥陷瓜洲渡.md",
    "第一百三回 刘姥姥三进荣国府 贾巧姐二哭大观园.md",
    "第一百四回 毒中毒薛姨妈添病 计上计夏金桂焚身.md",
    "第一百五回 薛宝钗借词含讽谏 王熙凤知命强英雄.md",
    "第一百六回 孤倔王孙悬崖撒手 凄惶红袖秋千传情.md",
    "第一百七回 史湘云诉前尘旧梦 贾宝玉淡后事今生.md",
    "第一百八回 情不情僧遭逢穷途 幻中幻境展演情榜.md",
    "癸酉本石头记前八十回批语摘录.md",
]
output_file = 'index.md'


def get_content(fn: str) -> str:
    fn = f"docs/{fn}"
    stem = Path(fn).stem
    j = abs(hash(fn))
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
        if stem[:5] == content[:5]:  # 内容包含标题
            content = f"# {content}"
        else:  # 内容未包含标题
            content = f"# {stem}\n\n{content}"
        for i in range(1, 5):
          content = content.replace(f"[^{i}]", f"[^{j}.{i}]")
        return f"""\clearpage

{content}
"""

def merge():
    """
    生成目录并合并内容
    :return:
    """
    content: list[str] = []
    with open("metadata.yaml", 'r', encoding='utf-8') as f:
        content.append(f"---\n{f.read()}\n---")
    for filename in files:
        content.append(get_content(filename))
    return '\n\n'.join(content)

# 执行合并
if __name__ == '__main__':
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(merge())
    print(f"✅ 已成功合并为 {output_file}")
