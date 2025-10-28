from collections import defaultdict


class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        votes = defaultdict(int)
        leadingPerson = -1
        leaderVotes = 0
        n = len(persons)
        self.uniqueTime = []
        self.leaderAtTime = []
        i = 0
        while i < n:
            votes[persons[i]] += 1
            if votes[persons[i]] >= leaderVotes:
                leaderVotes = votes[persons[i]]
                leadingPerson = persons[i]
            i += 1
            while i < n and times[i] == times[i-1]:
                votes[persons[i]] += 1
                if votes[persons[i]] >= leaderVotes:
                    leaderVotes = votes[persons[i]]
                    leadingPerson = persons[i]
                i += 1
            self.uniqueTime.append(times[i-1])
            self.leaderAtTime.append(leadingPerson)
        self.n = len(self.uniqueTime)
        return

    def q(self, t: int) -> int:
        if t >= self.uniqueTime[-1]:
            return self.leaderAtTime[-1]
        l, r = 0, self.n-1
        while l < r:
            mid = l+((r-l)//2)
            if self.uniqueTime[mid] <= t:  # works
                l = mid+1
            else:
                r = mid
        return self.leaderAtTime[l-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)


obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
