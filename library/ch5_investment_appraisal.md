# 第5章 投资项目评估

Chapter 5

Project Appraisal and Investment
Performance

5.1      Overview
This chapter is largely concerned with a number of applications of compound interest
theory to the assessment of investments and business ventures. These matters are,
of course, considered by accountants, economists, and others as well as by actuaries.
Some writers use terminology and symbols which differ from those usually employed
by actuaries, but there are no differences of principle. The chapter also introduces
the concept of real returns.

   • The net present value (NPV) of a project is calculated from the present values
      of the net cash flows. The project is profitable at a particular rate of interest if
      the NPV is positive. NPVs can be used to compare the profitability of different
      projects at a particular interest rate.

   • The internal rate of return (IRR) is the value of i that solves the equation of
      value for a project. The project is profitable if the IRR is positive. IRRs can be
      used to compare the return per unit investment achieved by different projects.

   • The payback period of a project is the time after which the cumulative cash
      flow of a project becomes positive. The time value of money is not considered
      in the calculation.

   • The discounted payback period is the time after which the cumulative NPV of
      the cash flow of a project becomes positive.




5.2 Net cash flows                                                                      71


5.2      Net cash flows
Suppose that an investor (who may be a private individual or a corporate body in
all that follows) is considering the merits of an investment or business project. The
investment or project will normally require an initial outlay and possibly other outlays
in future, which will be followed by receipts (although in some cases the pattern
of income and outgo is more complicated). The cash for flows associated with the
investment or business venture may be completely fixed (as in the case of a secure
fixed-interest security maturing at a given date), or they may have to be estimated.
The estimation of the cash inflows and outflows associated with a business project
usually requires considerable experience and judgement, and all relevant factors (such
as taxation) should be considered. It is often prudent to perform calculations on
more than one set of assumptions, for example, on the basis of ‘optimistic’, ‘average’,
and ‘pessimistic’ forecasts, respectively. More complicated techniques using statistical
theory, for example, are available to deal with this kind of uncertainty but are beyond
the scope of this book. Precision is not attainable in the estimation of cash flows
for many business projects, and so extreme accuracy is out of place in many of the
calculations that follow.
   Recall that the net cash flow ct at time t (measured in suitable time units) is

                  ct = cash inflow at time t - cash outflow at time t                (5.1)

If any payments may be regarded as continuous, then ρ(t), the net rate of cash flow
per unit time at time t, is defined as

                                   ρ(t) = ρ1 (t) − ρ2 (t)                            (5.2)

where ρ1 (t) and ρ2 (t) denote the rates of inflow and outflow at time t, respectively.


5.3      Net present values and yields
Having ascertained or estimated the net cash flows of the investment or project under
scrutiny, the investor will wish to measure its profitability in relation to other possible
investments or projects. In particular, he may wish to determine whether or not it is
prudent to borrow money to finance the venture.
   Assume for the moment that the investor may borrow or lend money at a fixed rate
of interest i per unit time. The investor could accumulate the net cash flows connected
with the project in a separate account in which interest is payable or credited at this
fixed rate. By the time the project ends (at time T , say), the balance in this account

5.3 Net present values and yields                                                             72


will be                                            Z T
                          X
                                        T −t
                              ct (1 + i)       +         ρ(t)(1 + i)T −t dt                 (5.3)

where the summation extends over all t such that ct ̸= 0.
     The present value at rate of interest i of the net cash flows is called the net present
value at rate of interest i of the investment or business project, and is usually denoted
by NPV(i). Hence,

                                   X                         Z T
                                                   −t
                     N P V (i) =       ct (1 + i)        +         ρ(t)(1 + i)−t dt         (5.4)


(Note that if the project continues indefinitely, the accumulation of Eq. determined
by Eq (5.3) is not defined, but the net present value may be defined by Eq (5.4) with
T = ∞.) If ρ(t) = 0, we obtain a simpler formula resulting from the discrete payments
                                                        X
                                     N P V (i) =              ct v t                        (5.5)

where v = (1 + i)−1 . Since the equation

                                           N P V (i) = 0                                    (5.6)

is the equation of value for the project at the present time, the yield i0 on the transac-
tion is the solution of this equation, provided that a unique solution exists. Conditions
under which the yield exists, and numerical methods for solving Eq (5.6).
     It may readily be shown that N P V (i) is a smooth function of the rate of interest
