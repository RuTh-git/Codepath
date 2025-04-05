def reverse_orders(orders):
    word = orders.split(' ')
    return reverse_deli(word)
    
def reverse_deli(word):
    if not word:
        return ""
    
    if word:
        last_word = word.pop()
        return last_word + " " + reverse_deli(word)
    
print(reverse_orders("Bagel Sandwich Coffee"))