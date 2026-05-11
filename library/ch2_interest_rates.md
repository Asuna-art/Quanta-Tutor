# 第2章 利率介绍

Chapter 2

Theory of interest rates

2.1      Overview
  • Interest is the reward paid by the borrower for the use of money, referred to as
      capital or principal, belonging to the lender.

  • Under the action of simple interest, interest is paid only on the principal amount
      and previously earned interest does not earn interest itself. A principal amount
      of C invested under simple interest at a rate of i per annum for n years will
      accumulate to
                                           C(1 + in)

  • Under the action of compound interest, interest is paid on previously earned
      interest. A principal amount of C invested under compound interest at a rate
      of i per annum for years will accumulate to

                                           C(1 + i)n


  • Compound interest is used in practice for all but very short-term investments.

  • The accumulation factor, A(t, T ), gives the value, at time T , of a unit investment
      made at time t < T . If the investment is subject to an effective rate of compound
      interest i, then
                                    A(t, T ) = (1 + i)T −t

  • The discount factor, v t , gives the present value at time zero of an investment
      that has unit value at time t > 0.

                            v t = (1 + i)−t = A(0, t)−1 = A(t, 0)

2.2 Introduction to interest rates                                                                       27


   • The principle of consistency states that A (t0 , tn ) = A (t0 , t1 ) A (t1 , t2 ) . . . A (tn−1 , tn )
        for all t0 < t1 < . . . < tn−1 < tn . It is a common assumption on consistent mar-
        kets.

   • The nominal rate of interest converted p thly, i(p) , is defined such that the
        effective rate of interest is i = i(p) /p per period of length 1/p.

   • The force of interest at time t can be defined by the expression δ(t) = limp→∞ i(p) (t),
        i.e., is the nominal rate converted momentarily.

   • The accumulation factor under the action of a force of interest between times t1
        and t2 is
                                                                  R t2
                                           A (t1 , t2 ) = e t1 δ(t)dt

   • The present value at t = 0 of a cash flow consisting of discrete payments Cti
        made at times ti and a continuous payment stream of rate ρ(t) is given by

                                       X                   Z ∞
                                           Cti v (ti ) +             v(t)ρ(t)dt


   • The value of a cash flow at times t1 and t2 are connected by
                    "                       #                 "                         #
                        value at time t1                             value at time t2
                                                [v (t1 )] =                                 [v (t2 )]
                        of cash flow                                 of cash flow


2.2        Introduction to interest rates
When you lend money, in a commercial context, you almost always want to get back
more money than the amount you lend. The difference between what you get and
what you lend is the interest. The interest rate is the interest as a fraction of the sum
lent.
   Why do interests exist? This is a vast question in economics, and there are multiple
answers. Here we just mention briefly some of them.

   • Lending is risky.
        So you would charge the borrower some interest to compensate you for the risk
        you take by lending your money to the borrower. This is called charging a risk
        premium. Usually, the higher the risk that you will not get all your money back,
        the higher the interest that you will charge. In particular, factors such as how
        credit-worthy the borrower is, what the borrower plans to do with the money,
        or the length of the loan, will affect the interest you ask.

2.2 Introduction to interest rates                                                   28


   • Opportunity cost.
      By choosing to lend now, it costs you the possibility to do other things with that
      money in the future. The interests are compensation for that loss of flexibility.

   • Inflation.
      The price of what you could buy today with your money generally increases
      with time. So if you get back at the end of the loan the same amount that you
      had initially lent, you have lost some buying power. Asking to be given back
      more money than the amount you lend protects you against losing some buying
      power due to inflation.

   • Preference for consuming now.
      People generally prefer having things now rather than in the future. Having
      food, new clothes, games, etc., today is felt as more valuable than having the
      same in the future. If your money was to be used to consume, by lending, you
      postpone your consumption and thus end up with something less valuable. The
      interests are a way to make up for that.

   • Everybody else charges interests.
      Interests are the cost of borrowing. Because everyone charges interest, there is
      a market price for borrowing. If you do not charge the same price, or about the
      same price, you lose out.