i and that N P V (i) → c0 as i → ∞.
     In economics and accountancy, the yield per annum is often referred to as the
internal rate of return (IRR) or the yield to redemption. The latter term is frequently
used when dealing with fixed-interest securities, for which the ’running’ yield is also
considered.
     The practical interpretation of the net present value function N P V (i) and the
yield is as follows. Suppose that the investor may lend or borrow money at a fixed
rate of interest i1 . Since, from Eq (5.4), N P V (i1 ) is the present value at rate of
interest i1 of the net cash flows associated with the project, we conclude that the
project will be profitable if and only if

                                           NPV (i1 ) > 0                                    (5.7)

Also, if the project ends at time T , then the profit (or, if negative, loss) at that time
is
                                     N P V (i1 ) (1 + i1 )T                                 (5.8)
5.4 The comparison of two investment projects                                              73


Let us now assume that, as is usually the case in practice, the yield i0 exists and
N P V (i) changes from positive to negative when i = i0 . Under these conditions, it is
clear that the project is profitable if and only if

                                           i1 < i0                                      (5.9)

i.e., the yield exceeds the rate of interest at which the investor may lend or borrow
money.


5.4      The comparison of two investment projects
Suppose now that an investor is comparing the merits of two possible investments or
business ventures, which we call projects A and B, respectively. We assume that the
borrowing powers of the investor are not limited.
   Let N P VA (i) and N P VB (i) denote the respective net present value functions, and
let iA and iB denote the yields (which we shall assume to exist). It might be thought
that the investor should always select the project with the higher yield, but this is not
always the best policy. A better criterion to use is the profit at time T (the date when
the later of the two projects ends) or, equivalently, the net present value, calculated
at the rate of interest i1 at which the investor may lend or borrow money. The reason
is that A is the more profitable venture if

                                 N P VA (i1 ) > N P VB (i1 )                           (5.10)

The fact that iA > iB may not imply that N P VA (i1 ) > N P VB (i1 ) is illustrated in
Figure 6.3.1. Although iA is larger than iB , the N P V (i) functions ’cross over’ at i′ .
It follows that N P VB (i1 ) > N P VA (i1 ) for any i1 < i′ , where i′ is the cross-over rate.
There may even be more than one cross-over point, in which case the range of interest
rates for which Project A is more profitable than Project B is more complicated. This
behaviour reflects that the NPVs are sensitive to the profile of the timings of cash
flows and the term of the investment.


5.5      Payback periods
So far we have assumed that the investor may borrow or lend money at the same
rate of interest i1 . In practice, however, he will probably have to pay a higher rate of
interest (j1 , say) on borrowings than the rate (j2 , say) he receives on investments. The
difference j1 − j2 between these rates of interest depends on various factors, including
the creditworthiness of the investor and the expense of raising a loan.
5.5 Payback periods                                                                              74


   The concepts of net present value and yield are, in general, no longer meaningful
in these circumstances. We must calculate the accumulation of the net cash flows
from first principles, the rate of interest depending on whether or not the investor’s
account is in credit. In many practical problems, the balance in the investor’s account
(i.e., the accumulation of net cash flows) will be negative until a certain time t1 and
positive afterwards, except, perhaps, when the project ends.
   In many practical problems, the net cash flow changes sign only once, this change
being from negative to positive. In these circumstances the balance in the investor’s
account will change from negative to positive at a unique time t1 , or it will always be
negative, in which case the project is not viable. If this time t1 exists, it is referred
to as the discounted payback period (DPP). It is the smallest value of t such that
A(t) ≥ 0, where

                             X                            Z t
                                                t−s
                   A(t) =          cs (1 + j1 )       +         ρ(s) (1 + j1 )t−s ds          (5.11)
                             s≤t                           0


Note that t1 does not depend on j2 but only on j1 , the rate of interest applicable to
the investor’s borrowings.
   Suppose that the project ends at time T .                      If A(T ) < 0 (or, equivalently, if
NPV (j1 ) < 0 ), the project has no discounted payback period and is not profitable.
If the project is viable (i.e., there is a discounted payback period t1 ), the accumulated
profit when the project ends at time T is
                                                           X
                       P =A (t1 ) (1 + j2 )T −t1 +                ct (1 + j2 )T −t
                                                           t>t1
                                   Z T
                             +           ρ(t) (1 + j2 )T −t dt
                                    t1


