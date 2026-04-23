def compute_failure_function(keyword):
    n = len(keyword)
    if n == 0:
        return []
    f = [0] * n
    t = 0
    for s in range(1, n):
        while t > 0 and keyword[s] != keyword[t]:
            t = f[t - 1]
        if keyword[s] == keyword[t]:
            t = t + 1
            f[s] = t
        else:
            f[s] = 0
    return f

def kmp_search(text, keyword):
    m = len(text)
    n = len(keyword)
    
    if n == 0:
        return "yes"
    if m == 0:
        return "no"

    f = compute_failure_function(keyword)
    s = 0

    for i in range(m):
        while s > 0 and text[i] != keyword[s]:
            s = f[s - 1]
            
        if text[i] == keyword[s]:
            s = s + 1
            
        if s == n:
            return "yes"

    return "no"

if __name__ == '__main__':
    keyword = "ababaa"
    
    texts_to_test = [
        "abababaab",
        "abababbaa"
    ]
    
    for text in texts_to_test:
        result = kmp_search(text, keyword)
        print(f"Text: {text} | Keyword: {keyword} -> Result: {result}")