In this chapter, we will see how interest rates work, and how to convert ‘X Gils in the
future’ into ‘Y Gils today’.


2.2.1     Simple interest
Suppose that an investor opens a savings account, which pays simple interest at the
rate of 9% per annum, with a single deposit of £100. The account will be credited
with £9 of interest for each complete year the money remains on deposit. If the
account is closed after 1 year, the investor will receive £109; if the account is closed
after 2 years, he will receive £118, and so on. This may be summarized more generally
as follows.
   If an amount C is deposited in an account that pays simple interest at the rate
of i per annum and the account is closed after n years (there being no intervening
payments to or from the account), then the amount paid to the investor when the
account is closed will be
                                       C(1 + ni)                                   (2.1)



2.2 Introduction to interest rates                                                    29


This payment consists of a return of the initial deposit C, together with interest of
amount
                                          niC                                       (2.2)

In our discussion so far, we have implicitly assumed that, in each of these last two
expressions, n is an integer. However, the normal commercial practice in relation to
fractional periods of a year is to pay interest on a pro rata basis, so that Eqs (2.1)
and (2.2) may be considered as applying for all non-negative values of n.
   Note that if the annual rate of interest is 12%, then i = 0.12 per annum; if the
annual rate of interest is 9%, then i = 0.09 per annum; and so on.
   We have assumed that 6 months and 10 months are periods of 1/2 and 10/12 of
1 year, respectively. For accounts of duration less than 1 year, it is usual to allow for
the actual number of days an account is held, so, for example, two 6-month periods
are not necessarily regarded as being of equal length. In this case Eq (2.1) becomes
                                             
                                          mi
                                     C 1+

where m is the duration of the account, measured in days, and i is the annual rate of
interest.
   The essential feature of simple interest, as expressed algebraically by (2.1), is that
interest, once credited to an account, does not itself earn further interest. This leads
to inconsistencies that are avoided by the application of compound interest theory, as
discussed in later sections.
   As a result of these inconsistencies, simple interest has limited practical use, and
this book will, necessarily, focus on compound interest. However, an important com-
mercial application of simple interest is simple discount, which is commonly used for
short-term loan transactions, i.e., up to 1 year. Under simple discount, the amount
lent is determined by subtracting a discount from the amount due at the later date.
If a lender bases his short-term transactions on a simple rate of discount d, then, in
return for a repayment of X after a period t (typically t < 1 ), he will lend X(1 − td)
at the start of the period. In this situation, d is also known as a rate of commercial
discount.


2.2.2       Repeated investment, compounded interest rates
Suppose now that a certain type of savings account pays simple interest at the rate
of i per annum. Suppose further that this rate is guaranteed to apply throughout the
next 2 years and that accounts may be opened and closed at any time. Consider an
investor who opens an account at the present time (t = 0) with an initial deposit of
C. The investor may close this account after 1 year (t = 1), at which time he will
2.2 Introduction to interest rates                                                    30


withdraw C(1 + i) (see Eq (2.1)). He may then place this sum on deposit in a new
account and close this second account after one further year (t = 2). When this latter
account is closed, the sum withdrawn (again see Eq (2.1)) will be

                  [C(1 + i)] × (1 + i) = C(1 + i)2 = C 1 + 2i + i2
                                                                     


If, however, the investor chooses not to switch accounts after 1 year and leaves his
money in the original account, on closing this account after 2 years, he will receive
C(1 + 2i). Therefore, simply by switching accounts in the middle of the 2-year period,
the investor will receive an additional amount i2 C at the end of the period. This extra
payment is, of course, equal to i(iC) and arises as interest paid (at t = 2 ) on the
interest credited to the original account at the end of the first year.
   From a practical viewpoint, it would be difficult to prevent an investor switching
