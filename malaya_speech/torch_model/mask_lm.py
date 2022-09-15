import torch
import math
import logging

logger = logging.getLogger(__name__)

LOG_BASE_CHANGE_FACTOR = 1.0 / math.log10(math.e)


class LM:
    def __init__(
        self,
        model,
        alpha: float = 0.05,
        beta: float = 0.5,
        order: int = 1,
        **kwargs,
    ):
        self.model = model
        self.alpha = alpha
        self.beta = beta
        self.order = order

    def cuda(self):
        return self.model.cuda()

    def score_partial_token(self, partial_token: str):
        return 0.0

    def get_start_state(self):
        return {
            'current_score': float('-inf'),
            'last_state': []
        }

    def score(self, prev_state, word: str, is_last_word: bool = False):
        new_state = prev_state['last_state'] + [word]
        current_score = self.model.score(' '.join(new_state))

        logger.debug(f'word: {word}, new_state: {new_state}, current_score: {current_score}')

        new_state = {
            'current_score': current_score,
            'last_state': new_state
        }

        return current_score, new_state
