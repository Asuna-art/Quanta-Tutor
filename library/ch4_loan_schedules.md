# 第4章 贷款偿还表

Chapter 4

Loan Repayment Schedules

4.1      Overview
In this chapter we consider an important commercial application of compound interest
and equations of value, namely loans. In particular, we discuss how to calculate
regular repayment amounts and methods for calculating the loan outstanding at any
time within the term of the loan.

   • The calculation of loan repayment amounts and schedules is an important ap-
      plication of equations of value.

   • The level loan repayment can be calculated with knowledge of the interest rate,
      term, and capital borrowed by solving the equation of value for the entire loan.

   • Each repayment amount covers the interest owed on the capital outstanding in
      the prior period and a contribution towards the capital repayment.

   • Under the retrospective method, the loan outstanding is calculated from the
      accumulated value of all prior repayments and the original capital receipt.

   • Under the prospective method, the loan outstanding is calculated from the
      present value of all future repayments under the original terms of the loan.


4.2      The general loan schedule
A very common transaction involving compound interest is a loan that is repaid by
regular instalments, at a fixed rate of interest, for a predetermined term.
   Consider the following example.
   Assume a bank lends an individual £1, 000 for three years, in return for three
payments of X, say, one at the end of each year. The bank will charge an effective

4.2 The general loan schedule                                                          65


rate of interest of 7% per annum. The equation of value for the transaction gives:

                              1000 = Xa3 ⇒ X = 381.05

So, the borrower pays £381.05 at times t = 1, 2 and 3 in return for the loan of £1, 000
at time 0 . These three payments cover both the interest due and the £1, 000 capital.
It is helpful to see how this works in detail:
   At time 1 the interest due on the loan of £1000 is £70. The total payment made
is £381.05. This leaves £311.05 that is available to repay some of the capital. The
capital outstanding after this is then £(1000 − 311.05) = £688.95.
   At time 2 the interest due is now only 7% of £688.95 = £48.22, as the borrower
does not pay interest on the capital that is already repaid, only on the amount out-
standing. This leaves £(381.05 − 48.22) = £332.83 available to repay capital. The
capital outstanding after this is then £(688.95 − 332.83) = £356.12.
   Finally, at time 3 the interest due is 7% of £356.12 = £24.93, leaving £381.05 −
24.93 = £356.12 available to pay the outstanding sum of £356.12, and the capital is
precisely repaid.
   One important point is that each repayment must pay first for interest due on the
outstanding capital. The balance is then used to repay some of the capital outstand-
ing. Each payment, therefore, comprises both interest and capital repayment. It may
be necessary to identify the separate elements of the payments - for example, if the
tax treatment of interest and capital differs. Notice also that, where repayments are
level, the interest component of the repayment instalments will decrease as capital is
repaid, with the consequence that the capital payment will increase.
Calculating the capital outstanding
   Let Lt be the amount of the loan outstanding at time t = 0, 1, . . . , n, immediately
after the repayment at t. The repayments are assumed to be in regular instalments, of
amount Xt at time t, t = 1, 2, 3, . . . , n. Note that we are not assuming all instalments
are the same amount. Let i be the effective rate of interest, per time unit, charged on
the loan. Let ft be the capital repaid at t, and let bt be the interest paid at t, so that
Xt = ft + bt . The equation of value for the loan at time 0 is:

                            L 0 = X 1 v + X2 v 2 + . . . + Xn v n

We can find the loan outstanding at t prospectively or retrospectively.

Prospective loan calculation
   Consider the loan transactions at time n, which is the end of the contract term.
After the final instalment of capital and interest the loan is exactly repaid. So the
final instalment, Xn must exactly cover the capital that remains outstanding after the
4.2 The general loan schedule                                                           66


instalment paid at n − 1, together with the interest due on that capital. That is:

                                  bn = iLn−1 ; fn = Ln−1

so that
                   Xn = iLn−1 + Ln−1 = (1 + i)Ln−1 ⇒ Ln−1 = Xn v

Similarly, at any time t + 1, t ≤ n − 2 we know that the capital repaid is Lt − Lt+1 , so
that the instalment Xt+1 is:

                   Xt+1 = iLt + (Lt − Lt+1 ) ⇒ Lt = (Lt+1 + Xt+1 ) v

Similarly, Lt+1 = Lt+2 + Xt+2 v, and working forward, successively substituting for
Lt+r until we get to Ln = 0, we get:

             Lt = (Lt+1 + Xt+1 ) v
                = ((Lt+2 + Xt+2 ) v + Xt+1 ) v = Xt+1 v + Xt+2 v 2 + Lt+2 v 2
                = Xt+1 v + Xt+2 v 2 + Xt+3 v 3 + Lt+3 v 3
                   .
                = ..
                = Xt+1 v + Xt+2 v 2 + Xt+3 v 3 + . . . + Xn v n−t

This gives the prospective method for calculating the loan outstanding. What this
equation tells us is that, for calculating the loan outstanding immediately after the
repayment at t, say, we have:
   Prospective Method: The loan outstanding at time t is the present (or
discounted) value at time t of the future repayment instalments.
   Note the condition for this method – the present value must be calculated at a
repayment date.

Retrospective loan calculation
   At t = 1 the interest due is b1 = iL0 , so the capital repaid is f1 = X1 − iL0 , leaving