accounts in the manner described here (or with even greater frequency). Further-
more, the investor, having closed his second account after 1 year, could then deposit
the entire amount withdrawn in yet another account. Any bank would find it ad-
ministratively very inconvenient to have to keep opening and closing accounts in the
manner just described. Moreover, on closing one account, the investor might choose
to deposit his money elsewhere. Therefore, partly to encourage long-term investment
and partly for other practical reasons, it is common commercial practice (at least in
relation to investments of duration greater than 1 year) to pay compound interest
on savings accounts. Moreover, the concepts of compound interest are used in the
assessment and evaluation of investments as discussed throughout this book.
   The essential feature of compound interest is that interest itself earns interest.
The operation of compound interest may be described as follows: consider a savings
account, which pays compound interest at rate i per annum, into which is placed an
initial deposit C at time t = 0. (We assume that there are no further payments to
or from the account.) If the account is closed after 1 year (t = 1) the investor will
receive C(1 + i). More generally, let An be the amount that will be received by the
investor if he closes the account after n years (t = n). It is clear that A1 = C(1 + i).
By definition, the amount received by the investor on closing the account at the end
of any year is equal to the amount he would have received if he had closed the account
1 year previously plus further interest of i times this amount. The interest credited to
the account up to the start of the final year itself earns interest (at rate i per annum)
over the final year. Expressed algebraically, this definition becomes

                                   An+1 = An + iAn



2.3 The rate of interest                                                                  31


or
                                   An+1 = (1 + i)An ,    n≥1                            (2.3)

     Since, by definition, A1 = C(1 + i), Eq (2.3) implies that, for n = 1, 2, . . .,

                                        An = C(1 + i)n                                  (2.4)

     Therefore, if the investor closes the account after n years, he will receive

                                            C(1 + i)n                                   (2.5)

     This payment consists of a return of the initial deposit C, together with accu-
mulated interest (i.e., interest which, if n > 1, has itself earned further interest) of
amount
                                         C [(1 + i)n − 1]                               (2.6)

In our discussion so far, we have assumed that in both these last expressions n is an
integer. However, we will widen the discussion and show that, under very general
conditions, Eqs (2.5) and (2.6) remain valid for all nonnegative values of n.
     Since
                               C(1 + i)t1 (1 + i)t2 = C(1 + i)t1 +t2
                                        

an investor who is able to switch his money between two accounts, both of which pay
compound interest at the same rate, is not able to profit by such action. This is in
contrast with the somewhat anomalous situation, described at the beginning of this
section, which may occur if simple interest is paid.
     Eqs (2.5) and (2.6) should be compared with the corresponding expressions under
the operation of simple interest (i.e., Eqs (2.1) and (2.2)). If interest compounds
(i.e., earns further interest), the effect on the accumulation of an account can be very
significant, especially if the duration of the account or the rate of interest is great.


2.3       The rate of interest
We begin by considering investments in which capital and interest are paid at the end
of a fixed term, there being no intermediate interest or capital payments. This is the
simplest form of a cash flow. An example of this kind of investment is a short-term
deposit in which the lender invests £1, 000 and receives a return of £1, 035 six months
later; £1, 000 may be considered to be a repayment of capital and £35 a payment of
interest, i.e., the reward for the use of the capital for 6 months.
     It is essential in any compound interest problem to define the unit of time. This
may be, for example, a month or a year, the latter period being frequently used in
2.3 The rate of interest                                                              32


practice. In certain situations, however, it is more appropriate to choose a different
period (e.g., 6 months) as the basic time unit. As we shall see, the choice of time scale
often arises naturally from the information one has.
   Consider a unit investment (i.e., of 1 ) for a period of 1 time unit, commencing
