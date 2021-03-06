import json

from nfa import Nfa
from dfa import Dfa

if __name__ == "__main__":
    with open("json/dfa.json", "r") as f:
        data = json.load(f)

        con = Dfa(data)
        c = con.minimize()
        print(c.minimize())
        print(c.read("aab"))
        print(con.read("aab"))
    with open("json/nfa.json", "r") as f:
        data = json.load(f)
        con = Nfa(data)
        h = con.determine()
        print(h)
        print(con.read("ab"))
        a = h.dot_dictionary("hola")
        print(a)
