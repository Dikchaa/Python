import textwrap

def wrap(string, max_width):
    # Text Wrap in Python - HackerRank Solution START
    return textwrap.fill(string,max_width)
    # Text Wrap in Python - HackerRank Solution END

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