at time t, and suppose that 1 + i(t) is returned at time t + 1. We call i(t) the rate
of interest for the period t to t + 1. One sometimes refers to i(t) as the effective rate
of interest for the period, to distinguish it from nominal rate of interest, which will
be discussed later. If it is assumed that the rate of interest does not depend on the
amount invested, the cash returned at time t + 1 from an investment of C at time t
is C[1 + i(t)]. (Note that in practice a higher rate of interest may be obtained from a
large investment than from a small one, but we ignore this point here.)
   Recall from Chapter 1 that the defining feature of compound interest is that it is
earned on previously earned interest; with this in mind, the accumulation of C from
time t = 0 to time t = n (where n is some positive integer) is

                         C[1 + i(0)][1 + i(1)] · · · [1 + i(n − 1)]                 (2.7)

   This is true since proceeds C[1 + i(0)] at time 1 may be invested at this time to
produce C[1 + i(0)][1 + i(1)] at time 2 , and so on.
   Rates of interest are often quoted as percentages. For example, we may speak
of an effective rate of interest (for a given period) of 12.75%. This means that the
effective rate of interest for the period is 0.1275. As an example, £100 invested at
12.75% per annum will accumulate to £100 × (1 + 0.1275) = £112.75 after 1 year.
Alternatively, £100 invested at 12.75% per 2-year period would have accumulated to
£112.75 after 2 years. Computing the equivalent rate of return over different units of
time is an essential skill that we will return to later in this chapter.
   If the rate of interest per period does not depend on the time t at which the
investment is made, we write i(t) = i for all t. In this case the accumulation of an
investment of C for any period of length n time units is, by Eq (2.7),

                                        C(1 + i)n                                   (2.8)

This formula, which will be shown later to hold (under particular assumptions) even
when n is not an integer, is referred to as the accumulation of C for n time units
under compound interest at rate i per time unit.
   The corresponding accumulation under simple interest at rate i per time unit is
defined, as in Chapter 1, as
                                        C(1 + in)                                   (2.9)

This last formula may also be considered to hold for any positive n, not necessarily
2.4 Nominal rates of interest and discount                                                  33


an integer.
   It is interesting to note the connection between the Taylor expansion of the formula
for an n-year accumulation of a unit investment under compound interest, Eq (2.8),
and that for an accumulation under simple interest, Eq (2.9)

                            C(1 + i)n = C 1 + in + O i2
                                                            


In particular, we see that, for small compound interest rates, the higher order terms
are negligible and the two expressions are approximately equal. This reflects that for
small interest rates the interest earned on interest would be negligible.


2.4      Nominal rates of interest and discount
‘Effective’ rates of interest and discount have interest paid once per measurement
period, either at the end of the period or at the beginning of the period.
   ‘Nominal’ is used where interest is paid more (or less) frequently than once per
measurement period.


2.4.1     Nominal rates of interest
We denote the nominal rate of interest payable p times per period by i(p) .
This is also referred to as the rate of interest convertible pthly or compounded
pthly.
   A nominal rate of interest per period, payable pthly, i(p) , is defined to be a rate of
              (p)
interest of i p applied for each pth of a period. For example, a nominal rate of interest
of 6% p.a. convertible quarterly means an interest rate of 64 = 1.5% per quarter or
£1.50 interest on a £100 investment every quarter.
                                                                                      (p)
   Hence, by definition, i(p) is equivalent to a pthly effective rate of interest of i p .
   The effective interest rate i is described by:
                                               p
                                          i(p)
                                      
                                  1+i= 1+                                            (2.10)
                                           p
   It’s noteworthy to remember i(1) = i.
   A critical insight for tackling problems involving nominal rates of interest (or
discount) is choosing the appropriate time unit.
   By aligning the basic time unit with the period corresponding to the nominal rate’s
                                       (p)
convertibility frequency, we can use i p as the effective rate of interest per unit time.
For instance, with an 18% per annum nominal rate convertible monthly, one month
becomes the time unit with a 1.5% interest rate per unit time or £1.50 interest on a

2.5 Accumulation and Discounting Factors                                             34


£100 investment every month.


