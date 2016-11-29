from sympy import simplify, evalf
import requests
from bs4 import BeautifulSoup

def calculate(str_expr, return_float=False):
    """
    Evaluate a string STR_EXPR.
    if STR_EXPR is a mathematical expression, simplify it with sympy.simplify
    Otherwise, search WolframAlpha for answers
    """
    try:
        result = simplify(str_expr)
        return result
    except Exception:
        # use Wolfram Alpha
        
        payload = {'input': str_expr, 'appid': 'UAGAWR-3X6Y8W777Q'}
        r = requests.get('http://api.wolframalpha.com/v2/query', params=payload)

        soup = BeautifulSoup(r.content,"lxml")
        if soup.queryresult['success'] == 'true':
            pods = soup.queryresult.findAll('pod')
            assert len(pods) >= 2
            num_string =  pods[1].plaintext.string.split()[0]
            if return_float:
                return float(simplify(num_string.replace(u"\u00D7", '*')))
            else:
                return num_string
        else:
            return "I don't know the answer"

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='read command line arguments')
    parser.add_argument('-s', action='store', dest='expr',
                        help='provide a string expression to evaluate')

    results = parser.parse_args()
    expr = results.expr

    print(calculate(expr))