This follows since the net cash flow is accumulated at rate j2 (the rate of interest
applicable to the investor’s deposits) after the discounted payback period has elapsed.
   If interest is ignored in Eq (5.11) (i.e., if we put j1 = 0 ), the resulting period is
called the payback period.
   The discounted payback period is often employed when considering a single in-
vestment of C, say, in return for a series of payments each of R, say, payable annually
in arrears for n years. The discounted payback period t1 years is clearly the smallest
integer t such that A∗ (t) ≥ 0, where

                       A∗ (t) = −C (1 + j1 )t + Rst                  at rate j1




5.6 The effects of inflation                                                           75


i.e., the smallest integer t such that

                                 Rat ≥ C          at rate j1

The project is therefore viable if t1 ≤ n, in which case the accumulated profit after n
years is clearly
                     P = A∗ (t1 ) (1 + j2 )n−t1 + Rsn−t1       at rate j2

   If the rates (or forces) of interest on borrowing and/or lending are assumed to
vary with time, one may find the accumulation of the net cash flow. In practice,
the determination of the net cash flow and its accumulation at any future time is
done computationally. It is usual in many such calculations to consider the net cash
flow and its accumulation on a yearly basis. The resulting analysis may be easily
understood and interpreted by those responsible for making investment decisions.


5.6      The effects of inflation
Consider the simplest situation in which an investor can lend and borrow money at
the same rate of interest i1 . In certain economic conditions, the investor may assume
that some or all elements of the future cash flows should incorporate allowances for
inflation (i.e., increases in prices and wages). The extent to which the various items in
the cash flow are subject to inflation may differ. For example, wages may increase more
rapidly than the prices of certain goods, or vice versa, and some items (such as the
income from rent-controlled property) may not rise at all, even in highly inflationary
conditions.
   The case when all items of cash flow are subject to the same rate of escalation e
per time unit is of special interest. In this case we find or estimate cei and ρe (t), the
net cash flow, and the net rate of cash flow allowing for escalation at rate e per unit
time, by the formulae

                                         cet = (1 + e)t ct                         (5.12)
                                   ρe (t) = (1 + e)t ρ(t)                          (5.13)

where ct and ρ(t) are estimates of the net cash flow and the net rate of cash flow,
respectively, at time t without any allowance for inflation. It follows that, with al-
lowance for inflation at rate e per unit time, the net present value of the investment




5.6 The effects of inflation                                                            76


or business project at rate of interest i is
                        X                            Z ∞
                                               −t
         N P Ve (i) =              t
                         ct (1 + e) (1 + i) +      ρ(t)(1 + e)t (1 + i)−t dt
                       X                Z ∞                                         (5.14)
                     =   ct (1 + j)−t +     ρ(t)(1 + j)−t dt


where
                                                     1+i
                                         1+j =
                                                     1+e
or
                                                    i−e
                                           j=                                       (5.15)
                                                    1+e
If e is not too large, one sometimes uses the approximation

                                           j ≈i−e                                   (5.16)

Combining Eqs (5.14) and (5.15), we have
                                                                   
                                                              i−e
                                N P Ve (i) = N P V0                                 (5.17)
                                                              1+e

where N P V0 is the net present value function with no allowance for inflation. It follows
that, with inflation at rate e per unit time, the yield (or internal rate of return) ie0 of
the project is such that
                                          ie0 − e
                                                  = i0
                                          1+e
where i0 is the corresponding yield if there were no inflation. This means that

                                       ie0 = i0 (1 + e) + e                         (5.18)

or, if e is small,
                                          ie0 ≈ i0 + e                              (5.19)

     These results are of considerable practical importance because projects that are
apparently unprofitable when rates of interest are high may become highly profitable
when even a modest allowance is made for inflation. It is, however, true that in many
ventures the positive cash flow generated in the early years of the venture is insufficient
to pay bank interest, so recourse must be had to further borrowing (unless the investor
has adequate funds of his own). This in itself does not undermine the profitability of
the project, but the investor would require the agreement of his lending institution
before further loans could be obtained, and this might cause difficulties in practice.