2.4.2    Nominal rates of discount
The nominal rate of discount payable p times per period is denoted by d(p) .
This rate is often referred to as the rate of discount convertible pthly or com-
pounded pthly.
   A nominal rate of discount per period payable pthly, d(p) , is described as a rate of
             (p)
discount of d p applied for each pth of a period. To provide some context, if we have
a nominal rate of discount of 5% p.a. convertible quarterly, it implies a discount rate
of 54 = 1.25% per quarter, or a discount of £1.25 for every £100 due quarterly.
   The relationship to derive the effective discount rate d is:
                                              p
                                         d(p)
                                     
                                 1−d= 1−                                          (2.11)
                                          p
   A noteworthy point is that d(1) = d, emphasizing the alignment of the effective
discount rate with the nominal rate when the period is singular.


2.5     Accumulation and Discounting Factors
In the ever-evolving realm of financial mathematics, the journey of a single dollar bill
reveals fascinating tales of growth and decline. How much will it be worth in the
future? What’s its present value if promised a few years down the line? To decode
such mysteries, we turn to the concepts of accumulation and discounting factors.
   For two time points, t1 and t2 with t1 < t2 , the accumulation factor, denoted as
A(t1 , t2 ), represents the accumulated value at time t2 of a unit investment made at
time t1 . In essence, it’s the magnifying factor that scales our initial investment over
time.


           Future Value at t2 of an investment of C at t1 = C × A(t1 , t2 )

   Often, when our starting reference point is the present, we use A(n) to represent
the accumulation factor from time 0 to n.
   Suppose A(0, 5) = 1.2. Investing £100 now would yield £120 in 5 years.
   While the accumulation factor focuses on future growth, the discounting factor
brings future values back to the present. We define the present value of payment of 1
due at time n as v(n), hence:

                                     v(n) =                                       (2.12)
                                              A(n)
2.5 Accumulation and Discounting Factors                                                            35

    If A(5) = 1.2, then v(5) = 1.2 = 0.8333. A promise of £1 five years from now is
worth only £0.8333 today.
    Let time be measured in suitable units (e.g., years); for t1 ≤ t2 we define A (t1 , t2 )
to be the accumulation at time t2 of a unit investment made at time t1 for a term
of (t2 − t1 ). It follows by the definition of ih (t) that, for all t and for all h > 0, the
accumulation over a time unit of length h is

                                       A(t, t + h) = 1 + hih (t)                                (2.13)

and hence that
                                            A(t, t + h) − 1
                                 ih (t) =                   ,        h>0                        (2.14)
                                                   h
The quantity A (t1 , t2 ) is often called an accumulation factor, since the accumulation
at time t2 of an investment of the sum C at time t1 is

                                                CA (t1 , t2 )                                   (2.15)

We define A(t, t) = 1 for all t, reflecting that the accumulation factor must be unity
over zero time.
    Now let t0 ≤ t1 ≤ t2 and consider an investment of 1 at time t0 . The proceeds at
time t2 will be A (t0 , t2 ) if one invests at time t0 for term t2 − t0 , or A (t0 , t1 ) × A (t1 , t2 )
if one invests at time t0 for term t1 − t0 and then, at time t1 , reinvests the proceeds
for term t2 − t1 . In a consistent market, these proceeds should not depend on the
course of action taken by the investor. Accordingly, we say that under the principle
of consistency
                                   A (t0 , t2 ) = A (t0 , t1 ) A (t1 , t2 )                     (2.16)

for all t0 ≤ t1 ≤ t2 . It follows easily by induction that, if the principle of consistency
holds,
                         A (t0 , tn ) = A (t0 , t1 ) A (t1 , t2 ) · · · A (tn−1 , tn )          (2.17)

for any n and any increasing set of numbers t0 , t1 , . . . , tn .
    Unless it is stated otherwise, one should assume that the principle of consistency
holds. In practice, however, it is unlikely to be realized exactly because of dealing
expenses, taxation, and other factors. Moreover, it is sometimes true that the accu-
mulation factors implied by certain mathematical models do not in general satisfy the
principle of consistency.




