# Nedbank Loan Calculator
print("---Welcome To Nedbank Loan Console Calculator---")

loan_amount = int(input("Please enter loan amount: "))
interest_rate = float(input("Please enter your interest rate without a percentage sign: "))
_number_of_months = 12  # how long it would take you to repay the loan.

total_repayment = loan_amount + (loan_amount * interest_rate)
monthly_installment = total_repayment / _number_of_months

print('Total Repayment: ', total_repayment)
print("Monthly installment: ", monthly_installment)
print("Please go to the nearest nedbank branch with you bank statement, ID and proof  of residence.")
