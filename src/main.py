from parglare import Parser, Grammar
import os
this_folder = os.path.dirname(__file__)
grammar_file = os.path.join(this_folder, 'grammar.pg')

grammar = Grammar.from_file(grammar_file)

parser = Parser(grammar, debug=True)

result = parser.parse({
  "source": "1JDGddeS9eHPwtm69w7Zhw2vQ5aUAbxDes",
  "source_name": "Elicia",
  "destination": "148nDEB2KV3CqYKqBB89HoxUkuvhjLMDim",
  "amount": "$242.96"
})

print(result)

  # "tx_type": "outbound",
  # "tx_class_type": "gift",
  # "date": "2021-03-01T10:09:07Z",
  # "note": "testing parser",
  # "user_id": 1,
  # "currency": "Dollar",
  # "coin_type": "ICX",
  # "fees": 0