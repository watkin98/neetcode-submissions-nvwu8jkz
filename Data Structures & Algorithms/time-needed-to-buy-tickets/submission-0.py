class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        stopwatch = 0
        person_k = k

        while tickets != []:
            tickets[0] -= 1
            stopwatch += 1
            if person_k == 0 and tickets[person_k] == 0:
                print(1)
                return stopwatch
            elif person_k == 0 and tickets[person_k] > 0:
                person_k_tickets = tickets.pop(person_k)
                tickets.append(person_k_tickets)
                person_k = len(tickets) - 1
            else:
                person = tickets.pop(0)
                if person != 0:
                    tickets.append(person)
                person_k -= 1
        print(2)
        return stopwatch
            