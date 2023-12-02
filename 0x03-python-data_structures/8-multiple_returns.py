#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing the length of the sentence and the first character.
    """
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])

# Below is for your local testing and should not be pushed to your repo
# if __name__ == "__main__":
#     sentence = "At school, I learnt C!"
#     length, first = multiple_returns(sentence)
#     print("Length: {:d} - First character: {}".format(length, first))
