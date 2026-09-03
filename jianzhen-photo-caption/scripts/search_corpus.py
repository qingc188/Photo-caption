# -*- coding: utf-8 -*-
"""
简媜文库检索脚本（供任何 AI Agent 调用）

用法：
    python search_corpus.py 关键词1 关键词2 ... [--top N] [--strict]

- 在 references/corpus/ 下按关键词检索简媜原文句子
- 默认输出匹配"任一关键词"的句子；--strict 改为匹配"全部关键词"
- --top N 控制返回上限（默认 40）
- 输出格式：句子 ——《书名》（篇名）| 来源文件
- 标题行、来源注释行自动忽略

示例：
    python search_corpus.py 树 午后 光影 --top 30
    python search_corpus.py 空椅 等待 --strict --top 20
"""
import os
import re
import sys
import glob

SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_DIR = os.path.join(SKILL_ROOT, 'references', 'corpus')


def is_noise(line):
    """跳过标题、来源注释、空行"""
    s = line.strip()
    if not s:
        return True
    if s.startswith('#'):
        return True
    if s.startswith('>'):
        return True
    if re.match(r'^[-=*_]{3,}$', s):
        return True
    return False


def load_lines():
    lines = []
    for f in glob.glob(os.path.join(CORPUS_DIR, '*.md')):
        name = os.path.basename(f)
        # 跳过书目汇总索引（非语料，内容与语料文件重复）
        if '书目汇总索引' in name:
            continue
        try:
            with open(f, encoding='utf-8') as fh:
                for raw in fh.read().splitlines():
                    s = raw.strip()
                    if not is_noise(s):
                        # 去掉行内可能残留的 [源：...] 噪声
                        s = re.sub(r'〔源：.*?〕', '', s).strip()
                        if s:
                            lines.append((s, name))
        except Exception:
            continue
    return lines


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = [a for a in sys.argv[1:] if a.startswith('--')]
    top = 40
    for i, a in enumerate(flags):
        if a == '--top' and i + 1 < len(flags) and flags[i + 1].isdigit():
            top = int(flags[i + 1])
        elif a.startswith('--top='):
            top = int(a.split('=', 1)[1])
    strict = '--strict' in flags

    if not args:
        print('用法: python search_corpus.py 关键词... [--top N] [--strict]')
        sys.exit(1)

    lines = load_lines()
    hits = []
    seen = set()
    for text, fname in lines:
        if strict:
            ok = all(k in text for k in args)
        else:
            ok = any(k in text for k in args)
        if ok and text not in seen:
            seen.add(text)
            hits.append((text, fname))

    # 精简：优先含出处标注的
    print(f'共命中 {len(hits)} 条（关键词: {"/".join(args)}）\n')
    for text, fname in hits[:top]:
        print(text)
        print(f'  └ {fname}\n')


if __name__ == '__main__':
    main()
