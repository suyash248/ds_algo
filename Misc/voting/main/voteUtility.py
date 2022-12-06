from Misc.voting.main.candidate import Candidate
from typing import Dict, List
from collections import defaultdict

class VoteUtility(object):
    def __init__(self):
        self.MAX_VOTES = 3
        self.candidates: Dict[str, Candidate] = dict()
        self.candidatesScores: Dict[str, int] = defaultdict(int)

    # [c1, c2, c3] -> len(candNames) - i
    def castVote(self, candidateNames: List[str]):
        voteCount = len(candidateNames)
        if voteCount == 0 or voteCount > self.MAX_VOTES:
            print("Invalid vote")
            return

        for i, candidateName in enumerate(candidateNames):
            if candidateName is None:
                print("Invalid name")
                continue
            candidateName = candidateName.lower()
            if candidateName not in self.candidates:
                self.candidates[candidateName] = Candidate(candidateName)

            currScore = voteCount - i
            self.candidatesScores[candidateName] = self.candidatesScores[candidateName] + currScore

    def leaderboard(self) -> List[str]:
        print(self.candidatesScores)  # TODO: Suyash - For testing, remove it later
        return list(sorted(self.candidatesScores.keys(), key=lambda cName: self.candidatesScores[cName], reverse=True))


