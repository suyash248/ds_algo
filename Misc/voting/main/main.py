"""
Problem Description:

We are going to implement a function that determines the winner of a round of Shipit. Our function is going to look something like this:


/**
 * For a list of votes, return an ordered set of candidate in descending order of their votes.
 */
List<String> findWinner(List<Vote> votes)
We pass in a list of votes and we are returned a list of names in the descending order of the score that each candidate received.

Assume that we extract the candidates' names from the votes as we process them.

Assumption: A voter is allowed to vote for up to Max three different candidates (this should be configurable). The order of the votes is important. The first vote that a voter places is worth three points. The second vote is worth two points. The third vote is worth one point.

Check for all the boundary conditions before implementing the problem

Sample Input:


leaderBoard = {
    "Mykola": 3
    Michale: 2,
    Marcin: 1
}

O(n) + Klog(n)

votes = [
        Vote(["Mykola", "Michale", "Marcin"]),
        Vote(["Marcin", "Michale", "Mykola"]),
        Vote(["Michale", "Mykola", "Marcin"]),
        Vote(["Michale", "Marcin", "Mykola"]),
        Vote(["Mykola", "Michale", "Marcin"]),
        Vote(["Marcin", "Michale", "Mykola"]),
        Vote(["Michale", "Mykola", "Marcin"]),
        Vote(["Michale", "Marcin", "Mykola"]),
        Vote(["Mykola", "Michale", "Marcin"]),
        Vote(["Marcin", "Michale", "Mykola"]),
        Vote(["Michale", "Mykola", "Marcin"]),
        Vote(["Michale", "Marcin", "Mykola"]),
        Vote(["Mykola", "Marcin", "Michale"]),
        Vote(["Mykola", "Marcin"]),
        Vote(["Mykola"]),
    ]
"""
from Misc.voting.main.vote import Vote
from Misc.voting.main.voteUtility import VoteUtility

if __name__ == '__main__':
    votes = [
        Vote(["Mykola", "Michale", "Marcin"]),
        Vote(["Mykola", "Mykola", "Mykola"]),
        Vote(["Mykola", "Michale", "Marcin", "Raj"]),
        Vote(["Michale", "Marcin", "Mykola"]),
        Vote(["Mykola", "Michale", "Marcin"]),
        # Vote(["Marcin", "Michale", "Mykola"]),
        # Vote(["Michale", "Mykola", "Marcin"]),
        # Vote(["Michale", "Marcin", "Mykola"]),
        # Vote(["Mykola", "Michale", "Marcin"]),
        # Vote(["Marcin", "Michale", "Mykola"]),
        # Vote(["Michale", "Mykola", "Marcin"]),
        # Vote(["Michale", "Marcin", "Mykola"]),
        # Vote(["Mykola", "Marcin", "Michale"]),
        # Vote(["Mykola", "Marcin"]),
        # Vote(["Mykola"]),
    ]
    voteUtility: VoteUtility = VoteUtility()
    for vote in votes:
        voteUtility.castVote(vote.candidates)

    winners = voteUtility.leaderboard()
    print(winners)
