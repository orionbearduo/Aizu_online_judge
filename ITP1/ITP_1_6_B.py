"""
Finding Missing Cards
Taro is going to play a card game. However, now he has only n cards,
even though there should be 52 cards (he has no Jokers).

The 52 cards include 13 ranks of each of the four suits: spade, heart, club and diamond.

Input
In the first line, the number of cards n (n ≤ 52) is given.

In the following n lines, data of the n cards are given. Each card is given by a pair of a character
and an integer which represent its suit and rank respectively. A suit is represented by 'S', 'H', 'C' and 'D' for spades,
hearts, clubs and diamonds respectively. A rank is represented by an integer from 1 to 13.

Output
Print the missing cards. The same as the input format,
each card should be printed with a character and an integer separated by a space character in a line.
Arrange the missing cards in the following priorities:

Print cards of spades, hearts, clubs and diamonds in this order.
If the suits are equal, print cards with lower ranks first.
"""
import sys


def make_all_cards():
    mark = ['S', 'H', 'C', 'D']
    cards = []

    for i in mark:
        for n in range(1, 14):
            cards.append(i + ' ' + str(n))

    return cards


if __name__ == '__main__':
    all_cards = make_all_cards()
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        card = sys.stdin.readline().strip()
        all_cards.remove(card)

    for i in all_cards:
        print(i)