class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        gas_station=0
        start_station=0
        for i in range(len(gas)):
            gas_station+=gas[i]
            gas_station-=cost[i]
            if gas_station<0:
                gas_station=0
                start_station=i+1
        return start_station