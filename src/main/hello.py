import requests
import prettytable as tb

def hello():
    response = requests.get('https://www.baidu.com')
    table=tb.PrettyTable()
    print(response)
    print("hello")


if __name__ == "__main__":
    hello()
