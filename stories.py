"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, words, text):
        """Create story with words and template text."""
        self.code= code
        self.prompts = words #each word passed in (eg "noun", "verb", "place") is going to be in a list of prompts so story.prompts =['noun', 'verb', 'place']
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""
        
        
        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "1", 
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""

)

story2 = Story(
    "2",
    ["place", "noun", "verb", "adjective", "plural_noun"],
""" Yesterday we went to {place} and saw the smallest {adjective} {noun}. It was {verb} {plural_noun}!
""") 

story3 = Story(
    "3",
    ["place", "noun", "verb", "adjective", "plural_noun"],
""" The {adjective} {noun} lives in the south of {place}, in her free she she {verb} {plural_noun}.
""")


stories = {s.code :s for s in [story1, story2, story3]}