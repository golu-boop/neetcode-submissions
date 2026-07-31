class Solution:
    def countSeniors(self, details: List[str]) -> int:
        psg_count = 0

        for s in details:
            first = s[-3]
            second = s[-4]
            temp = second + first
            if int(temp) > 60:
                psg_count += 1

        return psg_count