2.6 The force of interest                                                                  36


2.6       The force of interest
Equation (2.14) indicates how ih (t) is defined in terms of the accumulation factor
A(t, t + h). The values of ih (t0 ) for a series of values of h, varying from 1/4 (i.e., 3
months) to 1/365 (i.e., 1 day). The trend of these values should be noted. In practical
situations, it is not unreasonable to assume that, as h becomes smaller and smaller,
ih (t) tends to a limiting value. In general, of course, this limiting value will depend
on t. We therefore assume that for each value of t there is a number δ(t) such that

                                         lim ih (t) = δ(t)                             (2.18)
                                      h→0+


The notation h → 0+ indicates that the limit is considered as h tends to zero ”from
above”, i.e., through positive values. This is, of course, always true in the limit of a
time interval tending to zero.
     It is usual to call δ(t) the force of interest per unit time at time t. In view of
Eq (2.18), δ(t) is sometimes called the nominal rate of interest per unit time at time t
convertible momently. Although it is a mathematical idealization of reality, the force
of interest plays a crucial role in compound interest theory. Note that by combining
Eqs (2.14) and (2.18), we may define δ(t) directly in terms of the accumulation factor
as                                                                  
                                                   A(t, t + h) − 1
                              δ(t) = lim+                                              (2.19)
                                         h→0              h
The force of interest function δ(t) is defined in terms of the accumulation function
A (t1 , t2 ), but when the principle of consistency holds, it is possible, under very general
conditions, to express the accumulation factor in terms of the force of interest. This
result is contained in Theorem below.

     THEOREM If δ(t) and A (t0 , t) are continuous functions of t for t ≥ t0 , and the
principle of consistency holds, then, for t0 ≤ t1 ≤ t2
                                                       Z t2         
                               A (t1 , t2 ) = exp              δ(t)dt                  (2.20)
                                                         t1


The proof of this theorem is not required, but essentially relies on the fact that
Eq (2.19) is the derivative of A with respect to time.

     Equation (2.20) indicates the vital importance of the force of interest. As soon as
δ(t), the force of interest per unit time, is specified, the accumulation factors A (t1 , t2 )
can be determined by Eq (2.20). We may also find ih (t) by Eqs (2.20) and (2.14), and
so                                             hR             i
                                                  t+h
                                         exp       t
                                                        δ(s)ds − 1
                              ih (t) =                                                (2.21)
2.6 The force of interest                                                             37


   The particular case that δ(t) = δ for all t is of significant practical importance. It
is clear that in this case
                                   A (t0 , t0 + n) = eδn                          (2.22)

for all t0 and n ≥ 0. By Eq (2.21), the effective rate of interest per time unit is

                                         i = eδ − 1                               (2.23)

and hence
                                         eδ = 1 + i                               (2.24)

The accumulation factor A (t0 , t0 + n) may therefore be expressed in the alternative
form
                                A (t0 , t0 + n) = (1 + i)n                        (2.25)

We therefore have a generalization of Eq (2.8) to all n ≥ 0, not merely the positive
integers. Notation and theory may be simplified when δ(t) = δ for all t.
   Let us now define
                                     F (t) = A (t0 , t)                           (2.26)

where t0 is fixed and t0 ≤ t. Therefore, F (t) is the accumulation at time t of a unit
investment at time t0 . By Eq (2.20),
                                               Z t
                                  ln F (t) =          δ(s)ds                      (2.27)
                                                 t0


and hence we can express the force of interest in terms of the derivative of the accu-
mulation factor, for t > t0 ,

                                         d             F ′ (t)
                                δ(t) =      ln F (t) =                            (2.28)
                                         dt            F (t)

Although we have assumed so far that δ(t) is a continuous function of time t, in
certain practical problems we may wish to consider rather more general functions. In
particular, we sometimes consider δ(t) to be piecewise. In such cases, the Theorem
and other results are still valid. They may be established by considering δ(t) to be
the limit, in a certain sense, of a sequence of continuous functions.




