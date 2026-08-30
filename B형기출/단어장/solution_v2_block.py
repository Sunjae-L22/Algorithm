from bisect import bisect_left

BLOCK = 512                       # 블록 하나의 목표 크기 (2*BLOCK을 넘으면 쪼갠다)

class PAGE:
    __slots__ = ('no', 'word')
    def __init__(self, no, word):
        self.no = no
        self.word = word

def init() -> None:
    global blocks, heads, fen, nblk, best, cur_page
    blocks = [["a"]]              # 사전순 정렬된 단어를 블록으로 쪼개 담는다
    heads  = ["a"]                # 각 블록의 첫 단어 (블록을 이분탐색하기 위한 색인)
    nblk   = 1
    fen    = [0, 1]               # 펜윅: 블록별 단어 개수 -> 앞선 단어 수를 O(log)로
    best   = {"a": (-1, 1, "a")}  # 접두사 -> (-중요도, 등록순서, 단어)
    cur_page = 1                  # 1-based 페이지 번호

# ---- 펜윅 트리 (블록별 개수) ----
def _fen_add(i, v):
    while i <= nblk:
        fen[i] += v
        i += i & -i

def _fen_sum(i):                  # 1..i 블록의 단어 수 합
    s = 0
    while i > 0:
        s += fen[i]
        i -= i & -i
    return s

def _fen_kth(k):                  # k번째 단어가 든 블록과 블록 내 위치
    pos, rem, bit = 0, k, 1
    while bit * 2 <= nblk:
        bit *= 2
    while bit:
        if pos + bit <= nblk and fen[pos + bit] < rem:
            pos += bit
            rem -= fen[pos]
        bit //= 2
    return pos, rem - 1

def _rebuild():                   # 블록을 쪼갠 뒤 색인과 펜윅을 다시 만든다
    global heads, fen, nblk
    heads = [b[0] for b in blocks]
    nblk  = len(blocks)
    fen   = [0] * (nblk + 1)
    for i, b in enumerate(blocks):
        _fen_add(i + 1, len(b))

def _find_block(w):               # w가 들어갈(또는 있는) 블록 번호
    i = bisect_left(heads, w)
    return i - 1 if i else 0

def _page_of(w):
    bi = _find_block(w)
    return _fen_sum(bi) + bisect_left(blocks[bi], w) + 1

def _word_at(page):
    bi, off = _fen_kth(page)
    return blocks[bi][off]

# ---- API ----
def add(mWord: str, mImportance: int) -> PAGE:
    global cur_page
    bi  = _find_block(mWord)
    blk = blocks[bi]
    off = bisect_left(blk, mWord)
    blk.insert(off, mWord)                  # 블록 안에서만 밀린다 (최대 1024칸)
    _fen_add(bi + 1, 1)
    page = _fen_sum(bi) + off + 1
    if len(blk) > 2 * BLOCK:
        blocks[bi:bi + 1] = [blk[:BLOCK], blk[BLOCK:]]
        _rebuild()

    # 이 단어가 자기 접두사 6개의 대표를 갈아치우는지 확인
    # 튜플을 (-중요도, 등록순서)로 두면 "중요도 최대, 동점이면 먼저 등록" = 최솟값 하나로 끝난다
    cand = (-mImportance, _fen_sum(nblk), mWord)
    for i in range(1, len(mWord) + 1):
        p = mWord[:i]
        cur = best.get(p)
        if cur is None or cand < cur:
            best[p] = cand

    cur_page = page
    return PAGE(page, mWord)

def move(mDir: int) -> PAGE:
    global cur_page
    cur_page += mDir
    return PAGE(cur_page, _word_at(cur_page))

def go(mNo: int) -> PAGE:
    global cur_page
    cur_page = mNo
    return PAGE(mNo, _word_at(mNo))

def search(mStr: str) -> PAGE:
    global cur_page
    # 1) 완전 일치가 최우선
    i = bisect_left(heads, mStr)
    if i < nblk and heads[i] == mStr:       # 블록의 첫 단어와 일치하는 경우
        cur_page = _fen_sum(i) + 1
        return PAGE(cur_page, mStr)
    bi  = i - 1 if i else 0
    blk = blocks[bi]
    off = bisect_left(blk, mStr)
    if off < len(blk) and blk[off] == mStr:
        cur_page = _fen_sum(bi) + off + 1
        return PAGE(cur_page, mStr)
    # 2) 접두사 대표는 add에서 이미 갱신해 두었다
    cand = best.get(mStr)
    if cand is None:
        return PAGE(-1, _word_at(cur_page))
    w = cand[2]
    cur_page = _page_of(w)
    return PAGE(cur_page, w)
