import textwrap

def wrap(string, max_width):
    ans = textwrap.wrap(string, max_width)
    return textwrap.indent('\n'.join(ans), '')

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)   