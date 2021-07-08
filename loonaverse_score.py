import pandas as pd


def calculate_final_score(distance_score: int, alien_score: int):
    final_score = distance_score + alien_score * 500
    return final_score


def record_score(name: str, score_value: int):
    """Records the final score of the player into a running list.

    :param name: player's name
    :param score_value: final score of player at Game Over
    :return:
    """
    scores_df = pd.read_csv('assets/recorded_scores.csv')
    new_score_df = pd.DataFrame({'name': [name], 'score': [score_value]})
    scores_df = scores_df.append(new_score_df, ignore_index=True)
    sorted_df = scores_df.sort_values(by='score', ascending=False)
    sorted_df.to_csv('assets/recorded_scores.csv', index=False)


def top_3_scores():
    """ Retrieves the top 3 scores with names in the running list.
    Pandas to_dict() format: ‘dict’ (default) : dict like {column -> {index -> value}}

    :return: top 3 scores with names in a dictionary
    """
    scores_df = pd.read_csv('assets/recorded_scores.csv')
    top_3_df = scores_df.head(3)
    return top_3_df.to_dict()