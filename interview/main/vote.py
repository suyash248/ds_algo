from typing import List

from interview.main.candidate import Candidate


class Vote(object):
    def __init__(self, candidates: List[str]):
        self.candidates = candidates