a loan outstanding of:

                          L1 = L0 − (X1 − iL0 ) = L0 (1 + i) − X1

   In general, at time t ≥ 1 the interest due is bt = iLt−1 , leaving capital repaid at t
of Xt − iLt−1 , giving:
                                  Lt = Lt−1 (1 + i) − Xt




4.2 The general loan schedule                                                             67


Similarly, Lt−1 = Lt−2 (1 + i) − Xt−1 and, working back from t to 0 we have:

        Lt = Lt−1 (1 + i) − Xt
            = (Lt−2 (1 + i) − Xt−1 ) (1 + i) − Xt = Lt−2 (1 + i)2 − Xt−1 (1 + i) − Xt
            = L0 (1 + i)t − X1 (1 + i)t−1 + X2 (1 + i)t−2 + . . . + Xt−1 (1 + i) + Xt
                                                                                      


This gives the retrospective method of calculating the outstanding loan. This may be
described in words as:
    Retrospective Method: The loan outstanding at time t is the accumu-
lated value at time t of the original loan less the accumulated value at time
t of the repayments to date.
    Both approaches are very useful in calculating the capital outstanding at any time.
Neither result depends on the interest rate being constant. It may be useful to work
through the equations assuming the interest charged on the loan in year r − 1 to r is
ir , say.

Calculating the interest and capital element of the repayments
    Given the outstanding capital at any time we can calculate the interest and capital
element of any instalment. For example, consider the instalment Xt at time t. We
can calculate the interest element contained in this payment by calculating the loan
outstanding immediately after the previous instalment, at t − 1, Lt−1 . The interest
due on capital of Lt−1 for one unit of time at effective rate i per time unit is iLt−1 ,
and this is the interest paid at t. The capital repaid may be found using Xt − iLt−1 ,
or by Lt−1 − Lt .
    Similarly, it is a simple matter to calculate the interest paid and capital repaid
over several instalments. For example, consider the five instalments from t + 1 to
t + 5, inclusive. Then the loan outstanding immediately before the first instalment
is Lt . The loan outstanding after the fifth instalment is Lt+5 . The total capital
repaid in this period is therefore Lt − Lt+5 . The total capital and interest paid is
Xt+1 + Xt+2 + . . . + Xt+5 . Hence, the total interest paid is:

                    t+5
                    X
                            bk = (Xt+1 + Xt+2 + . . . + Xt+5 ) − (Lt − Lt+5 ) .
                    k=t+1



The loan schedule
    The loan payments can be expressed in the form of a table, or ’schedule’, as follows.
    With spreadsheet software it is a simple matter to construct the entire schedule
for any loan.


4.3 The loan schedule for a level annuity                                                          68

                   Loan                       Interest     Capital              Loan
      Year                      Instalment
                outstanding                     due         repaid          outstanding
    r →r+1                        at r + 1
                    at r                      at r + 1     at r + 1           at r + 1
      0→1            L0            X1           iL0        X1 − iL0     L1 = L0 − (X1 − iL0 )
       ..             ..            ..            ..           ..                 ..
        .              .             .             .            .                  .
    t→t+1           Lt             Xt+1         iLt       Xt+1 − iLt   Lt+1 = Lt − (Xt+1 − iLt )
      ..             ..             ..           ..            ..                 ..
       .              .              .            .             .                  .
    n−1→n          Ln−1            Xn          iLn−1      Xn − iLn−1              0

                                 Table 4.1: Loan schedule

4.3      The loan schedule for a level annuity
Consider the particular case where, on the basis of an interest rate of i per unit time,
a loan of amount an is made at time t = 0 in return for n repayments, each of amount
1 , to be made at times 1, 2, . . . , n. The lender may construct a schedule showing the
division of each payment into capital and interest.
   Immediately after the t th repayment has been made, there remain (n − t) out-
standing payments, and the prospective method shows that the outstanding loan is
simply an−t . In the notation of Section 5.1,

                                          Lt = an−t                                          (4.1)

then the amount of loan repaid at time t is

                              ft = Lt−1 − Lt = an−t+1 − an−t
                                                                                             (4.2)
                                              = v n−t+1

The lender’s schedule may be presented in the form of Table 4.2. More generally,
if an amount L is lent in return for n repayments, each of amount X = L/an , the
monetary amounts in the lender’s schedule are simply those in the schedule of Table 4.2
multiplied by the constant factor X.


4.4      The loan schedule for a pthly annuity
No new principles are involved in the loan schedule for a pthly annuity, since this is
simply a particular example of the general schedule discussed in the preceding sections.
For a loan repayable by a level annuity payable p thly in arrears over n time units and
based on an interest rate i per unit time, the schedule is best derived by working with
an interest rate of i(p) /p per time interval of length 1/p. Therefore, the interest due
at time r/p (r = 1, 2, . . . , np) is i(p) /p times the loan outstanding at time (r − 1)/p
(immediately after the repayment then due has been received).
                                               (p)
   For example, in relation to a loan of an (at rate i ), it is simple to show that
4.4 The loan schedule for a pthly annuity                                             69


the capital repaid in the r th annuity payment (r = 1, 2, . . . , np) is (1/p)v n−(r−1)/p
and that the loan outstanding immediately after the rth payment has been received
   (p)
is an−r/p (at rate i). This is simply the value of the outstanding payments from the
prospective method.



