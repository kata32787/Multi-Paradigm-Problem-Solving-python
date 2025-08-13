class StatisticsCalculator:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        frequency = {}
        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1

        max_freq = max(frequency.values())
        modes = [k for k, v in frequency.items() if v == max_freq]

        return modes


if __name__ == "__main__":
    numbers = [12, 32, 12, 12, 84, 14, 124, 55]

    stats_calc = StatisticsCalculator(numbers)

    print(f"Numbers: {numbers}")
    print(f"Mean: {stats_calc.mean():.2f}")
    print(f"Median: {stats_calc.median():.2f}")
    print(f"Mode: {', '.join(map(str, stats_calc.mode()))}")
