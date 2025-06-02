# Version 1
# Problem 1: Post Format Validator
'''You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.'''
def is_valid_post_format(posts):
  stack = []
  map = {')':'(', ']':'[', '}':'{'}
  
  for i in posts:
    if i in map.values():
      stack.append(i)
    elif i in map.keys():
      if not stack or stack.pop() != map[i]:
        return False 
  return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
'''Example Output:

True
True
False'''

# Problem 2: Reverse User Comments Queue
'''On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.
'''
def reverse_comments_queue(comments):
  pass


print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
'''Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']'''