2.7 Present values of cashflows                                                                        38


2.7        Present values of cashflows
2.7.1       Discrete and continuous payments
In many compound interest problems, one must find the discounted present value of
cashflows due in the future. It is important to distinguish between (a) discrete and
(b) continuous payments.
      Discrete cashflows The present value of the sums ct1 , ct2 , . . . , ctn due at times
t1 , t2 , . . . , tn (where 0 ≤ t1 < t2 < . . . < tn ) is:
                                                                            n
                                                                            X
                      ct1 v (t1 ) + ct2 v (t2 ) + · · · + ctn v (tn ) =           ctj v (tj )       (2.29)
                                                                            j=1

      If the number of payments is infinite, the present value is defined to be:
                                              ∞
                                              X
                                                     ctj v (tj )                                    (2.30)
                                               j=1

      provided that this series converges. It usually will in practical problems.
      Continuously payable cashflows (payment streams) Suppose that T > 0
and that between times 0 and T an investor will be paid money continuously, the
rate of payment at time t being ρ(t) per unit time. What is the present value of
this cashflow?
      In order to answer this question, it is essential to understand what is meant by the
rate of payment of the cashflow at time t. If M (t) denotes the total payment made
between time 0 and time t, then by definition:


                                        ρ(t) = M ′ (t) for all t                                    (2.31)

      Then, if 0 ≤ α < β ≤ T , the total payment received between time α and time β
is:
                                                            Z β
                                   M (β) − M (α) =                 M ′ (t)dt
                                                             α
                                                            Z β                                     (2.32)
                                                        =          ρ(t)dt
                                                             α

      Thus, the rate of payment at any time is simply the derivative of the total amount
paid up to that time, and the total amount paid between any two times is the integral
of the rate of payments over the appropriate time interval.
      Between times t and t + dt the total payment received is M (t + dt) − M (t). If
dt is very small this is approximately M ′ (t)dt or ρ(t)dt. Theoretically, therefore, we
may consider the present value of the money received between times t and t + dt as
2.7 Present values of cashflows                                                           39


v(t)ρ(t)dt. The present value of the entire cashflow is obtained by integration as:
                                      Z T
                                               v(t)ρ(t)dt                              (2.33)

   If T is infinite we obtain, by a similar argument, the present value:
                                      Z ∞
                                                   v(t)ρ(t)dt                          (2.34)

   By combining the results for discrete and continuous cashflows, we obtain the
formula:
                                                   Z ∞
                                 Σct v(t) +                  v(t)ρ(t)dt                (2.35)

   for the present value of a general cashflow (the summation being over those values
of t for which ct the discrete cashflow at time t, is non-zero).
   So far, we have assumed that all payments, whether discrete or continuous, are
positive. If one has a series of income payments (which may be regarded as positive)
and a series of outgoings (which may be regarded as negative) their net present
value is defined as the difference between the value of the positive cashflow and the
value of the negative cashflow.


2.7.2       Valuing cashflows
Consider times t1 and t2 , where t2 is not necessarily greater than t1 . The value at
time t1 of the sum C due at time t2 is defined as:
   (a) if t1 ≥ t2 , the accumulation of C from time t2 until time t1 ; or
   (b) if t1 < t2 , the discounted value at time t1 of C due at time t2 .
   In both cases the value at time t1 of C due at time t2 is:
                                         Z t2       
                                   C exp −     δ(t)dt                                  (2.36)
                                                        t1
                                          Rt             Rt
   Note: The convention that, if t1 > t2 , t12 δ(t)dt = − t21 δ(t)dt.
   Since:
                         Z t2              Z t2                   Z t1
                                δ(t)dt =             δ(t)dt −             δ(t)dt
                           t1                  0                    0

   it follows immediately from equation (2.44) that the value at time t1 of C due at
