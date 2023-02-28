from cols import COLS
import utility as util
import miscellaneous as misc
import random

def row(data, t):
    if data.cols:
        data.rows.append(t)
        for cols in [data.cols.x, data.cols.y]:
            for col in cols:
                add(col.col, t[col.col.at])
    else:
        data.cols = COLS(t)
    return data


def add(col, x, n = 1):
    if x != "?":
        col.n += n # Source of variable 'n'
        if hasattr(col, "isSym") and col.isSym:
            col.has[x] = n + (col.has.get(x, 0))
            if col.has[x] > col.most:
                col.most = col.has[x]
                col.mode = x
        else:
            x = float(x)
            col.lo = min(x, col.lo)
            col.hi = max(x, col.hi)
            all = len(col.has)
            if all < util.args.Max:
                pos = all + 1
            elif random.random() < util.args.Max / col.n:
                pos = util.rint(1, all)
            else:
                pos = None
            if pos:
                if isinstance(col.has, dict):
                    col.has[pos] = x
                else:
                    col.has.append(x)
                col.ok = False

def adds(col, t):
    for value in t or []:
        add(col, value)
    return col

def extend(range, n, s):
    range.lo = min(n, range.lo)
    range.hi = max(n, range.hi)
    add(range.y, s)