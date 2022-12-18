"""CSC110Y1F: Welcome File

Welcome to CSC110! This is a sample Python file that you should be able to
run after you have completed the steps in the Software Setup guide on our
First-Year Computer Science Summer Prep modules (https://q.utoronto.ca/courses/160038/).

To run this file in PyCharm, go to Run -> Run... and select 'welcome' in the popup menu.
After you've run this program for the first time, you'll be able to re-run it
easily by pressing the green ▶ arrow in the toolbar on the top-right of your window.
"""
# TODO: fill in the string with your name, and then delete this TODO comment.
MY_NAME = 'MY_NAME_HERE'


def greet(name: str) -> str:
    """Return a welcome message for the given person.

    >>> greet('David')
    'Hello, David! Welcome to CSC110. Hope you have a great time this term. :)'
    """
    return (f'Hello, {name}! Welcome to CSC110. ' +
            'Hope you have a great time this term. :)')


if __name__ == '__main__':
    print(greet(MY_NAME))
