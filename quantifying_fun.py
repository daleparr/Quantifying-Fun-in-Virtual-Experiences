# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:31 2024

@author: mrdpa
"""

def calculate_fun_score(T_avg, R, I, S, P, E, weights):
    """
    Calculate Fun Score using defined metrics and weights.

    Parameters:
        T_avg (float): Average playtime (hours).
        R (float): Retention rate (%).
        I (float): Impressions and reach.
        S (float): Social media engagement.
        P (float): Player feedback score.
        E (float): Event participation rate.
        weights (dict): Dictionary of weights for each metric.

    Returns:
        float: Calculated Fun Score.
    """
    fun_score = (
        weights['w1'] * T_avg +
        weights['w2'] * R +
        weights['w3'] * I +
        weights['w4'] * S +
        weights['w5'] * P +
        weights['w6'] * E
    )
    return fun_score

# Example usage
weights = {'w1': 0.2, 'w2': 0.2, 'w3': 0.15, 'w4': 0.15, 'w5': 0.2, 'w6': 0.1}
fun_score = calculate_fun_score(T_avg=2.5, R=85, I=5000, S=200, P=4.5, E=75, weights=weights)
print(f"Fun Score: {fun_score}")
