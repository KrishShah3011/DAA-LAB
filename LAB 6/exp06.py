# Interface for LCS Calculation Algorithm
class LCSAlgorithm:
    def calculate(self, sequence1, sequence2):
        pass


# Dynamic Programming based LCS Calculation
class DPLCS(LCSAlgorithm):
    def calculate(self, sequence1, sequence2):
        """Compute the Longest Common Subsequence (LCS) between two sequences using Dynamic Programming."""
        m, n = len(sequence1), len(sequence2)
        # Create a DP table to store lengths of LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the dp table in bottom-up manner
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if sequence1[i - 1] == sequence2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Backtrack to find the actual LCS
        lcs_sequence = []
        i, j = m, n
        while i > 0 and j > 0:
            if sequence1[i - 1] == sequence2[j - 1]:
                lcs_sequence.append(sequence1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        # The LCS is built backwards, so reverse it before returning
        return ''.join(reversed(lcs_sequence))


# Validator for Grade Sequences
class GradeSequenceValidator:
    @staticmethod
    def validate(grade_sequences):
        """Ensure the grade sequences are valid. Return 'Error' if any sequence contains digits."""
        if not grade_sequences:
            return "No common subsequence found"
        for grades in grade_sequences:
            if not grades:
                return "No characters in the string"
            if any(char.isdigit() for char in grades):  # Check if any character is a digit
                return "Grade sequences should not contain numbers"
        return None  # No issues found


# LCS Calculator that uses a specific LCS Algorithm
class LCSCalculator:
    def __init__(self, algorithm: LCSAlgorithm):
        self.algorithm = algorithm

    def find_lcs(self, grade_sequences):
        """Compute the longest common subsequence (LCS) among a list of grade sequences."""
        validation_error = GradeSequenceValidator.validate(grade_sequences)
        if validation_error:
            return validation_error
        
        # Start with the grades of the first student
        common_sequence = grade_sequences[0]
        
        # Iteratively find LCS with each subsequent student's grades
        for grades in grade_sequences[1:]:
            common_sequence = self.algorithm.calculate(common_sequence, grades)
            if not common_sequence:  # Exit early if there's no common subsequence left
                return "No common subsequence found"
        
        return common_sequence if common_sequence else "No common subsequence found"


# Example Usage
students_grades = [
    "",   # Valid grade sequence
    "1235",    # Valid grade sequence
]

# Instantiate the LCSCalculator with Dynamic Programming approach
lcs_calculator = LCSCalculator(DPLCS())

# Find the longest common subsequence of grades among students
print("Generated Grades for Each Student:")
for i, grades in enumerate(students_grades, 1):
    print(f"Student {i}: {grades}")

result = lcs_calculator.find_lcs(students_grades)
print("Longest Common Sequence of Grades:", result)
