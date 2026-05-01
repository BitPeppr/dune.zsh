with open("quotes.txt", "r") as f:
    quotes = [line for line in f.read().splitlines() if line.strip() != ""]

parsed_quotes = []

for i in range(0, len(quotes) - 1, 2):
    quote = quotes[i]
    author = quotes[i + 1]
    parsed_quote = quote + "\n" + author
    parsed_quote = parsed_quote.replace('"', '\\"')
    parsed_quotes.append(parsed_quote)

with open("parsed_quotes.txt", "w+") as f:
    for i in parsed_quotes:
        f.write('"' + i + '"\n')
