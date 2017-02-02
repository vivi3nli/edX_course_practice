#Problem 1

# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# Result Your Code Should Generate Below:
Remaining balance: 31.38

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

mIR = annualInterestRate / 12 #mIR = monthly interest rate
#mmp = monthlyPaymentRate * previousbalance #min monthly payment
m_balance = balance
for month in range(12):
    #Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    mmp = m_balance * monthlyPaymentRate
    #Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    mup = m_balance - mmp
    #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    m_balance = mup * (1 + mIR)
    
print("Remaining balance: " + str(round(m_balance, 2)))

#Problem 2
#mIR = monthly interest rate

#Test Case 1:
balance = 3329
annualInterestRate = 0.2

#Test Case 2:
balance = 4773
annualInterestRate = 0.2

#Test Case 3:
balance = 3329
annualInterestRate = 0.2

mIR = annualInterestRate / 12 
m_balance = balance
#monthly payment starts from 10
mp = 0

while m_balance > 0:
    m_balance = balance #initializing is essential
    mp += 10
    for month in range(12):
        #Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
        mup = m_balance - mp
        if mup * (1 + mIR ) - m_balance > 0:
            break
        #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
        m_balance = mup * (1 + mIR)
        #print(str(m_balance))    #this is for debugging

print("Lowest Payment: "+ str(mp))

#Problem 3
#Test Case 1:
balance = 320000
annualInterestRate = 0.2

#Test Case 2:
balance = 999999
annualInterestRate = 0.18
#mIR = monthly interest rate
mIR = annualInterestRate / 12 
#lower bone is 1/12 of the original credit
l_b = balance / 12
u_b = balance * ((1 + mIR) ** 12) / 12
m_balance = balance #this initialization is essential too
while abs(m_balance) > 0.01:
    m_balance = balance
    mp = (u_b + l_b) / 2
    for month in range(12):
        #Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
        mup = m_balance - mp
        if mup * (1 + mIR ) - m_balance > 0:
            break
        #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
        m_balance = mup * (1 + mIR)
    if m_balance > 0:
        l_b = mp
    else:
        u_b = mp

print("Lowest Payment: " + str(round(mp, 2)))





