time t2 is:

                                                   v (t2 )
                                               C                                       (2.37)
                                                   v (t1 )

2.7 Present values of cashflows                                                                                      40


       The value at a general time t1 of a discrete cashflow of ct at time t (for various
values of t ) and a continuous payment stream at rate ρ(t) per time unit may now be
found, by the methods given in Section 1, as:
                                                       Z ∞
                                           v(t)                         v(t)
                                      Σct         +             ρ(t)           dt                                (2.38)
                                          v (t1 )          −∞          v (t1 )
       where the summation is over those values of t for which ct ̸= 0. We note that in
the special case when t1 = 0 (the present time), the value of the cashflow is:
                                                       Z ∞
                                        Σct v(t) +              ρ(t)v(t)dt                                       (2.39)
                                                           −∞

       where the summation is over those values of t for which ct ̸= 0. This is a generalisa-
tion of formula (2.43) to cover the past as well as present or future payments. If there
are incoming and outgoing payments, the corresponding net value may be defined
as the difference between the value of the positive and the negative cashflows.
       If all the payments are due at or after time t1 , their value at time t1 may also be
called their discounted value, and if they are due at or before time t1 , their value
may be referred to as their accumulation. It follows that any value may be expressed
as the sum of a discounted value and an accumulation. This fact is helpful in certain
problems. Also, if t1 = 0 and all the payments are due at or after the present time,
their value may also be described as their (discounted) present value, as defined
by formula (2.43)
       The value at any time t1 of a cashflow may be obtained from its value at another
time t2 by applying the factor v (t2 ) /v (t1 ), i.e.
                    "                          #       "                            #
                         Value at time t1                  Value at time t2             h
                                                                                            v(t2 )
                                                                                                     i
                                                   =                                        v(t1 )
                                                                                                                 (2.40)
                         of cashflow                       of cashflow
       Or
                "                         #                  "                              #
                     Value at time t1                             Value at time t2
                                               [v (t1 )] =                                      [v (t2 )]         (2.41)
                     of cashflow                                  of cashflow
       Each side of equation (2.49) is the value of the cashflow at the present time (time
0 ).
       In particular, by choosing time t2 as the present time and letting t1 = t, we obtain
the result:
                 "                         #       "                                    #               
                        Value at time t                Value at the present                      1
                                               =                                                                 (2.42)
                        of cashflow                    time of cashflow                         v(t)

       These results are useful in many practical examples. The time 0 and the unit of

2.8 Interest income*                                                                     41


time may be chosen so as to simplify the calculations.


2.8         Interest income*
Consider now an investor who wishes not to accumulate money but to receive an
income while keeping his capital fixed at C. If the rate of interest is fixed at i per
time unit, and if the investor wishes to receive income at the end of each time unit, it
is clear that the income will be iC per time unit, payable in arrears, until such time
as the capital is withdrawn.
      However, if interest is paid continuously with force of interest δ(t) at time t then
the income received between times t and t + dt will be Cδ(t)dt.
      So, the total interest income from time 0 to time T will be:
                                                     Z T
                                      I(T ) =              Cδ(t)dt                   (2.43)

      If the investor withdraws the capital at time T , the present values of the income
and capital at time 0 are:
                                               Z T
                                          C          δ(t)v(t)dt                      (2.44)

      and


                                                    Cv(T )                            (2.45)

      Since:


Z T                  Z T            Z t                 Z t        T
      δ(t)v(t)dt =         δ(t) exp −    δ(s)ds dt = − exp −    δ(s)ds     = 1 − v(T )
 0                    0               0                               0      0
                                                                                     (2.46)
      we obtain
                                          Z T
                                 C=C            δ(t)v(t)dt + Cv(T )                  (2.47)

      as one would expect by general reasoning.
      So far, we have described the difference between money returned at the end of the
term and the cash originally invested as ‘interest’. In practice, however, this quantity
may be divided into interest income and capital gains, the term capital loss
being used for a negative capital gain.


